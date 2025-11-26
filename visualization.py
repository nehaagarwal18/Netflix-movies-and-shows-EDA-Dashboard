import seaborn as sns
import matplotlib.pyplot as plt

def plot_movies_vs_tv_shows(df):
    plt.figure(figsize=(6,5))
    sns.countplot(data=df, x='type', palette='Set2')
    plt.title('Count of Movies abd TV Shows on Netflix')
    return plt

def top_10_most_content_countries(df):
    top_countries = df['country'].value_counts().head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
    plt.title("Top 10 countries producing netflix's most content")
    plt.xlabel('Number of titles')
    return plt

def top_10_genres(df):
    genres = df['genre'].value_counts().head(10)
    plt.figure(figsize=(7,5))
    sns.barplot(x=genres.values, y=genres.index, palette='viridis')
    plt.title(f"Top 10 Genres on Netflix")
    plt.xlabel("Count")
    plt.ylabel("Genre")
    plt.tight_layout()
    return plt

def movie_duration_distribution(df):
    movies = df[df['type'] == 'Movie']
    movies['duration'] = movies['duration'].str.replace(' min', '').astype(float)
    plt.figure(figsize=(8,5))
    sns.histplot(movies['duration'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Movie Duration')
    plt.xlabel('Duration (minutes)')
    return plt

def most_freq_director(df):
    top_directors = df['director'].value_counts().head(10)
    sns.barplot(x=top_directors.values, y=top_directors.index, palette='viridis')
    plt.title('Top 10 Directors on Netflix')
    plt.tight_layout()
    return plt

def content_released_over_time(df):
    plt.figure(figsize=(12,5))
    df['release_year'].value_counts().sort_index().plot(kind='line', color='blue')
    plt.title('Content Released by Year')
    plt.xlabel('Release Year')
    plt.ylabel('Number of titles')
    return plt