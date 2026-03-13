import sqlite3
from typing import List, Tuple

# -------------------------------
# Database configuration
# -------------------------------
DB_FILE = "jasleen_movies.db"  # Personal movie collection database


# -------------------------------
# Table creation
# -------------------------------
def create_movies_table() -> None:
    """Create the 'movies' table to store movie details with duplicate prevention."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT,
                year INTEGER,
                director TEXT,
                UNIQUE(title, year)  -- prevent duplicate entries
            )
        """)


def create_ratings_table() -> None:
    """Create the 'ratings' table to store movie ratings."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                rating REAL,
                FOREIGN KEY(movie_id) REFERENCES movies(id)
            )
        """)


# -------------------------------
# Movie management
# -------------------------------
def add_movie(title: str, genre: str, year: int, director: str) -> bool:
    """
    Add a new movie to the collection.
    
    Automatically prevents duplicates based on title and year.
    
    Args:
        title (str): Movie title
        genre (str): Genre of the movie
        year (int): Release year
        director (str): Director's name
    
    Returns:
        bool: True if movie was added, False if it already exists
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Check if the movie already exists
        cursor.execute(
            "SELECT id FROM movies WHERE title = ? AND year = ?",
            (title, year)
        )
        existing = cursor.fetchone()
        if existing:
            return False  # Movie already exists

        # Insert new movie
        cursor.execute(
            "INSERT INTO movies (title, genre, year, director) VALUES (?, ?, ?, ?)",
            (title, genre, year, director)
        )
        return True


def add_movie_rating(movie_id: int, rating: float) -> None:
    """
    Add a rating for a movie.

    Multiple ratings can exist per movie; displayed rating is always the average.
    
    Args:
        movie_id (int): ID of the movie
        rating (float): Rating value (e.g., 8.5)
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ratings (movie_id, rating) VALUES (?, ?)",
            (movie_id, rating)
        )


# -------------------------------
# Movie retrieval
# -------------------------------
def get_all_movies(sort_by: str = None) -> List[Tuple]:
    """
    Retrieve all movies with their average rating.
    
    Args:
        sort_by (str, optional): Field to sort by ('rating', 'year', 'genre')
    
    Returns:
        List[Tuple]: List of movies with details and average rating
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.id, m.title, m.genre, m.year, m.director,
                   IFNULL(ROUND(AVG(r.rating), 2), 0) as avg_rating
            FROM movies m
            LEFT JOIN ratings r ON m.id = r.movie_id
            GROUP BY m.id
        """)
        movies = cursor.fetchall()

    if sort_by:
        if sort_by == "rating":
            movies.sort(key=lambda x: x[5], reverse=True)
        elif sort_by == "year":
            movies.sort(key=lambda x: x[3])
        elif sort_by == "genre":
            movies.sort(key=lambda x: x[2])

    return movies


# -------------------------------
# Get top-rated movies
# -------------------------------
def get_top_rated(limit: int = 5):
    """
    Return the top-rated movies based on average rating.
    Default limit is 5.
    """
    movies = get_all_movies(sort_by="rating")
    return movies[:limit] if movies else []


def search_movies_by(field: str, keyword: str) -> List[Tuple]:
    """
    Search for movies based on a specific field.

    Args:
        field (str): Column name to search ('title', 'genre', 'director', etc.)
        keyword (str): Search term
    
    Returns:
        List[Tuple]: Matching movies with their average rating
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        query = f"""
            SELECT m.id, m.title, m.genre, m.year, m.director,
                   IFNULL(ROUND(AVG(r.rating), 2), 0) as avg_rating
            FROM movies m
            LEFT JOIN ratings r ON m.id = r.movie_id
            WHERE m.{field} LIKE ?
            GROUP BY m.id
        """
        cursor.execute(query, (f"%{keyword}%",))
        results = cursor.fetchall()

    return results
