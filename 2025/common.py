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
        self.input_dir = Path(__file__).parent / str(day)
    
    def read_input(self, part: int) -> list[str]:
        """Read input file for a specific part"""
        input_file = self.input_dir / f"input-{part}.txt"
        return read_file(str(input_file), strip=True, split_char="\n")
    
    def run_tests(self):
        """Override this to run tests"""
        raise NotImplementedError
    
    def part1(self, data: list[str]) -> int:
        """Override this for part 1 logic"""
        raise NotImplementedError
    
    def part2(self, data: list[str]) -> int:
        """Override this for part 2 logic"""
        raise NotImplementedError
    
    def run(self):
        """Run both parts"""
        print(f"Day {self.day}")
        
        try:
            self.run_tests()
            print("All tests passed\n")
        except Exception as e:
            print(f"Tests failed: {e}\n")
            return
        
        # Part 1
        data1 = self.read_input(1)
        result1 = self.part1(data1)
        print(f"Part 1: {result1}")
        
        # Part 2
        data2 = self.read_input(2)
        result2 = self.part2(data2)
        print(f"Part 2: {result2}")