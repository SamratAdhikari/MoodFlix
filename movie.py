import pickle
import streamlit as st
import requests
import pandas as pd

# Function to get the poster of the movie using the IMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_poster_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_poster_path

# Function for recommending movies
def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie_names = []
    recommend_movie_posters = []

    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie_posters.append(fetch_poster(movie_id))
        recommend_movie_names.append(movies.iloc[i[0]].title)

    return recommend_movie_names, recommend_movie_posters

# Main function to handle the MoviePal recommendation logic
def movie_recommendation():
    # Load the movie data and similarity model
    with open('./models/movies_list.pkl', 'rb') as f:
        movies = pd.read_pickle(f)

    with open('./models/movie_similarity.pkl', 'rb') as f:
        similarity = pd.read_pickle(f)

    # Dropdown to select a movie from the list
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Enter The Movie's Name", movie_list)

    # Button to show movie recommendations
    if st.button('Show Recommendations'):
        st.divider()
        
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies, similarity)

        # Columns with horizontal padding
        col1, col2, col3, col4, col5 = st.columns(5)
        _, _, _, _, _ = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)

        # Display image and text of each recommended movie
        for i in range(1, 11):
            with eval(f'col{i}'):
                st.image(recommended_movie_posters[i-1])
                st.write(recommended_movie_names[i-1])

        with _:
            st.write("#")
