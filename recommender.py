import pandas as pd

# Load user ratings
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv("u.data", sep="\t", names=rating_cols)

# Load movie titles
movie_cols = ['movie_id', 'title'] + [f'col_{i}' for i in range(22)]
movies = pd.read_csv("u.item", sep="|", encoding="latin-1", names=movie_cols, usecols=[0, 1])

# Merge both datasets
df = pd.merge(ratings, movies, on="movie_id")

print("Data Loaded Successfully")
print(df.head())

# Create the user-movie matrix
movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating')

from sklearn.metrics.pairwise import cosine_similarity

# Fill NaN with 0s so we can compute similarity
movie_ratings_filled = movie_matrix.fillna(0).T  # Transpose so movies are rows

# Compute cosine similarity between all movies
similarity = cosine_similarity(movie_ratings_filled)

# Convert to a DataFrame for easy lookup
similarity_df = pd.DataFrame(similarity, index=movie_ratings_filled.index, columns=movie_ratings_filled.index)

# Function to get top-N similar movies
def get_recommendations(movie_name, top_n=5):
    if movie_name not in similarity_df:
        return ["Movie not found."]
    sim_scores = similarity_df[movie_name].sort_values(ascending=False)
    top_movies = sim_scores.iloc[1:top_n+1].index.tolist()
    return top_movies


