import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from common import Task


class Day6(Task):
    def __init__(self):
        super().__init__(int(Path(__file__).parent.name))

    def test_data(self):
        return [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]

    def run_tests(self):
        data = self.test_data()
        result_part1 = self.part1(data)
        print("Test Part 1 result:", result_part1)
        assert result_part1 == 4277556
        result_part2 = self.part2(data)
        print("Test Part 2 result:", result_part2)
        assert result_part2 == 3263827

    def part1(self, data: list[str]) -> int:
        last_row_index = len(data) - 1
        problems, operators, results = [], [], []
        allowed_operations = ['+', '*']
        
        for row in data[:last_row_index]:
            chars = row.split(" ")
            char_nums = [int(c) for c in chars if c.strip().isdigit()]
            problems.append(char_nums)
        
        problems = [list(column) for column in zip(*problems)]

        for _, char in enumerate(data[last_row_index]):
            if char in allowed_operations:
                operators.append(char)
    
        for problem, operator in zip(problems, operators):
            if operator == '+':
                results.append(sum(problem))
            elif operator == '*':
                result = 1
                for num in problem:
                    result *= num
                results.append(result)
        
        return sum(results)

    def part2(self, data: list[str], debug=False) -> int:
        last_row_index = len(data) - 1
        rows = data[:last_row_index]
        groups, current_group, operators, results = [], [], [], []
        allowed_operations = ['+', '*']
        row_length = max(len(row) for row in rows)
        
        for _, char in enumerate(data[last_row_index]):
            if char in allowed_operations:
                operators.append(char)
        for char_index in range(row_length):
            column_chars = [row[char_index] for row in rows]
            has_digit = any(c.isdigit() for c in column_chars)
            
            if has_digit:
                nums = [int(c) for c in column_chars if c.isdigit()]
                current_group.append(nums)
            else:
                if current_group:
                    groups.append(current_group)
                    current_group = []
        
        if current_group: # Last group
            groups.append(current_group)
        
        for group, operator in zip(reversed(groups), reversed(operators)):
            if debug:
                print(f"Group with operator '{operator}': {group}")
            numbers = []
            for problem in reversed(group):
                num = int(''.join(map(str, problem)))
                numbers.append(num)
            
            if operator == '+':
                result = sum(numbers)
            elif operator == '*':
                result = 1
                for num in numbers:
                    result *= num
            
            results.append(result)
            if debug:
                print(f"Result: {result}")
        return sum(results)

        
if __name__ == "__main__":
    Day6().run()
