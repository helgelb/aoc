import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from common import Task


class Day4(Task):
    def __init__(self):
        day = int(Path(__file__).parent.name)
        super().__init__(day)

    def run_tests(self):
        test_data = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        print("Part 1: Number of accessible paper rolls:", self.part1(test_data))
        assert self.part1(test_data) == 13
        print("Tests for part 1 passed")
        print("Part 2: Number of accessible paper rolls:", self.part2(test_data))
        assert self.part2(test_data) == 43
        print("Tests for part2 passed")

    def get_neighbors(
        self, x: int, y: int, data: list[str]
    ) -> tuple[list[tuple[int, int]], int]:
        potential_neighbors = [
            (x - 1, y),  # Left
            (x + 1, y),  # Right
            (x, y - 1),  # Up
            (x, y + 1),  # Down
            (x - 1, y - 1),  # Top-left
            (x + 1, y - 1),  # Top-right
            (x - 1, y + 1),  # Bottom-left
            (x + 1, y + 1),  # Bottom-right
        ]

        valid_neighbors = []
        for nx, ny in potential_neighbors:
            if 0 <= ny < len(data) and 0 <= nx < len(data[ny]):
                if data[ny][nx] == "@":
                    valid_neighbors.append((nx, ny))

        return valid_neighbors, len(valid_neighbors)

    def iterate_paper_roll_groups(
        self, data: list[str] | list[list[str]], debug=False
    ) -> int:
        num_accessible = 0
        for line_num, line in enumerate(data):
            for index, char in enumerate(line):
                if char == "@":
                    _, num_neighbors = self.get_neighbors(index, line_num, data)
                    if num_neighbors < 4:
                        if debug:
                            print(
                                f"Cell at ({index}, {line_num}) has {num_neighbors} neighbors"
                            )
                        data[line_num][index] = "x"  # Mark as processed
                        num_accessible += 1
        return num_accessible

    def part1(self, data: list[str], debug=False) -> int:
        num_accessible_paper_rolls = 0
        for line_num, line in enumerate(data):
            for index, char in enumerate(line):
                if char == "@":
                    _, num_neighbors = self.get_neighbors(index, line_num, data)
                    if num_neighbors < 4:
                        if debug:
                            print(
                                f"Cell at ({index}, {line_num}) has {num_neighbors} neighbors"
                            )
                        num_accessible_paper_rolls += 1
        return num_accessible_paper_rolls

    def part2(self, data: list[str]) -> int:
        data = [list(line) for line in data]
        number_of_rolls = 0
        while True:
            result = self.iterate_paper_roll_groups(data, False)
            if result == 0:
                break
            number_of_rolls += result
        return number_of_rolls


if __name__ == "__main__":
    Day4().run()
