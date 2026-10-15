"""Question 5: Calculate the probability of selecting a RED entry."""

from questions.dress_data import get_all_colors


def calculate_red_probability() -> float:
    """Return the probability that a randomly selected entry is RED."""
    colors = get_all_colors()

    if not colors:
        raise ValueError("Cannot calculate probability from an empty dataset.")

    red_count = sum(1 for color in colors if color == "RED")

    return red_count / len(colors)


def main() -> None:
    """Display the Question 5 result."""
    colors = get_all_colors()
    red_count = sum(1 for color in colors if color == "RED")
    probability = calculate_red_probability()

    print("\nQUESTION 5: PROBABILITY OF RED")
    print(f"Total entries: {len(colors)}")
    print(f"RED entries: {red_count}")
    print(f"Probability: {red_count}/{len(colors)} = {probability:.4f}")
    print(f"Percentage: {probability:.2%}")


if __name__ == "__main__":
    main()
