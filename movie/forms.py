# forms.py
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, FloatField
from wtforms.validators import InputRequired
from movie.models import  Movies, Actors, Movie_Actor_Relationship, Box
#from flask_login import current_user


class MovieForm(FlaskForm):
    movie_name = StringField('Name', validators=[InputRequired()])
    release_date = DateTimeField('Release Date', validators=[InputRequired()])
    country_movie = StringField('Country', validators=[InputRequired()])
    movie_type = StringField('Type', validators=[InputRequired()])
    year = IntegerField('Year', validators=[InputRequired()])
    box = FloatField('Box')  # You can customize this as needed
