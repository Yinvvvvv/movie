from datetime import datetime
from movie import db
#from flask_login import UserMixin



#定义数据模型

class Movie_Info(db.Model):
    __tablename__="movie_info"
    movie_id=db.Column(db.String(10),primary_key=True)
    movie_name=db.Column(db.String(50))
    release_date=db.Column(db.DateTime)
    country=db.Column(db.String(20))
    type=db.Column(db.String(10))
    year=db.Column(db.Integer)
    #box=db.relationship("Movie_Box", backref="movie_info", uselist=False)
    actors=db.relationship("Movie_Actor_Relation",backref="movie_info")

class Actor_Info(db.Model):
    __tablename__="actor_info"
    actor_id=db.Column(db.String(10),primary_key=True)
    actor_name=db.Column(db.String(20))
    gender=db.Column(db.String(2))
    country=db.Column(db.String(20))
    relationship=db.relationship("Movie_Actor_Relation",backref="actor_info")

class Movie_Actor_Relation(db.Model):
    __tablename__="movie_actor_relation"
    id=db.Column(db.String(10),primary_key=True)
    movie_id = db.Column(db.String(10), db.ForeignKey("movie_info.movie_id"))
    actor_id = db.Column(db.String(10), db.ForeignKey("actor_info.actor_id"))
    relation_type = db.Column(db.String(20))

class Movie_Box(db.Model):
    __tablename__="movie_box"
    movie_id=db.Column(db.String(10),primary_key=True)
    box=db.Column(db.Float)
    #movie=db.relationship("Movie_Info", backref='box', uselist=False)
