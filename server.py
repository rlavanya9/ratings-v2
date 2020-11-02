"""Server for movie ratings app."""
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import * # StrictUndefined



app = Flask(__name__)
app.secret_key = "poij;lkrjaf;"
app.jinja_env.undefined = StrictUndefined
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('/homepage.html')

@app.route('/movies')
def movies():
    """View all movies"""

    all_movies = crud.display_movies()
    return render_template('all_movies.html',
                            movies = all_movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Display the details for a single movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html',
                            movie=movie)

@app.route('/users')
def show_users():
    """show a list of all users"""

    all_users = crud.display_users()

    return render_template('all_users.html',
                            users = all_users)


@app.route('/users/<email>')
def show_profile(email):
    """show the profile for the selected user"""

    # user = crud.get_user_by_id(user_id)
    user = crud.get_user_by_id(email)

    return render_template('profile.html',
                            user=user)

@app.route('/new_users', methods=['POST'])
def register_user():
    """Register a new user"""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.check_user(email)
    if user:
        flash("Email already in use -- Cannot create account.")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in")

    return redirect('/')

@app.route('/login')
def login_user():
    """Log a user into the site"""

    email = request.args.get('email')
    password = request.args.get('password')

    if crud.check_user(email):
        is_valid = crud.validate_user(email, password)
        if is_valid:
            flash ("Logged in successfully!")
        else:
            flash("Email and password do not match, please check your login and try again or create an account.")
    else:
        flash("Email is not in our system, Please create a new account.")
    return redirect("/")

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
