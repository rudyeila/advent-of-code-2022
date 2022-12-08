
test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_input2 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def calculate_priority(char: str) -> int:
    subtrahend = 96 if char.islower() else 38
    return ord(char) - subtrahend

def calculate_intersection(rucksacks: list[list[str]]) -> set: 
    rucksacks = [set(r) for r in rucksacks]
    return set.intersection(*rucksacks)

def get_groups(rucksacks: list[str], group_size = 3) -> list[list[str]]:
    for i in range(0, len(rucksacks), group_size):
        yield rucksacks[i:i + group_size]


def solve_1(input: str) -> int:
    rucksacks = input.split("\n")
    total_priority = 0
    for rucksack in rucksacks:
        rucksack = [*rucksack]
        first_comp = rucksack[0:len(rucksack)//2]
        second_comp = rucksack[len(rucksack)//2:] 
        intersec = calculate_intersection([set(first_comp), set(second_comp)])

        for char in intersec:
            total_priority += calculate_priority(char)
    return total_priority


def solve_2(input: str) -> int:
    rucksacks = input.split("\n")
    for rucksack in rucksacks:
        rucksack = [*rucksack]
    groups = get_groups(rucksacks)

    total_priority = 0
    for group in groups:
        intersec = calculate_intersection(group)

        for char in intersec:
            total_priority += calculate_priority(char)
    return total_priority


if __name__ == '__main__':
    assert solve_1(test_input) == 157
    assert solve_2(test_input2) == 70

    with open("input.txt", 'r+') as f:
        input = f.read()
        assert solve_1(input) == 8240
        assert solve_2(input) == 2587

        total_priority = solve_2(input)
        print(total_priority)