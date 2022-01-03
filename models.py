import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
def db_drop_and_create_all():
    '''drops the database tables and starts fresh
    can be used to initialize a clean database
    '''
    db.drop_all()
    db.create_all()
    db_populate()

def db_populate():
    new_actor1 = Actor('Ranbir', 'Male', '28')
    new_actor2 = Actor('Deepika', 'Female', '26')
    
    new_movie1 = Movie('Good_old_days', date.today())
    new_movie2 = Movie('Villain', date.today())

    new_actor1.insert()
    new_actor2.insert()

    new_movie1.insert()
    new_movie2.insert()

    new_performance1 = Performance.insert().values(
        movie_id=new_movie1.id, actor_id=new_actor1.id)
    new_performance2 = Performance.insert().values(
        movie_id=new_movie1.id, actor_id=new_actor2.id)

    db.session.execute(new_performance1)
    db.session.execute(new_performance2)
    db.session.commit()

#Performance table n:n relationship

Performance = db.Table('Performance', db.Model.metadata,
    db.Column('Movie_id', Integer, db.ForeignKey('movies.id')),
    db.Column('Actor_id', Integer, db.ForeignKey('actors.id'))
)

#Actors table

class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  gender = Column(String)
  age = Column(Integer)

  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name' : self.name,
      'gender': self.gender,
      'age': self.age
    }

#Movie table

class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = db.relationship('Actor', secondary=Performance,
                             backref=db.backref('performances', lazy='joined'))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date}

