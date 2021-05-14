from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


def gender_of_name(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()["gender"]


def age_of_name(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()["age"]


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<name>')
def guess_by_name(name):
    gender = gender_of_name(name)
    age = age_of_name(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
