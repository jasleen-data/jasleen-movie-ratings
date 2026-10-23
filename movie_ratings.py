from database import (
    create_movies_table,
    create_ratings_table,
    add_movie,
    add_movie_rating,
    get_all_movies,
    search_movies_by,
    get_top_rated
)
from utils import display_movies, get_movie_id, get_rating
5
# -------------------------------------------------------
# Add sample movies to the collection if database is empty
# -------------------------------------------------------
def add_sample_movies():
    sample_movies = [
        ("Inception", "Sci-Fi", 2010, "Christopher Nolan"),
        ("Interstellar", "Sci-Fi", 2014, "Christopher Nolan"),
        ("The Matrix", "Action", 1999, "The Wachowskis"),
        ("Titanic", "Romance", 1997, "James Cameron"),
        ("Avatar", "Fantasy", 2009, "James Cameron")
    ]

    if not get_all_movies():
        for movie in sample_movies:
            add_movie(*movie)
        print("✨ Added a few sample movies to get you started!")


# -------------------------------------------------------
# Display main menu
# -------------------------------------------------------
def main_menu() -> str:
    print("\n=== 🎬 Jasleen's Movie Ratings App ===")
    print("1. Add a Movie")
    print("2. Rate a Movie")
    print("3. View All Movies")
    print("4. Search Movies")
    print("5. Top-Rated Movies")
    print("6. Exit")
    return input("Enter your choice (1-6): ").strip()


# -------------------------------------------------------
# Flow: Add a new movie
# -------------------------------------------------------
def add_movie_flow():
    print("\n--- Add a New Movie ---")
    title = input("Title: ").strip()
    genre = input("Genre: ").strip()

    try:
        year = int(input("Release Year: ").strip())
    except ValueError:
        print("⚠ Invalid year. Setting it to 0.")
        year = 0

    director = input("Director: ").strip()
    added = add_movie(title, genre, year, director)
    if added:
        print(f"✅ Movie '{title}' has been added to your collection!")
    else:
        print(f"⚠ Movie '{title}' ({year}) already exists.")


# -------------------------------------------------------
# Flow: Rate an existing movie
# -------------------------------------------------------
def rate_movie_flow():
    print("\n--- Rate a Movie ---")
    movies = get_all_movies()
    if not movies:
        print("⚠ No movies available to rate yet.")
        return

    display_movies(movies)
    movie_id = get_movie_id()
    if not movie_id:
        print("❌ Invalid movie ID.")
        return

    rating = get_rating()
    if rating is None:
        print("⚠ Invalid rating entered.")
        return

    add_movie_rating(movie_id, rating)
    print("⭐ Rating added successfully! Average rating updated.")

    # Display updated rating immediately
    updated_movie = [m for m in get_all_movies() if m[0] == movie_id]
    if updated_movie:
        print("\n📊 Updated Movie Rating:")
        display_movies(updated_movie)


# -------------------------------------------------------
# Flow: View movies
# -------------------------------------------------------
def view_movies_flow():
    print("\n--- View Movies ---")
    print("Sort by:")
    print("1. Rating")
    print("2. Year")
    print("3. Genre")
    print("4. No Sorting")

    choice = input("Enter choice: ").strip()
    sort_by = {"1": "rating", "2": "year", "3": "genre"}.get(choice)
    movies = get_all_movies(sort_by)
    if movies:
        display_movies(movies)
    else:
        print("⚠ No movies found in your collection.")


# -------------------------------------------------------
# Flow: Search movies
# -------------------------------------------------------
def search_movies_flow():
    print("\n--- Search Movies ---")
    print("1. Title")
    print("2. Genre")
    print("3. Director")

    choice = input("Enter choice: ").strip()
    field = {"1": "title", "2": "genre", "3": "director"}.get(choice)
    if not field:
        print("❌ Invalid choice.")
        return

    keyword = input(f"Enter {field} keyword: ").strip()
    results = search_movies_by(field, keyword)
    if results:
        display_movies(results)
    else:
        print(f"⚠ No movies found for '{keyword}'.")


# -------------------------------------------------------
# Flow: Show top-rated movies
# -------------------------------------------------------
def top_rated_flow():
    print("\n--- Top-Rated Movies ---")
    movies = get_top_rated()
    if movies:
        display_movies(movies)
    else:
        print("⚠ No ratings available yet.")


# -------------------------------------------------------
# Main program loop
# -------------------------------------------------------
if __name__ == "__main__":
    # Prepare the database
    create_movies_table()
    create_ratings_table()
    add_sample_movies()

    while True:
        choice = main_menu()
        if choice == "1":
            add_movie_flow()
        elif choice == "2":
            rate_movie_flow()
        elif choice == "3":
            view_movies_flow()
        elif choice == "4":
            search_movies_flow()
        elif choice == "5":
            top_rated_flow()
        elif choice == "6":
            print("👋 Goodbye! Thanks for using Jasleen's Movie Ratings App.")
            break
        else:
            print("❌ Invalid option. Please select between 1–6.")
