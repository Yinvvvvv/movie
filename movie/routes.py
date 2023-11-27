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
        new_movie = Movie_Info(
            movie_name=form.movie_name.data,
            release_date=form.release_date.data,
            country=form.country.data,
            type=form.type.data,
            year=form.year.data,
            #box=form.box.data
        )
        db.session.add(new_movie)
        db.session.commit()
        flash('Item created.')
        #movies = Movie_Info.query.all() 
        return redirect(url_for("existing_movies"))
    #movies = Movie_Info.query.all()    
    return render_template('add_movie.html', form=form)

@app.route('/existing_movies')
def existing_movies():
    movies = Movie_Info.query.all()
    return render_template('existing_movies.html', movies=movies)