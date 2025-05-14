import re
import sys


def hex_to_decimal(c):
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - ord("A") + 10


def hex_pair_to_decimal(pair):
    first = hex_to_decimal(pair[0])
    second = hex_to_decimal(pair[1])
    return (first << 4) + second  # can also use (first * 16) + second


def hex_to_rgb(hex):
    hex_color = hex.lstrip("#")

    # Expand short form (#ABC → #AABBCC)
    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])
    # Expand short form (#ABCD → #AABBCCDD)
    elif len(hex_color) == 4:
        hex_color = "".join([c * 2 for c in hex_color])

    r = hex_pair_to_decimal(hex_color[0:2])
    g = hex_pair_to_decimal(hex_color[2:4])
    b = hex_pair_to_decimal(hex_color[4:6])

    if len(hex_color) == 8:
        a = hex_pair_to_decimal(hex_color[6:8]) / 255
        return f"rgba({r} {g} {b} / {a:.5f})"
    elif len(hex_color) == 6:
        return f"rgb({r} {g} {b})"


for line in sys.stdin:
    modified_line = re.sub(
        r"\#([0-9a-fA-F]+)",
        lambda match: hex_to_rgb(match.group()),
        line,
    )
    sys.stdout.write(modified_line)

# print(hex_to_rgb("#123"))
