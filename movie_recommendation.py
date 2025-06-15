import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Extended Movie Data
# -------------------------------
data = {
    'title': [
        'The Matrix', 'John Wick', 'Inception', 'The Dark Knight', 'Interstellar',
        'Avengers: Endgame', 'Iron Man', 'Tenet', 'The Prestige', 'Batman Begins'
    ],
    'description': [
        'A hacker discovers reality is a simulation and fights evil machines.',
        'A former assassin comes out of retirement to seek revenge.',
        'A thief steals information by infiltrating dreams.',
        'A vigilante fights crime in Gotham City.',
        'Astronauts travel through a wormhole in search of a new home for humanity.',
        'Superheroes assemble to undo the damage caused by Thanos.',
        'A billionaire builds a high-tech suit to fight crime.',
        'A secret agent manipulates time to prevent World War III.',
        'Two magicians engage in a dangerous rivalry.',
        'A man becomes Batman to fight crime and injustice.'
    ]
}
df = pd.DataFrame(data)

# -------------------------------
# TF-IDF + Cosine Similarity
# -------------------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend_movie(title):
    if title not in df['title'].values:
        return []

    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # top 3 excluding the selected one
    recommended_titles = [df['title'].iloc[i[0]] for i in sim_scores]
    return recommended_titles

# -------------------------------
# GUI with Tkinter
# -------------------------------
def get_recommendations():
    movie = entry.get().strip()
    if not movie:
        result_label.config(text="")  # Clear when search is empty
        return

    recommendations = recommend_movie(movie)
    if not recommendations:
        result_label.config(text="❌ Movie not found.\nTry typing exactly as shown.")
    else:
        result = "\n".join(f"✔️ {rec}" for rec in recommendations)
        result_label.config(text=f"Recommended Movies:\n{result}")

# -------------------------------
# Clear result when typing
# -------------------------------
def on_entry_change(event):
    if not entry.get().strip():
        result_label.config(text="")

# -------------------------------
# GUI Layout
# -------------------------------
root = tk.Tk()
root.title("🎬 Movie Recommendation System")
root.geometry("420x330")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Enter a Movie Title:", font=('Arial', 13), bg="#f0f0f0")
title_label.pack(pady=12)

entry = tk.Entry(root, width=45, font=('Arial', 11))
entry.pack(pady=5)
entry.bind("<KeyRelease>", on_entry_change)

button = tk.Button(root, text="Get Recommendations", font=('Arial', 11, 'bold'),
                   command=get_recommendations, bg="#4caf50", fg="white")
button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 11), bg="#f0f0f0", justify='left')
result_label.pack(pady=20)

root.mainloop()
