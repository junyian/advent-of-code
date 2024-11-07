with open("input.txt", "r") as f:
    pos = 0
    for line in f:
        for i, c in enumerate(line):
            if c == "(":
                pos += 1
            else:
                pos -= 1
            if pos == -1:
                print(i + 1)
                break
