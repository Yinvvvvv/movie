from datetime import datetime
from movie import db
#from flask_login import UserMixin



#定义数据模型

class Movies(db.Model):
    __tablename__="Movies"
    movie_id=db.Column(db.String(10),primary_key=True)
    movie_name=db.Column(db.String(50))
    release_date=db.Column(db.DateTime)
    country_movie=db.Column(db.String(20))
    type=db.Column(db.String(10))
    year=db.Column(db.Integer)
    box=db.Column(db.Float)
    relationship=db.relationship("Movie_Actor_Relationship",backref="movies")

class Actors(db.Model):
    __tablename__="Actors"
    actor_id=db.Column(db.String(10),primary_key=True)
    actor_name=db.Column(db.String(20))
    gender=db.Column(db.String(2))
    country_actor=db.Column(db.String(20))
    relationship=db.relationship("Movie_Actor_Relationship",backref="actors")

class Movie_Actor_Relationship(db.Model):
    __tablename__="Movie_Actor_Relationship"
    relation_id=db.Column(db.String(10),primary_key=True)
    movie_id = db.Column(db.String(10), db.ForeignKey("Movies.movie_id"))
    person_id = db.Column(db.String(10), db.ForeignKey("Actors.actor_id"))
    role_type = db.Column(db.String(20))

class Box(db.Model):
    __tablename__="Box"
    box_id=db.Column(db.String(10),primary_key=True)
    movie_id=db.Column(db.String(10),db.ForeignKey("Movies.movie_id"))
    box=db.Column(db.Float)
