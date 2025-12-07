def read_input(input: str) -> list[str]:
    return open(input, "r").readlines()


def part1(rotation: list[str]) -> int:
    count = 0
    needle = 50
    for line in rotation:
        dir = line[0]
        steps = int(line[1:])
        if dir == "L":
            needle -= steps
        elif dir == "R":
            needle += steps
        needle %= 100
        if (needle % 100) == 0:
            count += 1
    return count


def part2(rotation: list[str]) -> int:
    count = 0
    needle = 50
    for line in rotation:
        dir = line[0]
        steps = int(line[1:])
        count += steps // 100
        steps = steps % 100
        if dir == "L":
            if steps > needle and needle != 0:
                count += (steps // 100) + 1
            needle = (needle - steps) % 100
            if needle % 100 == 0:
                count += 1
        elif dir == "R":
            if steps > (100 - needle) and needle != 0:
                count += (steps // 100) + 1
            needle = (needle + steps) % 100
            if needle % 100 == 0:
                count += 1
    return count


if __name__ == "__main__":
    testinput = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert part1(testinput) == 3
    assert part2(testinput) == 6

    data = read_input("input.txt")
    print(part1(data))
    print(part2(data))
