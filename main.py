import os

ENTRY = "I vow to keep your batteries charged, your firmware updated, and your backups safe, in sickness and in low power mode."


def output_path():
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def write_entry(text, path=None):
    path = path or output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    text = ENTRY
    write_entry(text)


if __name__ == "__main__":
    main()
