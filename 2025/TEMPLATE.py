import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from common import Task


class DayX(Task):
    def __init__(self):
        super().__init__(int(Path(__file__).parent.name))

    def test_data(self):
        return [
            # Add your test data here
        ]

    def run_tests(self):
        pass

    def part1(self, data: list[str]) -> int:
        pass

    def part2(self, data: list[str]) -> int:
        pass


if __name__ == "__main__":
    DayX().run()
