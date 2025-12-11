def read_input(input: str) -> list[str]:
    return open(input, "r").readlines()


def get_max_digit(digits: str, num: int, prev_num: str) -> str:
    if num == 1:
        number = max(digits)
        return prev_num + number
    else:
        tmp_digits = digits[: -(num - 1)]
        number = max(tmp_digits)
        number_pos = tmp_digits.index(number)
        return get_max_digit(digits[number_pos + 1 :], num - 1, prev_num + number)


def part1(inputs: list[str]) -> int:
    sum = 0
    for s in inputs:
        sum += int(get_max_digit(s.strip(), 2, ""))
    return sum


def part2(inputs: list[str]) -> int:
    sum = 0
    for s in inputs:
        sum += int(get_max_digit(s.strip(), 12, ""))
    return sum


if __name__ == "__main__":
    testinput = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    assert part1(testinput) == 357
    assert part2(testinput) == 3121910778619

    data = read_input("input.txt")
    print(part1(data))
    print(part2(data))
