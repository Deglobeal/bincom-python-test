"""Generate the first 50 Fibonacci numbers and calculate their sum."""


def fibonacci_sequence(count: int = 50) -> list[int]:
    """Return the first count Fibonacci numbers, starting with 0, 1."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    a, b = 0, 1

    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def sum_first_50_fibonacci() -> int:
    """Return the sum of the first 50 Fibonacci numbers."""
    return sum(fibonacci_sequence(50))


def main() -> None:
    sequence = fibonacci_sequence(50)

    print(f"First 50 Fibonacci numbers: {sequence}")
    print(f"Sum: {sum(sequence)}")


if __name__ == "__main__":
    main()
