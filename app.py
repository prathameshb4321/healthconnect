from flask import Flask, render_template, request
import csv
import os
from utils.symptom_detector import detect_symptoms

app = Flask(__name__)

CSV_FILE = "patients.csv"


def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name",
                "Email",
                "Age",
                "Phone",
                "Concern",
                "Detected Symptoms"
            ])

        writer.writerow(data)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    age = request.form["age"]
    phone = request.form["phone"]
    concern = request.form["concern"]

    symptoms, categories = detect_symptoms(concern)

    summary = (
        f"Patient {name} ({age} years old) "
        f"reported: {concern}"
    )

    auto_response = (
        "Thank you for contacting HealthConnect. "
        "Your concern has been successfully recorded. "
        "A healthcare volunteer may review your concern soon."
    )

    save_to_csv([
        name,
        email,
        age,
        phone,
        concern,
        ", ".join(symptoms)
    ])

    return render_template(
        "result.html",
        name=name,
        summary=summary,
        symptoms=symptoms,
        categories=categories,
        auto_response=auto_response
    )


if __name__ == "__main__":
    app.run(debug=True)