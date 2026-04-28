import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load cleaned data
df = pd.read_csv('data/movies_clean.csv')

# Initialize TF-IDF
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')

# Convert text to vectors
vectors = tfidf.fit_transform(df['tags']).toarray()

print("✅ Vectorization completed")
print("Shape of vectors:", vectors.shape)