import os
from flask import Flask, render_template, request

app = Flask(__name__)

reviews = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        code = request.form.get("code")
        issue = request.form.get("issue")
        severity = request.form.get("severity")
        fix = request.form.get("fix")

        reviews.append({
            "code": code,
            "issue": issue,
            "severity": severity,
            "fix": fix
        })

    return render_template("index.html", reviews=reviews)

if __name__ == "__main__":
    app.run(debug=True)