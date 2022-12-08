import re

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class Instruction:

    def __init__(self, instruction_line: str):
        self.n = int(re.search(r'move (.*?) from', instruction_line).group(1))
        self.source = int(re.search(r'from (.*?) to', instruction_line).group(1))
        self.destination = int(re.search(r'to (.*?)$', instruction_line).group(1))

    def __str__(self):
        return f"move {self.n} from {self.source} to {self.destination}"

class Supply:

    def __init__(self, initial_assignment: str) -> None:
        print(initial_assignment)
        initial_assignment = initial_assignment.split("\n")
        initial_assignment.reverse()
        print(initial_assignment)
        self.num_stacks = self._get_num_stacks(initial_assignment[0])

        self.stacks = [list() for i in range(self.num_stacks)]

        for line in initial_assignment[1:]:
            stack_idx = 0
                
            i = 0
            while i < len(line):
                if (i+4) < len(line) and line[i:i+4] == "    ":
                    i += 4
                    stack_idx += 1
                    continue
            
                char = line[i]
                i += 1 
                if char.isalpha():
                    self.append(stack_idx, char)                    
                elif char == " ":
                    stack_idx += 1
                else:
                    continue

    def read_tops(self) -> str:
        result = ""
        for idx in range(len(self.stacks)):
            result += self.read(idx, -1)
        return result

    def append(self, stack_idx,  item) -> None:
        self.stacks[stack_idx].append(item)   

    def pop(self, stack_idx) -> any:
        return self.stacks[stack_idx].pop()    

    def read(self, stack_idx, element_idx) -> any:
        return self.stacks[stack_idx][element_idx] if self.stacks[stack_idx] else ""

    def move_part1(self, number: int, source: int, destination: int):
        for i in range(number):
            item = self.pop(source)
            self.append(destination, item)
        
    def move_part2(self, number: int, source: int, destination: int):
        to_move = []
        for i in range(number):
            to_move.append(self.pop(source))
        to_move.reverse()
        for item in to_move:
            self.append(destination, item)

    def execute_instruction(self, instruction: Instruction, mode="part1"):
        if mode == "part1":
            self.move_part1(instruction.n, instruction.source-1, instruction.destination-1)
        else:
            self.move_part2(instruction.n, instruction.source-1, instruction.destination-1)


    def _get_num_stacks(self, index_line: str) -> int:
        indices = [int(x) for x in index_line.split() if x.isdigit()]
        return max(indices) if indices else None



def solve1(input: str) -> str:
    initial_assignment, instructions = input.split("\n\n")    
    instructions = [Instruction(line) for line in instructions.split("\n")]
    supply = Supply(initial_assignment)

    for instr in instructions:
        print(instr)
        supply.execute_instruction(instr)
        print(supply.read_tops())
        print(supply.stacks)
        print()

    return supply.read_tops()


def solve2(input: str) -> str:
    initial_assignment, instructions = input.split("\n\n")    
    instructions = [Instruction(line) for line in instructions.split("\n")]
    supply = Supply(initial_assignment)

    for instr in instructions:
        print(instr)
        supply.execute_instruction(instr, mode="part2")
        print(supply.read_tops())
        print(supply.stacks)
        print()

    return supply.read_tops()

if __name__ == "__main__":
    assert solve1(test_input) == "CMZ"
    assert solve2(test_input) == "MCD"

    with open("input.txt", "r") as f:
        input = f.read()
        # assert solve1(input) == 496
    #     assert solve2(input) == 847

        # print(solve1(input))
        print(solve2(input))