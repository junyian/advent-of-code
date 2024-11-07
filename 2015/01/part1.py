with open("input.txt", "r") as f:
    floor = 0
    for line in f:
        floor += line.count("(") - line.count(")")

print(floor)
