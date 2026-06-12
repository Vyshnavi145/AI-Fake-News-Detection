from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    if request.method == "POST":

        news = request.form["news"]

        vector = vectorizer.transform([news])

        result = model.predict(vector)

        if result[0] == 0:
            prediction = "Fake News"
        else:
            prediction = "Real News"

    return render_template(
        "index.html",
        prediction=prediction
    )

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))