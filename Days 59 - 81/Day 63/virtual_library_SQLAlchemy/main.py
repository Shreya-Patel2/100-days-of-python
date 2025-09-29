from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "###"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
    # return render_template("index.html")
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        BOOK_NAME = request.form["name"]
        BOOK_AUTHOR = request.form["author"]
        BOOK_RATING = request.form["rating"]
        my_dict = {"title": {BOOK_NAME},
                   "author": {BOOK_AUTHOR},
                   "rating": {BOOK_RATING}}
        all_books.append(my_dict)

        with app.app_context():
            book = Book(title=BOOK_NAME, author=BOOK_AUTHOR, rating=BOOK_RATING)
            db.session.add(book)
            db.session.commit()

        return render_template("index.html", books=all_books)

    return render_template("add.html")


# @app.route("/edit/<title>", methods=["GET", "POST"])
# def edit(title):
#     requested_post = None
#     for book in all_books:
#         if book["title"] == title:
#             with app.app_context():
#                 book_to_update = db.session.execute(db.select(Book).where(Book.title == title)).scalar()
#                 book_to_update.rating = request.form["rating"]
#                 db.session.commit()
#     return render_template("index.html", books=all_books)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    book_id = request.args.get('book_id')
    all_books = db.session.query(Book).all()
    return render_template("edit.html", book_id=int(book_id), all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

# book_id = 5
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
