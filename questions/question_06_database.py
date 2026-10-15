"""Question 6: Store dress-color frequencies in PostgreSQL."""

import os

import psycopg

from questions.dress_data import get_color_frequencies


def get_database_connection():
    """Connect to PostgreSQL using environment-based configuration."""
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "bincom_python_test"),
        user=os.getenv("DB_USER", os.getenv("USER", "")),
        password=os.getenv("DB_PASSWORD") or None,
    )


def create_table(connection) -> None:
    """Create the color-frequency table if it does not exist."""
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dress_color_frequencies (
                color VARCHAR(50) PRIMARY KEY,
                frequency INTEGER NOT NULL CHECK (frequency >= 0)
            )
            """
        )
    connection.commit()


def save_color_frequencies(connection) -> int:
    """Insert or update all recorded color frequencies.

    Returns the number of color labels processed.
    """
    frequencies = get_color_frequencies()

    with connection.cursor() as cursor:
        cursor.executemany(
            """
            INSERT INTO dress_color_frequencies (color, frequency)
            VALUES (%s, %s)
            ON CONFLICT (color)
            DO UPDATE SET frequency = EXCLUDED.frequency
            """,
            list(frequencies.items()),
        )

    connection.commit()
    return len(frequencies)


def fetch_color_frequencies(connection) -> list[tuple[str, int]]:
    """Return stored color labels and frequencies in alphabetical order."""
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT color, frequency
            FROM dress_color_frequencies
            ORDER BY color
            """
        )
        return cursor.fetchall()


def main() -> None:
    """Create the table, save the frequencies, and display the records."""
    with get_database_connection() as connection:
        create_table(connection)
        saved_count = save_color_frequencies(connection)
        records = fetch_color_frequencies(connection)

    print("\nQUESTION 6: POSTGRESQL COLOR FREQUENCIES")
    print(f"Color labels saved: {saved_count}")
    print("\nColor       Frequency")
    print("--------------------")
    for color, frequency in records:
        print(f"{color:<12}{frequency}")


if __name__ == "__main__":
    main()
