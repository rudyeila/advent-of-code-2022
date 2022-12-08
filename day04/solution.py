test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


# def get_pairs(input: str):
#     # pairs = [tuple((ranges[0], ranges[1]) for ranges in line.split(",")) for line in input.split("\n")]
#     pairs = [[ranges for ranges in line.split(",")] for line in input.split("\n")]
#     # lines = input.split("\n")
#     # pairs = []
#     # for line in lines:
#     #     ranges = line.split(",")
#     #     pairs.append((ranges[0], ranges[1]))
#     print(pairs)
#     return pairs 

def parse_ranges(pair: str) -> tuple:
    (range1, range2) = pair
    start1 = int(range1.split("-")[0])
    end1 = int(range1.split("-")[1])
    start2 = int(range2.split("-")[0])
    end2 = int(range2.split("-")[1])
    return start1, end1, start2, end2 

def check_overlap_part1(pair: str) -> bool:
    start1, end1, start2, end2 = parse_ranges(pair)
    
    if start2 >= start1 and end2 <= end1:
        return True
    if start1 >= start2 and end1 <= end2:
        return True 
    return False

def check_overlap_part2(pair: str) -> bool:
    start1, end1, start2, end2 = parse_ranges(pair)
    
    if (start2 >= start1 and start2 <= end1) or (end2 >= start1 and end2 <= end1):
        return True
    if (start1 >= start2 and start1 <= end2) or (end1 >= start2 and end1 <= end2):
        return True
    return False


def solve1(input: str) -> int:
    pairs = [[ranges for ranges in line.split(",")] for line in input.split("\n")]
    overlapping_pairs = 0
    for pair in pairs:
        if check_overlap_part1(pair):
            overlapping_pairs += 1
    return overlapping_pairs

def solve2(input: str) -> int:
    pairs = [[ranges for ranges in line.split(",")] for line in input.split("\n")]
    overlapping_pairs = 0
    for pair in pairs:
        if check_overlap_part2(pair):
            overlapping_pairs += 1

    return overlapping_pairs

if __name__ == "__main__":
    assert solve1(test_input) == 2
    assert solve2(test_input) == 4

    with open("input.txt", "r") as f:
        input = f.read()
        assert solve1(input) == 496
        assert solve2(input) == 847

        print(solve1(input))
        print(solve2(input))
        
