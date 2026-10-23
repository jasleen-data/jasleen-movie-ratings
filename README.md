#  Jasleen's Movie Ratings App


![Python](https://img.shields.io/badge/Python-3.x-blue)
![Database](https://img.shields.io/badge/Database-SQLite-green)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib-orange)
![Project](https://img.shields.io/badge/Project-CLI%20Application-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


A **Python-based Movie Management and Analytics Application** with an **interactive command-line interface (CLI)** and **data visualization dashboards**.  
This app allows users to **organize, rate, and analyze their movie collection** efficiently while showcasing professional Python coding, database management, and data visualization skills—perfect for portfolios and recruiter attention.



##  Table of Contents

1. [About the Application](#-about-the-application)  
2. [Key Features](#-key-features)  
3. [Folder Structure](#-folder-structure)  
4. [Technology Stack](#-technology-stack)  
5. [Installation & Setup](#-installation--setup)  
6. [Project Workflow](#-project-workflow)   
7. [Why This Application Stands Out](#-why-this-application-stands-out)  
8. [Future Enhancements](#-future-enhancements)  
9. [Author](#-author)  
10. [License](#-license)  



##  About the Application

This is a **fully functional Python application** that lets users:

- Add, view, and search movies.  
- Rate movies and calculate average ratings.  
- Sort movies by rating, year, or genre.  
- Generate **interactive, portfolio-ready charts** for top-rated movies, genre distribution, and rating trends over years.

Even without a GUI, the combination of **CLI input/output** and **interactive dashboards** makes it a complete, professional application.



##  Key Features

1. **Interactive CLI App**
   - Add movies with details: title, genre, release year, and director.  
   - Rate movies and maintain historical ratings.  
   - Search and sort your collection efficiently.  

2. **Automatic Duplicate Prevention**
   - Ensures each movie is unique by title and year.  

3. **Interactive Data Visualization**
   - **Top-Rated Movies**: Horizontal bar chart with star-based ratings.  
   - **Genre Distribution**: Colorful pie chart of movie genres.  
   - **Rating Trends Over Years**: Scatter plot tracking rating evolution.  
   - Hover-over tooltips show director info and movie details.  

4. **Portfolio-Ready Outputs**
   - All charts saved automatically in `charts/` folder.  
   - Perfect for demonstrating **data analysis, Python coding, and visualization skills**.  



##  Folder Structure

jasleen-movie-ratings/
├── main.py
├── database.py
├── utils.py
├── visualize.py
├── jasleen_movies.db
├── charts/
├── top_rated_movies.png
└── genre_distribution.png

 ##  Technology Stack   

      -Programming Language: Python 3.x
      -Database: SQLite (lightweight & portable)
      -Visualization: Matplotlib, mplcursors (interactive tooltips)
      -File Management: OS module for automated chart storage
      -Code Organization: Modular design for maintainability


##  Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/jasleen-data/jasleen-movie-ratings.git
```

### 2. Move into the project folder

```bash
cd jasleen-movie-ratings
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

The project uses SQLite, so the database is created locally when the application runs.
   

 ##  Project Workflow

   1. Database Initialization
      -Creates tables for movies and ratings automatically.
      -Adds sample movies if the database is empty.

   2. Movie Management
       -Add, view, search, and sort movies via CLI.
       -Duplicate prevention ensures clean data.

   3. Rating System
       -Rate any movie (0–10 scale).
       -Average ratings are updated immediately.

   4. Dashboard Visualization
       -Generate top-rated, genre, and trends charts.
       -Hover over bars and scatter points to view movie and director info.



 ##  Why This Project Stands Out

   -App-Like CLI Interface: Functions like a real movie management app.
   -Interactive Analytics: Hover-over tooltips make data exploration intuitive.
   -Portfolio-Ready Outputs: Visualizations highlight technical skills and attention to detail.
   -Professional Structure: Modular, maintainable Python code demonstrating full-stack Python abilities.



 ##  Future Enhancements
   
   -Develop a GUI version using Tkinter or PyQt.
   -Add user authentication for personalized collections.
   -Enable exporting movie data to CSV or Excel.
   -Integrate IMDb or TMDb API for automatic movie details.



 ##  Author

    Jasleen Kaur

    B.Tech Student | Python Developer | Data Analytics Enthusiast

    GitHub:
    https://github.com/jasleen-data

    LinkedIn:
    www.linkedin.com/in/jasleen-kaur-3b180b39a

 ##  License
      This project is open-source under the MIT License.




