"""Question 1: Calculate the mean frequency of recorded color labels."""

from questions.dress_data import get_color_frequencies


def calculate_mean_frequency() -> float:
    """Return the average frequency across unique recorded color labels."""
    frequencies = get_color_frequencies().values()

    if not frequencies:
        raise ValueError("Cannot calculate the mean of an empty dataset.")

    return sum(frequencies) / len(frequencies)


def main() -> None:
    """Display the Question 1 result."""
    frequencies = get_color_frequencies()
    total_entries = sum(frequencies.values())
    mean = calculate_mean_frequency()

    print("\nQUESTION 1: MEAN FREQUENCY")
    print(f"Total entries: {total_entries}")
    print(f"Unique recorded labels: {len(frequencies)}")
    print(f"Mean frequency: {mean:.2f}")


if __name__ == "__main__":
    main()
