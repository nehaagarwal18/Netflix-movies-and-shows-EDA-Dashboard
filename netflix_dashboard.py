import streamlit as st
import pandas as pd
from visualization import (
    plot_movies_vs_tv_shows,
    top_10_most_content_countries,
    top_10_genres,
    movie_duration_distribution,
    most_freq_director,
    content_released_over_time
)

### Load Data
st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.title("Netflix Movies and TV Shows - Dashboard")

df = pd.read_csv("netflix_titles.csv")
df = df.loc[:, ~df.columns.duplicated()]
df = df.reset_index(drop=True)

df['date_added'] = pd.to_datetime(df['date_added'], errors="coerce")
df['year_added'] = df['date_added'].dt.year
df['genre'] = df['listed_in'].str.split(", ")
df = df.explode('genre').reset_index(drop=True)

### Create Filters
st.sidebar.header("Filters")
selected_types = st.sidebar.multiselect("Select Type", df['type'].unique(), df['type'].unique())

genre_options = df['genre'].dropna().unique().tolist()
selected_genres = st.sidebar.multiselect("Select Genres", options=genre_options, default=genre_options[:10])

country_options = df['country'].dropna().unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", options=country_options)

min_year = int(df['release_year'].min())
max_year = int(df['release_year'].max())
year_range = st.sidebar.slider(
    "Release Year range", 
    min_value=min_year,
    max_value=max_year,
    value=(2000, max_year)
)

### Filter Data
filtered_df = df.copy()

if selected_types:
    filtered_df = filtered_df[filtered_df['type'].isin(selected_types)]

if selected_genres:
    filtered_df = filtered_df[filtered_df['genre'].isin(selected_genres)]

if selected_countries:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]

filtered_df = filtered_df[(filtered_df['release_year'] >= year_range[0]) & (filtered_df['release_year'] <= year_range[1])]

### Visualizations
st.subheader("What to watch? (Filtered Recommendations)")
st.dataframe(filtered_df[['title', 'type', 'genre', 'country', 'release_year', 'rating']].drop_duplicates().sort_values(by='release_year', ascending=False))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Movies vs TV Shows")
    fig1 = plot_movies_vs_tv_shows(df)
    st.pyplot(fig1)

    st.subheader("Top 10 Genres on Netflix")
    fig3 =  top_10_genres(df)
    st.pyplot(fig3)

    st.subheader("Content Released Over Years")
    fig5 = content_released_over_time(df)
    st.pyplot(fig5)


with col2:
    st.subheader("Top 10 Most Content Producing Countries")
    fig2 = top_10_most_content_countries(df)
    st.pyplot(fig2)

    st.subheader("Top 10 Most Frequent Directors")
    fig4 = most_freq_director(df)
    st.pyplot(fig4)

    st.subheader("Movie Duration Distribution")
    fig6 = movie_duration_distribution(df)
    st.pyplot(fig6)




