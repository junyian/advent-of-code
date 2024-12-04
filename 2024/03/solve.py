import re


def read_input(input: str) -> list[str]:
    with open(input, "r") as f:
        lines = f.readlines()

        result = []
        for line in lines:
            result += get_tokens(line)
        return result


def get_tokens(input: str) -> list[str]:
    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", input)
    return matches


def part1(input: list[str]) -> int:
    sum = 0
    for i in input:
        match = re.findall(r".*\((\d+),(\d+)\).*", i)
        if match:
            sum += int(match[0][0]) * int(match[0][1])
    return sum


def part2(input: list[str]) -> int:
    sum = 0
    do = True
    for i in input:
        if do:
            match = re.findall(r".*\((\d+),(\d+)\).*", i)
            if match:
                sum += int(match[0][0]) * int(match[0][1])
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False

    return sum


if __name__ == "__main__":
    testinput1 = (
        r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert part1(get_tokens(testinput1)) == 161

    testinput2 = (
        r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert part2(get_tokens(testinput2)) == 48

    input = read_input("input.txt")
    print(part1(input))
    print(part2(input))
