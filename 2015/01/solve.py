def read_input(input: str) -> str:
    return open(input, "r").readline().strip()


def part1(input: str) -> int:
    return input.count("(") - input.count(")")


def part2(input: str) -> int:
    pos = 0
    for i, c in enumerate(input):
        if c == "(":
            pos += 1
        else:
            pos -= 1
        if pos == -1:
            return i + 1
    return 0


if __name__ == "__main__":
    input = read_input("input.txt")
    print(part1(input))
    print(part2(input))
