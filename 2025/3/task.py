from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from common import read_file


def find_largest_two_digit_combination(data: list[str], debug=False) -> list[str]:
    combinations = []
    for line in data:
        if debug:
            print(line)
        largest_digit = max(line)
        largest_position = [i for i, c in enumerate(line) if c == largest_digit][0]
        if debug:
            print("Largest digit:", largest_digit, "at position", largest_position)

        if largest_position == len(line) - 1:
            # largest cannot be last digit
            largest_digit = max(line[:-1])
            largest_position = [i for i, c in enumerate(line) if c == largest_digit][0]
            if debug:
                print(
                    "Adjusted largest digit:",
                    largest_digit,
                    "at position",
                    largest_position,
                )

        second_largest_digit = max(line[largest_position + 1 :])
        if debug:
            print(
                "Second largest digit after position",
                largest_position,
                "is",
                second_largest_digit,
            )
            print("Combination:", largest_digit + second_largest_digit)
        combinations.append(largest_digit + second_largest_digit)
    return combinations


def find_largest_n_digit_combination(
    data: list[str], n: int = 12, debug=False
) -> list[str]:
    combinations = []
    for line in data:
        num_to_remove = len(line) - n
        digits = list(line)

        for _ in range(num_to_remove):
            removed = False
            for index in range(len(digits) - 1):
                if digits[index] < digits[index + 1]:
                    if debug:
                        print(f"Removing digit {digits[index]} at position {index}")
                    digits.pop(index)
                    removed = True
                    break

            if not removed:
                if debug:
                    print(f"Removing last digit {digits[-1]}")
                digits.pop()

        result = "".join(digits)
        combinations.append(result)

    return combinations


def sum_combinations(combinations: list[str]) -> int:
    total = 0
    for combo in combinations:
        total += int(combo)
    return total


test_data = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]


def test1(test_data=test_data):
    expected_largest_combinations = ["98", "89", "78", "92"]
    result = find_largest_two_digit_combination(test_data)
    print(result)
    assert result == expected_largest_combinations
    expected_sum = sum(int(x) for x in expected_largest_combinations)
    total = sum_combinations(result)
    print(total)
    assert total == expected_sum


def task1():
    input_file = Path(__file__).parent / "input-1.txt"
    data = read_file(str(input_file), strip=True, split_char="\n")
    combinations = find_largest_two_digit_combination(data, debug=False)
    total = sum_combinations(combinations)
    print("Part 1:", total)


def test2(test_data=test_data):
    print(test_data)
    expected_largest_combinations = [
        "987654321111",
        "811111111119",
        "434234234278",
        "888911112111",
    ]
    print("Expected:", expected_largest_combinations)
    result = find_largest_n_digit_combination(test_data, n=12)  # , debug=True)
    print("Result:", result)
    assert result == expected_largest_combinations
    sum_result = sum_combinations(result)
    expected_sum = sum(int(x) for x in expected_largest_combinations)
    print(expected_sum)
    print("Sum Result:", sum_result)
    assert sum_result == expected_sum


def task2():
    input_file = Path(__file__).parent / "input-2.txt"
    data = read_file(str(input_file), strip=True, split_char="\n")
    result = find_largest_n_digit_combination(data, n=12, debug=False)
    sum = sum_combinations(result)
    print("Part 2:", sum)


if __name__ == "__main__":
    # test1()
    task1()
    # test2()
    task2()
