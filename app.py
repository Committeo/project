from flask import Flask, render_template, request
from book_recommendation import recommend

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- EXPLORE PAGE ----------------
@app.route("/explore", methods=["GET", "POST"])
def explore():
    recommendations = []

    if request.method == "POST":
        book = request.form["book"]
        mood = request.form["mood"]
        recommendations = recommend(book, mood)

    return render_template(
        "explore.html",
        recommendations=recommendations
    )


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
