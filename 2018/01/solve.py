def read_input(input: str) -> list[str]:
    with open(input, "r") as f:
        inputs = f.readlines()
        return inputs


def part1(input: list[str]) -> int:
    sum = 0
    for i in input:
        n = int(i[1:])
        if i[0] == "+":
            sum += n
        else:
            sum -= n
    return sum


def part2(input: list[str]) -> int:
    f = [0]
    sum = 0
    i = 0
    while True:
        n = int(input[i][1:])
        if input[i][0] == "+":
            sum += n
        else:
            sum -= n
        if sum in f:
            return sum
        else:
            f.append(sum)
            i += 1
            if len(input) == i:
                i = 0


if __name__ == "__main__":
    assert part1(["+1", "+1", "+1"]) == 3
    assert part1(["+1", "+1", "-2"]) == 0
    assert part1(["-1", "-2", "-3"]) == -6
    print(part1(read_input("input.txt")))

    assert part2(["+1", "-1"]) == 0
    assert part2(["+3", "+3", "+4", "-2", "-4"]) == 10
    assert part2(["-6", "+3", "+8", "+5", "-6"]) == 5
    assert part2(["+7", "+7", "-2", "-7", "-4"]) == 14
    print(part2(read_input("input.txt")))
