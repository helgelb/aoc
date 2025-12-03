import os


def read_file(file_path: str, strip=True, split_char="\n") -> str | list[str]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r") as file:
        content = file.read()
        if strip:
            content = content.strip()
        if split_char:
            content = content.split(split_char)
        return content
