from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load data
df = pd.read_csv('data/movies_clean.csv')

# Create vectors
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(df['tags']).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    if movie not in df['title'].values:
        return ["Movie not found"]

    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommendations = []
    for i in movie_list[1:6]:
        recommendations.append(df.iloc[i[0]].title)

    return recommendations

# API endpoint
@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}

@app.get("/recommend")
def get_recommendations(movie: str):
    results = recommend(movie)
    return {"movie": movie, "recommendations": results}