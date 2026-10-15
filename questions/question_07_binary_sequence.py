"""Binary-sequence puzzle: mark each 1 that completes three consecutive 1s."""


def transform_binary_sequence(binary: str) -> str:
    """Return 1 where three consecutive input bits end, otherwise 0."""
    if not binary:
        raise ValueError("The binary sequence cannot be empty.")

    if any(bit not in "01" for bit in binary):
        raise ValueError("The sequence must contain only 0s and 1s.")

    output = []

    for index in range(len(binary)):
        if index >= 2 and binary[index - 2:index + 1] == "111":
            output.append("1")
        else:
            output.append("0")

    return "".join(output)


def main() -> None:
    """Display the assessment's example and its transformed output."""
    binary = "0101101011101011011101101000111"
    result = transform_binary_sequence(binary)

    print("\nBINARY-SEQUENCE PUZZLE")
    print(f"Input:  {binary}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
