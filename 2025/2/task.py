import os


def read_file(file_path, strip=True, split_char="\n"):
    with open(file_path, "r") as file:
        content = file.read()
        if strip:
            content = content.strip()
        if split_char:
            content = content.split(split_char)
        return content


def task1(data, debug=False):
    invalid_arr = []
    for item in data:
        range_parts = item.split("-")
        if len(range_parts) != 2:
            continue
        start, end = range_parts
        if not (start.isdigit() and end.isdigit()):
            continue
        start_num = int(start)
        end_num = int(end)

        for num in range(start_num, end_num + 1):
            if len(str(num)) % 2 == 0:
                num_str = str(num)
                mid = len(num_str) // 2
                left = num_str[:mid]
                right = num_str[mid:]
                if left == right:
                    if debug:
                        print(item, ": ", num_str, " ", left, "==", right)
                    invalid_arr.append(num)
    return sum([int(x) for x in invalid_arr])


def task2(data, debug=False):
    invalid_arr = []
    for item in data:
        range_parts = item.split("-")
        if len(range_parts) != 2:
            continue
        start, end = range_parts
        if not (start.isdigit() and end.isdigit()):
            continue
        start_num = int(start)
        end_num = int(end)

        for num in range(start_num, end_num + 1):
            num_str = str(num)
            length = len(num_str)
            hit = False

            for part_size in range(1, length + 1):
                if length % part_size != 0:
                    continue
                parts = [
                    num_str[i : i + part_size] for i in range(0, length, part_size)
                ]

                if len(parts) >= 2 and len(set(parts)) == 1:
                    if debug:
                        print(f"{item}: {num_str}  {len(parts)} parts of '{parts[0]}'")
                    invalid_arr.append(num)
                    hit = True
                    break
            if hit:
                continue

    return sum([int(x) for x in invalid_arr])


def test_task1():
    test_data = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
    ]
    test_result = 1227775554
    result = task1(test_data)
    assert result == test_result
    print("test_task1 passed")


def test_task2():
    test_data = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]
    test_result = 4174379265
    result = task2(test_data, True)
    assert result == test_result
    print("test_task2 passed")


def run_tests():
    test_task1()
    test_task2()


def run_task1():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_file(filepath, split_char=",")
    result = task1(input_data)
    print("Part 1: " + str(result))


def run_task2():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_file(filepath, split_char=",")
    result = task2(input_data)
    print("Part 2: " + str(result))


# run_tests()
run_task1()
run_task2()
