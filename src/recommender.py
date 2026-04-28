import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
df = pd.read_csv('data/movies_clean.csv')

# Create TF-IDF vectors
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(df['tags']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    # find index of movie
    movie_index = df[df['title'] == movie].index[0]

    # get similarity scores
    distances = similarity[movie_index]

    # sort movies based on similarity
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    # print top 5 recommendations
    print(f"\nRecommendations for '{movie}':\n")
    for i in movie_list[1:6]:
        print(df.iloc[i[0]].title)

# Test
recommend("Avatar")