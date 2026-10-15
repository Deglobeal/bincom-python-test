
from collections import Counter

# Original dress-color data from the Bincom HTML table.
# Keep the original entries so that possible spelling errors
# can be reviewed instead of silently corrected.

dress_colors = {
    "MONDAY": """
    GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW,
    ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE,
    BLUE, BLUE, GREEN
    """,

    "TUESDAY": """
    ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK,
    ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE,
    BLUE, BLUE
    """,

    "WEDNESDAY": """
    GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW,
    ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE,
    BLUE, WHITE, WHITE
    """,

    "THURSDAY": """
    BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW,
    ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE,
    BLUE, BLUE, GREEN
    """,

    "FRIDAY": """
    GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE,
    ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE,
    BLUE, BLUE, WHITE
    """
}


def extract_colors(day_data):
    """Convert a comma-separated string into a list of colors."""
    return [
        color.strip().upper()
        for color in day_data.split(",")
        if color.strip()
    ]


# Combine the colors from all five days.
all_colors = []

for day, day_data in dress_colors.items():
    daily_colors = extract_colors(day_data)
    all_colors.extend(daily_colors)

# Count the occurrences of each color.
color_frequencies = Counter(all_colors)

# Question 1: Mean frequency per recorded color label
mean_frequency = len(all_colors) / len(color_frequencies)

print("\nQUESTION 1: MEAN FREQUENCY")
print(f"Total entries: {len(all_colors)}")
print(f"Unique recorded labels: {len(color_frequencies)}")
print(f"Mean frequency: {mean_frequency:.2f}")


# Question 2: Find the most frequently worn color (mode).
highest_frequency = max(color_frequencies.values())

most_worn_colors = [
    color
    for color, frequency in color_frequencies.items()
    if frequency == highest_frequency
]

print("\nQUESTION 2: MOST-WORN COLOR (MODE)")
print("Color(s):", ", ".join(sorted(most_worn_colors)))
print("Frequency:", highest_frequency)


# Question 3: Median frequency per recorded color label
sorted_frequencies = sorted(color_frequencies.values())
number_of_labels = len(sorted_frequencies)

middle = number_of_labels // 2

if number_of_labels % 2 == 0:
    median_frequency = (
        sorted_frequencies[middle - 1] + sorted_frequencies[middle]
    ) / 2
else:
    median_frequency = sorted_frequencies[middle]

print("\nQUESTION 3: MEDIAN FREQUENCY")
print(f"Sorted frequencies: {sorted_frequencies}")
print(f"Median frequency: {median_frequency:.2f}")


# Question 4: Population variance of color frequencies
mean_frequency = sum(sorted_frequencies) / len(sorted_frequencies)

squared_deviations = [
    (frequency - mean_frequency) ** 2
    for frequency in sorted_frequencies
]

variance = sum(squared_deviations) / len(sorted_frequencies)

print("\nQUESTION 4: POPULATION VARIANCE")
print(f"Mean frequency: {mean_frequency:.4f}")
print(f"Variance: {variance:.4f}")

# Question 5: Probability of randomly selecting red
red_count = color_frequencies.get("RED", 0)
total_count = len(all_colors)

red_probability = red_count / total_count if total_count else 0

print("\nQUESTION 5: PROBABILITY OF RED")
print(f"Red entries: {red_count}")
print(f"Total entries: {total_count}")
print(f"Probability: {red_count}/{total_count} = {red_probability:.4f}")
print(f"Percentage: {red_probability:.2%}")


if __name__ == "__main__":
    print("BINCOM DRESS-COLOR FREQUENCY REPORT")
    print("=" * 40)
    print(f"Days analyzed: {len(dress_colors)}")
    print(f"Total entries: {len(all_colors)}")
    print(f"Unique recorded color labels: {len(color_frequencies)}")
    print()

    print("Color frequencies:")
    for color, frequency in sorted(color_frequencies.items()):
        print(f"{color}: {frequency}")
