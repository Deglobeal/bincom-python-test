"""Question 3: Calculate the median frequency of recorded color labels."""

from questions.dress_data import get_color_frequencies


def calculate_median_frequency() -> float:
    """Return the median of the recorded color-label frequencies."""
    frequencies = sorted(get_color_frequencies().values())

    if not frequencies:
        raise ValueError("Cannot calculate the median of an empty dataset.")

    middle = len(frequencies) // 2

    if len(frequencies) % 2 == 0:
        return (frequencies[middle - 1] + frequencies[middle]) / 2

    return float(frequencies[middle])


def main() -> None:
    """Display the Question 3 result."""
    frequencies = sorted(get_color_frequencies().values())
    median = calculate_median_frequency()

    print("\nQUESTION 3: MEDIAN FREQUENCY")
    print(f"Sorted frequencies: {frequencies}")
    print(f"Median frequency: {median:.2f}")


if __name__ == "__main__":
    main()
