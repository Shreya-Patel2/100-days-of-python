from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    CURRENT_YEAR = datetime.now().year
    return render_template("index.html", num=random_number, year=CURRENT_YEAR)


@app.route('/guess/<name>')
def greet(name):

    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = response_gender.json()["gender"]

    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    age = response_age.json()["age"]

    return render_template("index.html", name=str(name).title(), gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
