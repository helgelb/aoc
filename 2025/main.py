import subprocess
import sys
import os


def main():
    print("Advent of Code 2025")

    if len(sys.argv) > 1:
        days = [int(sys.argv[1])]
    else:
        days = range(1, 12)

    for day in days:
        day_dir = f"{day}"
        if not os.path.isdir(day_dir):
            continue
        subprocess.run(["python3", f"{day}/task.py"])


if __name__ == "__main__":
    main()
