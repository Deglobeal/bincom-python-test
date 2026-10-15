"""Bonus: recursively search for a number in a list."""


def recursive_search(numbers: list[float], target: float, index: int = 0) -> int:
    """Return the first matching index, or -1 if not found."""
    if index >= len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return recursive_search(numbers, target, index + 1)


def main() -> None:
    numbers = [
        float(value.strip())
        for value in input("Enter numbers separated by commas: ").split(",")
    ]
    target = float(input("Enter the number to search for: "))

    result = recursive_search(numbers, target)

    if result == -1:
        print(f"{target:g} was not found.")
    else:
        print(f"{target:g} was found at index {result}.")


if __name__ == "__main__":
    main()
