import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from common import Task


class Day5(Task):
    def __init__(self):
        super().__init__(int(Path(__file__).parent.name))

    def test_data(self):
        return [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ]

    def get_ingredient_parts(self, data: list[str]) -> tuple[set[str], set[str]]:
        separator_index = data.index("")
        ranges = {line for line in data[:separator_index]}
        available = {int(line) for line in data[separator_index + 1 :]}
        return ranges, available

    def get_ranges(self, ranges: set[str]) -> list[tuple[int, int]]:
        result = []
        for line in ranges:
            start, end = map(int, line.split("-"))
            result.append((start, end))
        return result

    def run_tests(self):
        data = self.test_data()
        result1 = self.part1(data)
        print("Testresult for part 1: ", result1)
        assert result1 == 3
        result2 = self.part2(data)
        print("Testresult for part 2: ", result2)
        assert result2 == 14

    def part1(self, data: list[str]) -> int:
        ranges_str, available = self.get_ingredient_parts(data)
        ranges = self.get_ranges(ranges_str)

        result = set()
        for start, end in ranges:
            for num in available:
                if start <= num <= end:
                    result.add(num)
        return len(result)

    def part2(self, data: list[str]) -> int:
        ranges_str, _ = self.get_ingredient_parts(data)
        ranges = self.get_ranges(ranges_str)
        ranges.sort()
        total = 0
        start, end = ranges[0]

        for new_start, new_end in ranges[1:]:
            if new_start <= end + 1:
                end = max(end, new_end)
            else:
                total += end - start + 1
                start, end = new_start, new_end

        return total + (end - start + 1)


if __name__ == "__main__":
    Day5().run()
