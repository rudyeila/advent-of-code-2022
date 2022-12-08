test_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

def solve(input: str, num_repeating_chars = 4) -> int:
    input_lines = input.split("\n")
    results = []
    for line in input_lines:
        for i in range(0, len(line)-num_repeating_chars):
            cur_window = line[i:i+num_repeating_chars]
            window_set = set(cur_window)
            if len(window_set) == num_repeating_chars: 
                results.append(i+num_repeating_chars)
                break

    return results


if __name__ == "__main__":
    # assert solve1(test_input) == "CMZ"
    # assert solve2(test_input) == "MCD"
    print(solve(test_input, 4))
    print(solve(test_input, 14))


    with open("input.txt", "r") as f:
        input = f.read()

        print(solve(input, 4))
        print(solve(input, 14))

        # print(solve2(input))