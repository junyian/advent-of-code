def read_input(input: str) -> str:
    with open(input, "r") as f:
        inputs = f.readline().strip()
        return inputs


def part1(input: str) -> int:
    total = 0
    lastval = 0
    for c in input:
        if int(c) == lastval:
            total += lastval
        lastval = int(c)
    if lastval == int(input[0]):
        total += lastval
    return total


def part2(input: str) -> int:
    total = 0
    length = len(input)
    for i, c in enumerate(input[: length // 2]):
        if c == input[(length // 2) + i]:
            total += int(c)
    return total * 2


if __name__ == "__main__":
    assert part1("1122") == 3
    assert part1("1111") == 4
    assert part1("1234") == 0
    assert part1("91212129") == 9
    print(part1(read_input("input.txt")))

    assert part2("1212") == 6
    assert part2("1221") == 0
    assert part2("123425") == 4
    assert part2("123123") == 12
    assert part2("12131415") == 4
    print(part2(read_input("input.txt")))
