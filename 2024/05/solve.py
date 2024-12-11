def read_input(input: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    with open(input, "r") as f:
        lines = f.readlines()
        rules = {}
        updates = []
        for line in lines:
            if "|" in line:
                a, b = line.strip().split("|")
                if int(a) not in rules:
                    rules[int(a)] = []
                if int(b) not in rules:
                    rules[int(b)] = []
                rules[int(a)].append([int(a), int(b)])
                rules[int(b)].append([int(a), int(b)])
            elif "," in line:
                pages = line.strip().split(",")
                pages = [int(page) for page in pages]
                updates.append(pages)

        return (rules, updates)


def isInOrder(update: list[int], rules: dict[int, list[int]]) -> bool:
    for i in range(1, len(update) - 1):
        rule = rules[update[i]]
        for r in rule:
            try:
                if r[0] == update[i]:
                    loc = update.index(r[1])
                    if loc < i:
                        return False
                elif r[1] == update[i]:
                    loc = update.index(r[0])
                    if loc > i:
                        return False
            except ValueError as _:
                pass

    return True


def sortUpdate(update: list[int], rules: dict[int, list[int]]) -> list[int]:
    restart = True
    updated = update.copy()
    while restart is True:
        sorted = False
        for i in range(1, len(update) - 1):
            rule = rules[updated[i]]
            for r in rule:
                try:
                    if r[0] == updated[i]:
                        loc = updated.index(r[1])
                        if loc < i:
                            tmp = updated[i]
                            updated[i] = updated[loc]
                            updated[loc] = tmp
                            sorted = True
                    elif r[1] == updated[i]:
                        loc = updated.index(r[0])
                        if loc > i:
                            tmp = updated[i]
                            updated[i] = updated[loc]
                            updated[loc] = tmp
                            sorted = True
                except ValueError as _:
                    pass
        if sorted is False:
            restart = False
    return updated


def part1(input: tuple[dict[int, list[int]], list[list[int]]]) -> int:
    sum = 0
    rules = input[0]
    updates = input[1]

    for update in updates:
        if isInOrder(update, rules):
            sum += update[len(update) // 2]

    return sum


def part2(input: tuple[dict[int, list[int]], list[list[int]]]) -> int:
    sum = 0
    rules = input[0]
    updates = input[1]

    for update in updates:
        updated = sortUpdate(update, rules)
        if update != updated:
            sum += updated[len(updated) // 2]
    return sum


if __name__ == "__main__":
    assert part1(read_input("test.txt")) == 143
    print(part1(read_input("input.txt")))

    assert part2(read_input("test.txt")) == 123
    print(part2(read_input("input.txt")))
