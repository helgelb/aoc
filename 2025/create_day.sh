#!/bin/bash

# Script to create a new AOC day directory with template files

if [ -z "$1" ]; then
    echo "Usage: ./create_day.sh <day_number>"
    echo "Example: ./create_day.sh 1"
    exit 1
fi

DAY=$1
DAY_DIR="./$DAY"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if day directory already exists
if [ -d "$DAY_DIR" ]; then
    echo "Error: Directory $DAY_DIR already exists"
    exit 1
fi

# Check if TEMPLATE.py exists
if [ ! -f "$SCRIPT_DIR/TEMPLATE.py" ]; then
    echo "Error: TEMPLATE.py not found in $SCRIPT_DIR"
    exit 1
fi

# Create directory
mkdir -p "$DAY_DIR"
echo "Created directory: $DAY_DIR"

# Create empty input file
touch "$DAY_DIR/input.txt"
echo "Created input file"

# Copy and modify template, removing comments and empty lines
sed "s/DayX/Day$DAY/g; s/X/$DAY/g; /^[[:space:]]*#/d; /^[[:space:]]*$/d" "$SCRIPT_DIR/TEMPLATE.py" > "$DAY_DIR/task.py"
echo "Created task.py from template"

# Format with ruff
uv run ruff format "$DAY_DIR/task.py" > /dev/null 2>&1
echo "Formatted with ruff"

echo ""
echo "Day $DAY is ready! Run it with:"
echo "  cd $DAY_DIR && python3 task.py"
