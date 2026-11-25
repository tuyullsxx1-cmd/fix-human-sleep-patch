import os

NOTE = "Fixed: human sleep now installs in one uninterrupted block. The 3 a.m. existential dread prompt is a known issue and will not be fixed."


def main():
    os.makedirs("/output", exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open("/output/entry.txt", flags, 0o644)
    try:
        os.write(fd, NOTE.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
