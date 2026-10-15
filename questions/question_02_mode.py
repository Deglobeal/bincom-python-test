"""Question 2: Find the most frequently recorded color label."""

from questions.dress_data import get_color_frequencies


def calculate_mode() -> tuple[list[str], int]:
    """Return the most frequent color labels and their frequency."""
    frequencies = get_color_frequencies()

    if not frequencies:
        raise ValueError("Cannot calculate the mode of an empty dataset.")

    highest_frequency = max(frequencies.values())
    modes = sorted(
        color
        for color, frequency in frequencies.items()
        if frequency == highest_frequency
    )

    return modes, highest_frequency


def main() -> None:
    """Display the Question 2 result."""
    modes, frequency = calculate_mode()

    print("\nQUESTION 2: MOST-WORN COLOR (MODE)")
    print("Color(s):", ", ".join(modes))
    print("Frequency:", frequency)


if __name__ == "__main__":
    main()
