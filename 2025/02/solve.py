def read_input(input: str) -> list[str]:
    return open(input, "r").readlines()


def part1(ids: str) -> int:
    sum = 0

    parsed_ids = ids.split(",")
    for p in parsed_ids:
        start, end = map(int, p.split("-"))
        for i in range(start, end + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                half = len(str_i) // 2
                if str_i[:half] == str_i[half:]:
                    sum += i
    return sum


def part2(ids: str) -> int:
    result_sum = 0

    parsed_ids = ids.split(",")
    for p in parsed_ids:
        start, end = map(int, p.split("-"))
        for i in range(start, end + 1):
            # print(f"{i=}")

            unique_digits = set(str(i))

            if i < 10:
                continue

            if len(unique_digits) == 1:
                result_sum += i
                continue

            num_digits = len(str(i))
            splits = 2
            len_per_split = num_digits // splits
            max_splits = num_digits // 2

            while splits <= max_splits:
                if splits == 2:
                    a = str(i)[:len_per_split]
                    b = str(i)[len_per_split:]
                    if a == b:
                        result_sum += i
                        break
                elif splits == 3:
                    a = str(i)[:len_per_split]
                    b = str(i)[len_per_split : 2 * len_per_split]
                    c = str(i)[2 * len_per_split :]
                    if a == b == c:
                        result_sum += i
                        break
                elif splits == 4:
                    a = str(i)[:len_per_split]
                    b = str(i)[len_per_split : 2 * len_per_split]
                    c = str(i)[2 * len_per_split : 3 * len_per_split]
                    d = str(i)[3 * len_per_split :]
                    if a == b == c == d:
                        result_sum += i
                        break
                elif splits == 5:
                    a = str(i)[:len_per_split]
                    b = str(i)[len_per_split : 2 * len_per_split]
                    c = str(i)[2 * len_per_split : 3 * len_per_split]
                    d = str(i)[3 * len_per_split : 4 * len_per_split]
                    e = str(i)[4 * len_per_split :]
                    if a == b == c == d == e:
                        result_sum += i
                        break
                splits += 1
                len_per_split = num_digits // splits
    return result_sum


if __name__ == "__main__":
    testinput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    assert part1(testinput) == 1227775554
    assert part2(testinput) == 4174379265

    data = read_input("input.txt")
    print(part1(data[0].strip()))
    print(part2(data[0].strip()))
