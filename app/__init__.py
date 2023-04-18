#app/__init__.py

from flask import Flask

#initialize application
app=Flask(__name__,instance_relative_config=True)

#Load the views
from app import views

#Load configuration file
app.config.from_object('config')
