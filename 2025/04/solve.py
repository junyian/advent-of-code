def read_input(input: str) -> list[str]:
    return [line.strip() for line in open(input, "r").readlines()]


def part1(inputs: list[str]) -> int:
    sum = 0

    row_count = len(inputs)
    col_count = len(inputs[0])

    for r in range(row_count):
        for c in range(col_count):
            if inputs[r][c] == ".":
                continue
            else:
                count = 0
                # up
                if r > 0 and inputs[r - 1][c] == "@":
                    count += 1
                # down
                if r < (row_count - 1) and inputs[r + 1][c] == "@":
                    count += 1
                # left
                if c > 0 and inputs[r][c - 1] == "@":
                    count += 1
                # right
                if c < (col_count - 1) and inputs[r][c + 1] == "@":
                    count += 1
                # upper left
                if r > 0 and c > 0 and inputs[r - 1][c - 1] == "@":
                    count += 1
                # upper right
                if r > 0 and c < (col_count - 1) and inputs[r - 1][c + 1] == "@":
                    count += 1
                # lower left
                if r < (row_count - 1) and c > 0 and inputs[r + 1][c - 1] == "@":
                    count += 1
                # lower right
                if (
                    r < (row_count - 1)
                    and c < (col_count - 1)
                    and inputs[r + 1][c + 1] == "@"
                ):
                    count += 1
                if count <= 3:
                    sum += 1
    return sum


def part2(inputs: list[str]) -> int:
    sum = 0

    row_count = len(inputs)
    col_count = len(inputs[0])

    # Convert strings to lists of characters so we can modify them
    inputs2 = [list(row) for row in inputs]

    while True:
        tmp_inputs = [row.copy() for row in inputs2]
        tmp_sum = 0

        for r in range(row_count):
            for c in range(col_count):
                if tmp_inputs[r][c] == ".":
                    continue
                else:
                    count = 0
                    # up
                    if r > 0 and tmp_inputs[r - 1][c] == "@":
                        count += 1
                    # down
                    if r < (row_count - 1) and tmp_inputs[r + 1][c] == "@":
                        count += 1
                    # left
                    if c > 0 and tmp_inputs[r][c - 1] == "@":
                        count += 1
                    # right
                    if c < (col_count - 1) and tmp_inputs[r][c + 1] == "@":
                        count += 1
                    # upper left
                    if r > 0 and c > 0 and tmp_inputs[r - 1][c - 1] == "@":
                        count += 1
                    # upper right
                    if (
                        r > 0
                        and c < (col_count - 1)
                        and tmp_inputs[r - 1][c + 1] == "@"
                    ):
                        count += 1
                    # lower left
                    if (
                        r < (row_count - 1)
                        and c > 0
                        and tmp_inputs[r + 1][c - 1] == "@"
                    ):
                        count += 1
                    # lower right
                    if (
                        r < (row_count - 1)
                        and c < (col_count - 1)
                        and tmp_inputs[r + 1][c + 1] == "@"
                    ):
                        count += 1
                    if count <= 3:
                        inputs2[r][c] = "."
                        tmp_sum += 1
        sum += tmp_sum
        if tmp_sum == 0:
            break
    return sum


if __name__ == "__main__":
    testinput = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    assert part1(testinput) == 13
    assert part2(testinput) == 43

    data = read_input("input.txt")
    print(part1(data))
    print(part2(data))
