import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv("Books.csv", low_memory=False)
ratings = pd.read_csv("Ratings.csv")

rating_col = "Book-Rating" if "Book-Rating" in ratings.columns else "Book_Rating"
ratings = ratings[ratings[rating_col] > 0]

df = ratings.merge(books, on="ISBN")

df = df.groupby("User-ID").filter(lambda x: len(x) >= 5)
df = df.groupby("Book-Title").filter(lambda x: len(x) >= 5)

pivot = df.pivot_table(
    index="Book-Title",
    columns="User-ID",
    values=rating_col
).fillna(0)

similarity = cosine_similarity(pivot)
similarity_df = pd.DataFrame(similarity, index=pivot.index, columns=pivot.index)

def recommend(book_name, mood=None, n=8):
    matches = [b for b in similarity_df.index if book_name.lower() in b.lower()]
    if not matches:
        return []

    book = matches[0]
    recs = similarity_df[book].sort_values(ascending=False)[1:n+1]

    result = []
    for b in recs.index:
        info = books[books["Book-Title"] == b].iloc[0]
        result.append({
            "title": b,
            "author": info["Book-Author"],
            "year": info["Year-Of-Publication"],
            "publisher": info["Publisher"]
        })
    return result
