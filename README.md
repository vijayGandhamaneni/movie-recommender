# 🎬 Movie Recommendation System

## 📌 Overview
This project is a content-based movie recommendation system that suggests similar movies based on user input. It uses NLP techniques and similarity measures to provide recommendations.

---

## 🎯 Problem Statement

Users often struggle to discover similar movies based on content. This system solves it using NLP-based similarity instead of manual search.

---

## 🚀 Features
- Data preprocessing and feature engineering
- TF-IDF vectorization for text representation
- Cosine similarity for recommendation
- FastAPI deployment for real-time predictions
- Interactive API documentation using Swagger UI

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Uvicorn

---

## 📂 Project Structure

movie-recommender/
├── data/
├── src/
├── app/
├── notebooks/
├── requirements.txt
├── README.md

---

## 🏗️ Architecture

User → FastAPI → TF-IDF Vectorization → Cosine Similarity → Recommendations

---

## ⚙️ How It Works
1. Clean and preprocess movie data  
2. Convert text data into vectors using TF-IDF  
3. Compute similarity using cosine similarity  
4. Recommend top similar movies  

---

## ▶️ Run the Project

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Run API

uvicorn app.main:app --reload

### Step 3: Open in browser
- http://127.0.0.1:8000  
- http://127.0.0.1:8000/docs  

---

## 📊 Example API

GET /recommend?movie=Avatar

---

## 📸 Sample Output

**Request:**
GET /recommend?movie=Avatar

**Response:**
[
  "Apollo 18",
  "Beowulf",
  "The Helix... Loaded",
  "The American",
  "The Adventures of Pluto Nash"
]

---

## 🧠 Key Learnings

- Built an end-to-end ML pipeline
- Performed feature engineering using TF-IDF
- Implemented cosine similarity for recommendations
- Deployed ML system using FastAPI

---

## ⚠️ Limitations

- Recommendations depend only on textual features
- No user personalization
- Accuracy can be improved with more features

---

## 💡 Future Scope
- Add more features (cast, director, keywords)
- Improve recommendation accuracy
- Add frontend UI

---

## 📌 Author
Vijay Kiran Chowdary Gandhamaneni