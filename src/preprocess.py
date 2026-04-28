import pandas as pd
import ast

# Load dataset
df = pd.read_csv('data/movies_raw.csv')

# Select required columns
df = df[['title', 'overview', 'genres']]

# Remove missing values
df.dropna(inplace=True)

# Convert genres from string to clean text
def extract_genres(text):
    genres = []
    for item in ast.literal_eval(text):
        genres.append(item['name'])
    return " ".join(genres)

df['genres'] = df['genres'].apply(extract_genres)

# Combine features
df['tags'] = df['overview'] + " " + df['genres']

# Final dataset
df = df[['title', 'tags']]

# Save cleaned data
df.to_csv('data/movies_clean.csv', index=False)

print("✅ Preprocessing completed. Clean data saved.")