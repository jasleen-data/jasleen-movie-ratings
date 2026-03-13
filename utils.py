from typing import List, Optional, Tuple

# -------------------------------
# Display Movies in a Table
# -------------------------------
def display_movies(movies: List[Tuple]) -> None:
    """
    Display a list of movies in a clean, formatted table.

    Each movie shows its ID, Title, Genre, Year, Director, Average Rating, and Stars.
    Stars are calculated from the average rating.
    """
    if not movies:
        print("⚠ No movies to display.")
        return

    header = f"{'ID':<5} {'Title':<30} {'Genre':<15} {'Year':<6} {'Director':<20} {'Rating':<10} {'Stars'}"
    print(header)
    print("-" * len(header))

    for movie in movies:
        id_, title, genre, year, director, avg_rating = movie
        rating_display = f"{avg_rating:.1f}" if avg_rating else "N/A"
        stars = rating_to_stars(avg_rating) if avg_rating else "N/A"
        print(f"{id_:<5} {title:<30} {genre:<15} {year:<6} {director:<20} {rating_display:<10} {stars}")


# -------------------------------
# Convert numeric rating to stars
# -------------------------------
def rating_to_stars(rating: float) -> str:
    """
    Convert a 0-10 rating into a visual star rating (max 5 stars).

    Full star = ★, Half star = ½, Empty star = ☆

    Example:
        8.6 -> ★★★★★☆ (4.3 stars)
    """
    max_stars = 5
    scaled = rating / 2  # scale 0-10 to 0-5 stars
    full_stars = int(scaled)
    half_star = scaled - full_stars >= 0.5

    stars_str = "★" * full_stars
    if half_star:
        stars_str += "½"

    stars_str = stars_str.ljust(max_stars, "☆")
    return stars_str


# -------------------------------
# Prompt user for movie ID
# -------------------------------
def get_movie_id() -> Optional[int]:
    """
    Prompt the user to enter a movie ID.
    
    Returns:
        int if valid input, else None
    """
    try:
        return int(input("Enter the Movie ID: ").strip())
    except ValueError:
        print("⚠ Invalid input. Please enter a valid number.")
        return None


# -------------------------------
# Prompt user for rating
# -------------------------------
def get_rating() -> Optional[float]:
    """
    Prompt the user to enter a rating between 0.0 and 10.0.

    Returns:
        float if valid, else None
    """
    try:
        rating = float(input("Enter rating (0.0 - 10.0): ").strip())
        if 0 <= rating <= 10:
            return rating
        print("⚠ Rating must be between 0 and 10.")
        return None
    except ValueError:
        print("⚠ Invalid input. Please enter a number between 0 and 10.")
        return None
