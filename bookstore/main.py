from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os
# create new database
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "new-books-collection.db"))
print(f"Database path: {db_path}")

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    if not db.session.query(Book).filter_by(title="Harry Potter").first():
        new_book = Book(title="Harry Potter 3", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', all_books=all_books)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_title = request.form["title"]
        book_author = request.form["author"]
        book_rating = float(request.form["rating"])
        if not db.session.query(Book).filter_by(title=book_title).first():
            new_book = Book(title=book_title, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
