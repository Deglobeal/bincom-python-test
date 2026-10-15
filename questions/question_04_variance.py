"""Question 4: Calculate the population variance of color frequencies."""

from questions.dress_data import get_color_frequencies


def calculate_population_variance() -> float:
    """Return the population variance of recorded color-label frequencies."""
    frequencies = list(get_color_frequencies().values())

    if not frequencies:
        raise ValueError("Cannot calculate variance of an empty dataset.")

    mean = sum(frequencies) / len(frequencies)
    squared_differences = [(frequency - mean) ** 2 for frequency in frequencies]

    return sum(squared_differences) / len(frequencies)


def main() -> None:
    """Display the Question 4 result."""
    frequencies = sorted(get_color_frequencies().values())
    variance = calculate_population_variance()

    print("\nQUESTION 4: POPULATION VARIANCE")
    print(f"Sorted frequencies: {frequencies}")
    print(f"Population variance: {variance:.4f}")


if __name__ == "__main__":
    main()
