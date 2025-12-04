from pathlib import Path


def read_file(file_path, strip=True, split_char="\n"):
    with open(file_path, "r") as file:
        content = file.read()
        if strip:
            content = content.strip()
        return content.split(split_char)


class Task:
    """Base class for AOC tasks"""

    def __init__(self, day: int):
        self.day = day
        self.input_file = Path(__file__).parent / str(day) / "input.txt"

    def read_input(self) -> list[str]:
        """Read input file"""
        return read_file(str(self.input_file), strip=True, split_char="\n")

    def run_tests(self):
        """Override this to run tests"""
        pass

    def part1(self, data: list[str]) -> int:
        """Override this for part 1 logic"""
        return 0

    def part2(self, data: list[str]) -> int:
        """Override this for part 2 logic"""
        return 0

    def run(self):
        """Run both parts"""
        print(f"=== Day {self.day} ===")

        try:
            self.run_tests()
            print("✓ All tests passed\n")
        except Exception as e:
            print(f"✗ Tests failed: {e}\n")
            return

        data = self.read_input()
        result1 = self.part1(data)
        print(f"Part 1: {result1}")

        result2 = self.part2(data)
        print(f"Part 2: {result2}")
