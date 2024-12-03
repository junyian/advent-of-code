def read_input(input: str) -> list[list[int]]:
    with open(input, "r") as f:
        lines = f.readlines()
        lines = [line.strip().split(" ") for line in lines]
        result = []
        for line in lines:
            line_ints = [int(v) for v in line]
            result.append(line_ints)
        return result


def isSafe(input: list[int]) -> bool:
    if input[0] > input[1]:
        for i in range(len(input) - 1):
            diff = input[i] - input[i + 1]
            if diff < 1 or diff > 3:
                return False
    else:
        for i in range(len(input) - 1):
            diff = input[i + 1] - input[i]
            if diff < 1 or diff > 3:
                return False
    return True


def part1(input: list[list[int]]) -> int:
    sum = 0
    for i in input:
        if isSafe(i):
            sum += 1
    return sum


def part2(input: list[list[int]]) -> int:
    sum = 0
    for i in input:
        if not isSafe(i):
            for j in range(len(i)):
                i2 = i.copy()
                i2.pop(j)
                if isSafe(i2):
                    sum += 1
                    break
        else:
            sum += 1
    return sum


if __name__ == "__main__":
    testinput = read_input("test.txt")
    assert part1(testinput) == 2
    assert part2(testinput) == 4

    input = read_input("input.txt")
    print(part1(input))
    print(part2(input))
