# 2025

## Setup

```bash
uv sync
```

## Create a new day

```bash
./create_day.sh <day_number>
```

This creates a new day directory with `task.py`, `input-1.txt`, and `input-2.txt`.

## Run

Run a specific day:

```bash
cd <day> && python3 task.py
```

Or use main:

```bash
python3 main.py           # Run all days
python3 main.py <day>     # Run a specific day
```

## Format & Lint

```bash
uv run ruff format .
uv run ruff check --fix .
```
