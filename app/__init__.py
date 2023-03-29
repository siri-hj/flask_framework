from flask import Flask, current_app, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

ctx = app.app_context()
ctx.push()

app.config.from_object('config')
db = SQLAlchemy(app)

from app import models,views