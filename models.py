from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Name', db.String())
    project_finished = db.Column('Created', db.DateTime())
    description = db.Column('Description', db.Text)
    skills_practiced = db.Column('Skills Practiced', db.String())
    url = db.Column('URL', db.String())

    def __repr__(self):
        return f'''(Project : {self.project_finished}
        Name: {self.name}
        Url: {self.url}
        Description: {self.description}
        Skills Practiced: {self.skills_practiced}
        )'''
