import pprint

OUT = []


def read_input(input: str) -> list[str]:
    with open(input, "r") as f:
        lines = f.readlines()
        return lines


def find_right(input: list[str], x: int, y: int) -> bool:
    global OUT
    cols = len(input[0].strip())
    if y + 3 < cols:
        if input[x][y + 1] == "M" and input[x][y + 2] == "A" and input[x][y + 3] == "S":
            OUT[x][y] = "X"
            OUT[x][y + 1] = "M"
            OUT[x][y + 2] = "A"
            OUT[x][y + 3] = "S"
            return True
    return False


def find_left(input: list[str], x: int, y: int) -> bool:
    if y - 3 >= 0:
        if input[x][y - 1] == "M" and input[x][y - 2] == "A" and input[x][y - 3] == "S":
            OUT[x][y] = "X"
            OUT[x][y - 1] = "M"
            OUT[x][y - 2] = "A"
            OUT[x][y - 3] = "S"
            return True
    return False


def find_down(input: list[str], x: int, y: int) -> bool:
    rows = len(input)
    if x + 3 < rows:
        if input[x + 1][y] == "M" and input[x + 2][y] == "A" and input[x + 3][y] == "S":
            OUT[x][y] = "X"
            OUT[x + 1][y] = "M"
            OUT[x + 2][y] = "A"
            OUT[x + 3][y] = "S"
            return True
    return False


def find_up(input: list[str], x: int, y: int) -> bool:
    if x - 3 >= 0:
        if input[x - 1][y] == "M" and input[x - 2][y] == "A" and input[x - 3][y] == "S":
            OUT[x][y] = "X"
            OUT[x - 1][y] = "M"
            OUT[x - 2][y] = "A"
            OUT[x - 3][y] = "S"
            return True
    return False


def find_downright(input: list[str], x: int, y: int) -> bool:
    rows = len(input)
    cols = len(input[0])

    if x + 3 < rows and y + 3 < cols:
        if (
            input[x + 1][y + 1] == "M"
            and input[x + 2][y + 2] == "A"
            and input[x + 3][y + 3] == "S"
        ):
            OUT[x][y] = "X"
            OUT[x + 1][y + 1] = "M"
            OUT[x + 2][y + 2] = "A"
            OUT[x + 3][y + 3] = "S"
            return True
    return False


def find_downleft(input: list[str], x: int, y: int) -> bool:
    rows = len(input)

    if x + 3 < rows and y - 3 >= 0:
        if (
            input[x + 1][y - 1] == "M"
            and input[x + 2][y - 2] == "A"
            and input[x + 3][y - 3] == "S"
        ):
            OUT[x][y] = "X"
            OUT[x + 1][y - 1] = "M"
            OUT[x + 2][y - 2] = "A"
            OUT[x + 3][y - 3] = "S"
            return True
    return False


def find_upright(input: list[str], x: int, y: int) -> bool:
    cols = len(input[0])

    if x - 3 >= 0 and y + 3 < cols:
        if (
            input[x - 1][y + 1] == "M"
            and input[x - 2][y + 2] == "A"
            and input[x - 3][y + 3] == "S"
        ):
            OUT[x][y] = "X"
            OUT[x - 1][y + 1] = "M"
            OUT[x - 2][y + 2] = "A"
            OUT[x - 3][y + 3] = "S"
            return True
    return False


def find_upleft(input: list[str], x: int, y: int) -> bool:
    if (x - 3) >= 0 and (y - 3) >= 0:
        if (
            input[x - 1][y - 1] == "M"
            and input[x - 2][y - 2] == "A"
            and input[x - 3][y - 3] == "S"
        ):
            OUT[x][y] = "X"
            OUT[x - 1][y - 1] = "M"
            OUT[x - 2][y - 2] = "A"
            OUT[x - 3][y - 3] = "S"
            return True
    return False


def part1(input: list[str]) -> int:
    sum = 0

    numrows = len(input)
    numcols = len(input[0].strip())

    # print(numrows, numcols)
    global OUT

    for i in range(numrows):
        OUT.append([])
        for j in range(numcols):
            OUT[i].append(".")

    # pprint.pprint(OUT)

    for i in range(numrows):
        for j in range(numcols):
            if input[i][j] == "X":
                if find_right(input, i, j):
                    sum += 1
                if find_left(input, i, j):
                    sum += 1
                if find_down(input, i, j):
                    sum += 1
                if find_up(input, i, j):
                    sum += 1
                if find_downright(input, i, j):
                    sum += 1
                if find_downleft(input, i, j):
                    sum += 1
                if find_upright(input, i, j):
                    sum += 1
                if find_upleft(input, i, j):
                    sum += 1

    # pprint.pprint(OUT)
    return sum


def xmas(input: list[str], x: int, y: int) -> bool:
    found = 0
    if (input[x - 1][y - 1] == "M" and input[x + 1][y + 1] == "S") or (
        input[x - 1][y - 1] == "S" and input[x + 1][y + 1] == "M"
    ):
        found += 1
    if (input[x + 1][y - 1] == "M" and input[x - 1][y + 1] == "S") or (
        input[x + 1][y - 1] == "S" and input[x - 1][y + 1] == "M"
    ):
        found += 1
    if found == 2:
        return True
    else:
        return False


def part2(input: list[str]) -> int:
    sum = 0

    numrows = len(input)
    numcols = len(input[0].strip())

    for i in range(1, numrows - 1):
        for j in range(1, numcols - 1):
            if input[i][j] == "A":
                if xmas(input, i, j):
                    sum += 1
    return sum


if __name__ == "__main__":
    assert part1(read_input("test.txt")) == 18

    print(part1(read_input("input.txt")))

    assert part2(read_input("test.txt")) == 9
    print(part2(read_input("input.txt")))
