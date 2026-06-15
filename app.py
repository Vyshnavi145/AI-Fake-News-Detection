from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key from Render Environment Variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    if request.method == "POST":

        news = request.form["news"]

        response = model.generate_content(
            f"""
            Analyze the following claim or news article.

            Return:
            1. Verdict (True / False / Uncertain)
            2. Explanation
            3. Confidence

            Claim:
            {news}
            """
        )

        prediction = response.text

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))