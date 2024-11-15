directions = [
    (0, 1),  # N
    (1, 0),  # E
    (0, -1),  # S
    (-1, 0),  # W
]


def read_input(input: str) -> list[str]:
    with open(input, "r") as f:
        inputs = f.readline().strip().split(", ")
        return inputs


def part1(input: list[str]) -> int:
    x, y = 0, 0
    current_direction = 0

    for i in input:
        if i[0] == "R":
            current_direction = (current_direction + 1) % 4
        elif i[0] == "L":
            current_direction = (current_direction - 1) % 4
        x += int(i[1:]) * directions[current_direction][0]
        y += int(i[1:]) * directions[current_direction][1]
    return abs(x) + abs(y)


def part2(input: list[str]) -> int:
    x, y = 0, 0
    current_direction = 0
    visited = set()

    for i in input:
        if i[0] == "R":
            current_direction = (current_direction + 1) % 4
        elif i[0] == "L":
            current_direction = (current_direction - 1) % 4
        for _ in range(int(i[1:])):
            x += directions[current_direction][0]
            y += directions[current_direction][1]
            if (x, y) not in visited:
                visited.add((x, y))
            else:
                return abs(x) + abs(y)
    return 0


if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))
