import streamlit as st
import pandas as pd
from recommender import similarity_df, get_recommendations

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Movie Recommender System")
st.markdown("Find movies similar to your favorite ones using collaborative filtering! 🎥✨")

# Dropdown for movie selection
movie_list = sorted(similarity_df.columns)
selected_movie = st.selectbox("Select a movie:", movie_list)

# Button to get recommendations
if st.button("Recommend 🎯"):
    recommendations = get_recommendations(selected_movie)
    st.subheader("You might also like:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
