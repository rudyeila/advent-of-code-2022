from typing import Self

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class Node:

    def __init__(self, name: str,  parent = None):
        self.name = name
        self.parent: Node | None = parent

    def get_size(self) -> int:
        raise NotImplementedError()

    def get_abs_path(self) -> str: 
        if self.parent is not None:
            if self.parent.name == "/": 
                return self.parent.get_abs_path() + self.name
            else:
                return self.parent.get_abs_path() + "/" + self.name
        else: 
            return self.name



class Directory(Node):
    
    def __init__(self, name: str, parent: Node = None):
        super().__init__(name, parent)
        self.children: list[Node] = list()
        if self.parent is not None:
            self.parent.add_child(self)

    def add_child(self, child: Node):
        self.children.append(child)

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            size += child.get_size()
        return size

    def find_child_by_name(self, child_name) -> Self | None:
        for child in self.children:
            if child.name == child_name:
                return child
        return None 


    def __str__(self) -> str:
        return f"- {self.name} (dir)"

class File(Node): 

    def __init__(self, name: str, parent: Directory=None, size: int = 1000):
        super().__init__(name, parent)
        self.size = size
        if self.parent is not None:
            self.parent.add_child(self)

    def get_size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        return f"- {self.name} (file, size={self.size})"

class FileSystem:

    def __init__(self):
        self.root_dir = Directory("/")
        self.cur_dir = self.root_dir

    def init_file_system(self, input: str): 
        commands = input.split("\n")
        
        for cmd in commands: 
            if cmd.startswith("$ cd "):
                self.handle_cd(cmd)
            elif cmd.startswith("$ ls"):
                continue
            else:
                if cmd.startswith("dir "):
                    dir_name = cmd[4:]
                    child_dir = self.cur_dir.find_child_by_name(dir_name)
                    if child_dir is None:
                        child_dir = Directory(dir_name, self.cur_dir)
                else: # file
                    size, filename = cmd.split(" ")
                    child = self.cur_dir.find_child_by_name(filename)
                    if child is None:
                        child = File(filename, self.cur_dir, int(size))
                    
    def handle_cd(self, command):
        cd_target = command[5:]
        if cd_target == "..":
            if self.cur_dir.parent is not None:
                self.cur_dir = self.cur_dir.parent
            else:
                self.cur_dir = self.root_dir
        elif cd_target == "/":
            self.cur_dir = self.root_dir
        else: 
            next_dir = self.cur_dir.find_child_by_name(cd_target)
            if next_dir is None: 
                next_dir = Directory(cd_target, self.cur_dir)
            self.cur_dir = next_dir

    def solve_part1(self) -> int:
        q = [self.root_dir]
        visited = []
        total_size = 0
        while q:  
            node = q.pop()

            for child in node.children:
                if child not in visited:
                    visited.append(child)
                    if isinstance(child, Directory):
                        q.append(child)
            
            if node.get_size() <= 100000:
                total_size += node.get_size()
        
        return total_size

    def solve_part2(self) -> int:
        total_space = 70000000
        update_size = 30000000
        used_space = self.root_dir.get_size()
        available_space = total_space - used_space
        needed_space = update_size - available_space
        
        q = [self.root_dir]
        visited = []
        potential_dirs = []
        while q:  
            node = q.pop()
            if node.get_size() >= needed_space:
                potential_dirs.append(node)
            for child in node.children:
                if child not in visited:
                    visited.append(child)
                    if isinstance(child, Directory):
                        q.append(child)

        potential_dirs.sort(key=lambda x: x.get_size())
        return potential_dirs[0].get_size()
    
    def __str__(self) -> str:
        result = ""
        q = [self.root_dir]
        result += str(self.root_dir.get_abs_path()) + "\n"
        while q:
            cur_node = q.pop()
            for child in cur_node.children:
                if isinstance(child, Directory):
                    q.append(child)
                result += str(child.get_abs_path()) + "\n"

        return result 

def solve(input: str) -> int:
    fs = FileSystem()
    fs.init_file_system(input)
    print(fs)
    return (fs.solve_part1(), fs.solve_part2())



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
        print(solve(input))