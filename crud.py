"""CRUD operations."""
from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime



def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_id(email):
    """query for the details of a user"""

    # return User.query.get(user_id)
    return User.query.filter_by(email = email).one()
    # return q1


def display_users():
    """Return a list of all users"""

    return User.query.all()

def check_user(email):

    # return User.query.filter_by(email = email).first()
    return User.query.filter(User.email == email).first()

def validate_user(email, password):
    
    user = User.query.filter(User.email == email).first()
    return user.password == password


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def display_movies():
    """return a list of all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """query for the details of a movie"""

    # return Movie.query.filter_by(movie_id = movie_id)
    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """create a movie rating."""
    rating = Rating(user_id=user, movie_id=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)