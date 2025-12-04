import os


class Task:
    def __init__(
        self, starting_position=50, target_position=0, max_position=100, debug=False
    ):
        self.starting_position = starting_position
        self.target_position = target_position
        self.max_position = max_position
        self.number_of_hits = 0
        self.position = starting_position % max_position
        self.debug = debug

    def _read_input(self, filename):
        return (
            open(os.path.join(os.path.dirname(__file__), filename))
            .read()
            .strip()
            .split("\n")
        )

    def _process_lines(self, lines, count_crossing=False):
        self.debug and print(self.position, self.number_of_hits)

        for i, line in enumerate(lines):
            if self.debug and i == 5:
                break

            direction, value = line[0], line[1:]
            value = int(value)
            prev_position = self.position

            if direction == "R":
                self.position += value
            elif direction == "L":
                self.position -= value

            self.position = self.position % self.max_position

            if not count_crossing:
                if self.position == self.target_position:
                    self.number_of_hits += 1
            else:
                loops = value // self.max_position
                remainder = value % self.max_position
                end = (
                    prev_position + remainder
                    if direction == "R"
                    else prev_position - remainder
                ) % self.max_position

                self.number_of_hits += loops
                if direction == "R":
                    if end <= prev_position and (
                        self.target_position > prev_position
                        or self.target_position <= end
                    ):
                        self.number_of_hits += 1
                    elif prev_position < self.target_position <= end:
                        self.number_of_hits += 1
                else:
                    if end >= prev_position and (
                        self.target_position < prev_position
                        or self.target_position >= end
                    ):
                        self.number_of_hits += 1
                    elif end <= self.target_position < prev_position:
                        self.number_of_hits += 1

            self.debug and print(direction, value, self.position, self.number_of_hits)

        return self.number_of_hits

    def run(self, filename, count_crossing=False):
        lines = self._read_input(filename)
        return self._process_lines(lines, count_crossing)


if __name__ == "__main__":
    task1 = Task()
    task2 = Task()
    print("Part 1: " + str(task1.run("input.txt")))
    print("Part 2: " + str(task2.run("input.txt", count_crossing=True)))
