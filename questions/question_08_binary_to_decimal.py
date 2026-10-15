"""Generate a random four-digit binary number and convert it to decimal."""

import random


def generate_random_binary_number() -> str:
    """Generate four binary digits, preserving leading zeros."""
    return format(random.randint(0, 15), "04b")


def binary_to_decimal(binary: str) -> int:
    """Convert a binary string to a base-10 integer."""
    if len(binary) != 4 or any(bit not in "01" for bit in binary):
        raise ValueError("Input must contain exactly four binary digits.")

    return int(binary, 2)


def main() -> None:
    binary = generate_random_binary_number()
    decimal = binary_to_decimal(binary)

    print(f"Random binary number: {binary}")
    print(f"Base-10 equivalent: {decimal}")


if __name__ == "__main__":
    main()
