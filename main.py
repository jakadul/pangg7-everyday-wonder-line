"""Entry for make.fun bounty u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.

Writes one text (1-200 code points) to /output/entry.txt. No network, deterministic.
"""
import os

TEXT = (
    "The kettle clicks and the room holds its breath one second, as if the house had been waiting all morning to be asked something."
)


def write_entry(text, limit):
    n = len(text)
    assert text.strip(), "text is only white space"
    assert 1 <= n <= limit, f"length {n} outside 1..{limit}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return n


def main():
    n = write_entry(TEXT, 200)
    print(f"wrote /output/entry.txt: {n} code points")


if __name__ == "__main__":
    main()
