import sqlite3
import matplotlib.pyplot as plt
from typing import List, Tuple
import mplcursors  # For interactive tooltips
import os

DB_FILE = "jasleen_movies.db"
OUTPUT_DIR = "charts"  # Folder to save portfolio images


# -------------------------------
# Convert numeric rating to stars
# -------------------------------
def rating_to_stars(rating: float) -> str:
    max_stars = 5
    scaled = rating / 2
    full_stars = int(scaled)
    half_star = (scaled - full_stars) >= 0.5
    stars = "★" * full_stars
    if half_star:
        stars += "½"
    stars = stars.ljust(max_stars, "☆")
    return stars


# -------------------------------
# Fetch movies from database
# -------------------------------
def fetch_movies() -> List[Tuple]:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.title, m.genre, m.year, IFNULL(ROUND(AVG(r.rating),2),0) as avg_rating, m.director
        FROM movies m
        LEFT JOIN ratings r ON m.id = r.movie_id
        GROUP BY m.id
    """)
    movies = cursor.fetchall()
    conn.close()
    return movies


# -------------------------------
# Ensure output directory exists
# -------------------------------
def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


# -------------------------------
# Top-rated movies chart
# -------------------------------
def plot_top_rated_movies(movies: List[Tuple], top_n: int = 5) -> None:
    top_movies = sorted([m for m in movies if m[3] > 0], key=lambda x: x[3], reverse=True)[:top_n]
    if not top_movies:
        print("⚠ No rated movies found.")
        return

    titles = [m[0] for m in top_movies][::-1]
    ratings = [m[3] for m in top_movies][::-1]
    stars = [rating_to_stars(r) for r in ratings][::-1]
    directors = [m[4] for m in top_movies][::-1]

    plt.figure(figsize=(10, 5))
    bars = plt.barh(titles, ratings, color='skyblue', edgecolor='gray')
    plt.xlim(0, 10)
    plt.xlabel("Average Rating (0-10)")
    plt.title(f"🎬 Top {len(titles)} Rated Movies", fontsize=14, pad=15)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    for bar, rating, star in zip(bars, ratings, stars):
        plt.text(rating + 0.1, bar.get_y() + bar.get_height()/2, f"{rating:.1f} {star}", va='center', fontsize=10)

    # Add interactive tooltips
    cursor = mplcursors.cursor(bars, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        idx = sel.target.index
        sel.annotation.set(text=f"Director: {directors[idx]}", fontsize=10, alpha=0.8)

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_rated_movies.png")
    plt.show()


# -------------------------------
# Genre distribution pie chart
# -------------------------------
def plot_genre_distribution(movies: List[Tuple]) -> None:
    genre_counts = {}
    genre_colors = {}
    color_map = plt.cm.tab20.colors
    color_idx = 0

    for _, genre, _, _, _ in movies:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
        if genre not in genre_colors:
            genre_colors[genre] = color_map[color_idx % len(color_map)]
            color_idx += 1

    if not genre_counts:
        print("⚠ No genres found.")
        return

    plt.figure(figsize=(6,6))
    plt.pie(genre_counts.values(), labels=genre_counts.keys(),
            autopct='%1.1f%%', startangle=140, colors=[genre_colors[g] for g in genre_counts.keys()])
    plt.title("🎨 Movie Genre Distribution", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/genre_distribution.png")
    plt.show()


# -------------------------------
# Rating trends over years
# -------------------------------
def plot_rating_trends(movies: List[Tuple]) -> None:
    rated_movies = [m for m in movies if m[3] > 0]
    if not rated_movies:
        print("⚠ No rated movies to show trends.")
        return

    years = [m[2] for m in rated_movies]
    ratings = [m[3] for m in rated_movies]
    titles = [m[0] for m in rated_movies]

    plt.figure(figsize=(10,5))
    scatter = plt.scatter(years, ratings, color='lightgreen', edgecolor='black', s=100)
    plt.plot(years, ratings, linestyle='--', alpha=0.5, color='green')
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.title("📈 Rating Trends Over Years", fontsize=14)
    plt.ylim(0, 10)
    plt.grid(linestyle='--', alpha=0.5)

    # Interactive tooltips
    cursor = mplcursors.cursor(scatter, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        idx = sel.target.index
        sel.annotation.set(text=f"{titles[idx]} ({ratings[idx]:.1f})", fontsize=10, alpha=0.8)

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/rating_trends.png")
    plt.show()


# -------------------------------
# Full Dashboard
# -------------------------------
def movie_dashboard():
    ensure_output_dir()
    movies = fetch_movies()
    if not movies:
        print("⚠ No movies found in the database.")
        return

    plot_top_rated_movies(movies)
    plot_genre_distribution(movies)
    plot_rating_trends(movies)
    print(f"✅ Charts saved in '{OUTPUT_DIR}' folder for portfolio showcase.")


# -------------------------------
# Run dashboard
# -------------------------------
if __name__ == "__main__":
    movie_dashboard()
