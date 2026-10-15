"""Original Bincom dress-color data and reusable counting helpers."""

from collections import Counter


DRESS_COLORS = {
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
    """,
}


def extract_colors(day_data: str) -> list[str]:
    """Parse comma-separated color labels without altering their spelling."""
    return [
        color.strip().upper()
        for color in day_data.split(",")
        if color.strip()
    ]


def get_all_colors() -> list[str]:
    """Return all recorded color labels across the five weekdays."""
    colors = []
    for day_data in DRESS_COLORS.values():
        colors.extend(extract_colors(day_data))
    return colors


def get_color_frequencies() -> Counter[str]:
    """Count each recorded color label."""
    return Counter(get_all_colors())
