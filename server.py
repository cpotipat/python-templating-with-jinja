from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


def gender_of_name(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()


def age_of_name(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    gender = gender_of_name("peter")["gender"]
    age = age_of_name("peter")["age"]
    return render_template("index.html", gender=gender, age=age, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
