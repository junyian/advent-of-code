def read_input(input: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            a, b = line.strip().split("   ")
            left.append(int(a))
            right.append(int(b))
    return (left, right)


def part1(input: tuple[list[int], list[int]]) -> int:
    sum = 0
    left = sorted(input[0])
    right = sorted(input[1])
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum


def part2(input: tuple[list[int], list[int]]) -> int:
    sum = 0
    for i in range(len(input[0])):
        sum += input[0][i] * input[1].count(input[0][i])
    return sum


if __name__ == "__main__":
    testinput = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    assert part1(testinput) == 11
    assert part2(testinput) == 31

    input = read_input("input.txt")
    print(part1(input))
    print(part2(input))
