"""Server for movie ratings app."""

from flask import Flask
from datetime import datetime


app = Flask(__name__)
class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(30))

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User: user = {self.user_id} email = {self.email}>'

class Movie(db.Model):
    """A movie."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'<Movie movie id = {self.movie_id} title = {self.title}>'

class Rating(db.Model):
    """Rating a movie"""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')


    def __repr__(self):
        return f'<Rating rating_id = {self.rating_id} score = {self.score}>'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
