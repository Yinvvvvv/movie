# routes.py

from movie import app, db
from movie.models import Movies, Actors, Movie_Actor_Relationship
from movie.forms import *
from flask import render_template, url_for, request, redirect, flash, abort
#from flask_login import current_user, logout_user, login_user, login_required
from datetime import datetime

@app.route('/')
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        new_movie = Movies(
            movie_name=form.movie_name.data,
            release_date=form.release_date.data,
            country_movie=form.country_movie.data,
            type=form.movie_type.data,
            year=form.year.data,
            box=form.box.data
        )
        db.session.add(new_movie)
        db.session.commit()
        
    #movies = Movies.query.all()  # Retrieve all movies from the database
    return render_template('add_movie.html', form=form)
