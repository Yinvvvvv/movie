# routes.py

from movie import app, db
from movie.models import Movie_Info, Actor_Info, Movie_Actor_Relation, Movie_Box
from movie.forms import *
from flask import render_template, url_for, request, redirect, flash, abort
#from flask_login import current_user, logout_user, login_user, login_required
from datetime import datetime

@app.route('/')


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        # Check if the movie already exists in the database
        existing_movie = Movie_Info.query.filter_by(movie_name=form.movie_name.data).first()

        if existing_movie:
            # Update existing movie if found
            existing_movie.release_date = form.release_date.data
            existing_movie.country = form.country.data
            existing_movie.type = form.type.data
            existing_movie.year = form.year.data
        else:
            # Create a new movie if it doesn't exist
            new_movie = Movie_Info(
                movie_name=form.movie_name.data,
                release_date=form.release_date.data,
                country=form.country.data,
                type=form.type.data,
                year=form.year.data,
            )
            db.session.add(new_movie)

        db.session.commit()
        flash('Movie information updated.')
         # Retrieve all movies to display on the page
        movies = Movie_Info.query.all()
        return render_template('add_movie.html', form=form, movies=movies)

    # On GET request or form validation failure, render the template
    movies = Movie_Info.query.all()
    return render_template('add_movie.html', form=form, movies=movies)

@app.route('/query_movies', methods=['GET', 'POST'])
def query_movies():
    form = MovieSearchForm()
    if request.method == 'POST':
        # Handle form submission to query movies based on user input
        search_term = request.form.get('search_term', '')
        movies = Movie_Info.query.filter(Movie_Info.movie_name.ilike(f'%{search_term}%')).all()
    else:
        # Display all movies by default
        movies = Movie_Info.query.all()

    return render_template('query_movies.html',form=form, movies=movies)