from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = " https://api.npoint.io/f1e098a52bb6297e97db"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")



@app.route('/<blog_id>')
def get_blog(blog_id):
    blog_url = " https://api.npoint.io/f1e098a52bb6297e97db"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
