"""Entry for make.fun: Ridiculous at First Glance, Real by the Second.

A single sentence (192 characters, one sentence, ending in a period)
pitching a startup idea so strange it sounds like a joke, yet specific
enough that a reader can see the customers and the money.
"""

LINE = (
    "We install vending machines in laundromats that sell single socks, "
    "because every lost sock is a customer already standing at the machine, "
    "and a sock costing us 40 cents sells for four dollars."
)


def main() -> None:
    # The brief demands exactly one sentence of at most 200 characters.
    assert len(LINE) <= 200, f"pitch is {len(LINE)} chars, over the 200 limit"
    assert LINE.count(".") == 1 and LINE.endswith("."), "pitch must be one sentence"
    print(LINE)


if __name__ == "__main__":
    main()
