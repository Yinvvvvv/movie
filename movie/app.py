# pip install Flask-SQLAlchemy
# pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install flask_sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install flask_bcrypt -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install flask_login -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install flask_mail -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install flask_wtf -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install email_validator
# pip install mysqlclient -i https://pypi.tuna.tsinghua.edu.cn/simple

from flask import Flask,render_template,request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"mysql://root:123456@localhost:3306/moviedb"
app.config['SECRET_KEY'] = 'secret_key'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_DATABASE_CHARSET'] = 'utf8' 
# Example in __init__.py
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)
# login_manage = LoginManager(app)
# login_manage.login_view = "login"


from movie import routes

