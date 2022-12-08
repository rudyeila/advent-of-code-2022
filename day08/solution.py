test_input = """30373
25512
65332
33549
35390"""


def is_visible_from_left(grid, x, y):
    height = grid[y][x]
    relevant_row = grid[y][0:x]
    relevant_row.reverse()
    viewing_distance = 0
    for tree_h in relevant_row:
        if tree_h >= height:
            return viewing_distance + 1
        else:
            viewing_distance += 1
    return viewing_distance

def is_visible_from_right(grid, x, y):
    if x == len(grid[y]) - 1:
        return 0 
    height = grid[y][x]
    relevant_row = grid[y][x+1:]
    viewing_distance = 0
    for tree_h in relevant_row:
        if tree_h >= height:
            return viewing_distance + 1
        else:
            viewing_distance += 1
    return viewing_distance

def is_visible_from_top(grid, x, y):
    height = grid[y][x]
    relevant_col = [grid[i][x] for i in range(0, y)]
    relevant_col.reverse()
    viewing_distance = 0
    for tree_h in relevant_col:
        if tree_h >= height:
            return viewing_distance + 1
        else:
            viewing_distance += 1
    return viewing_distance


def is_visible_from_bottom(grid, x, y):
    if y == len(grid) - 1:
        return 0 
    height = grid[y][x]
    relevant_col = [grid[i][x] for i in range(y+1, len(grid))]
    viewing_distance = 0
    for tree_h in relevant_col:
        if tree_h >= height:
            return viewing_distance + 1
        else:
            viewing_distance += 1
    return viewing_distance  

def get_grid(input: str) -> int:
    rows = input.split("\n")
    grid = [[int(height) for height in row] for row in rows]
    return grid

def solve_part1(input: str) -> int:
    grid = get_grid(input)
    
    scores = list(list())
    highest_score = 0
    for x in range(len(grid)):
        scores.append(list())
        for y in range(len(grid[x])):
            scores[x].append(0)
            top = is_visible_from_top(grid, x, y)
            left = is_visible_from_left(grid, x, y)
            right = is_visible_from_right(grid, x, y)
            bottom = is_visible_from_bottom(grid, x, y)
            score = top * left * right * bottom
            if score > highest_score:
                highest_score = score
            scores[x][y] = score
    return highest_score

if __name__ == "__main__":
    # print(solve_part1(test_input))

    with open("input.txt", "r") as f:
        input = f.read()
        print(solve_part1(input))