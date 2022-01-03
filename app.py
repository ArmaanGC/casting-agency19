import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, db_drop_and_create_all, Actor, Movie, Performance, db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response

  #-----------------------------------------------------------------------------

  #ROUTES

  # ENDPOINT: GET /actors
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
      actor_data = Actor.query.order_by(Actor.id).all()

      if len(actor_data) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'actors': [actor.format() for actor in actor_data]
      }), 200

  # ENDPOINT: GET /movies
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
      movie_data = Movie.query.order_by(Movie.id).all()

      if len(movie_data) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'movies': [movie.format() for movie in movie_data]
      }), 200

  # ENDPOINT: POST /actors
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actor(payload):
      body = request.get_json()

      if (body is None):
          abort(400)
      age = body.get('age', None)
      name = body.get('name', None)
      gender = body.get('gender', None)
      if ((age is None) or (name is None) or (gender is None)):
          abort(422)
      try:
          actor = Actor(name=name, gender=gender, age=age)
          actor.insert()

          return jsonify({
              'success': True,
              'created': actor.id
          }), 200

      except:
          abort(422)

  # ENDPOINT: POST /movies
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def post_movie(payload):
      body = request.get_json()
      if (body is None):
          abort(400)
      title = body.get('title', None)
      release_date = body.get('release_date', None)

      if ((title is None) or (release_date is None)):
          abort(422)
      try:
          movie = Movie(title=title, release_date=release_date)
          movie.insert()

          return jsonify({
              'success': True,
              'created': movie.id
          }), 200

      except:
          abort(422)

  # ENDPOINT: PATCH /actors/<id>
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('update:actors')
  def update_actor(payload, actor_id):
      actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

      if actor is None:
          abort(404)

      body = request.get_json()    
      if body is None:
         abort(400)   
      
      age = body.get('age', None)
      name = body.get('name', None)
      gender = body.get('gender', None)

      try:
          if age is not None:
                actor.age = age
          if name is not None:
                actor.name = name    
          if gender is not None:
                actor.gender = gender

          actor.update()

          return jsonify({
              'success': True,
              'actor': actor.format()
          }), 200

      except:
          abort(422)

  # ENDPOINT: PATCH /movies/<id>
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('update:movies')
  def update_movie(payload, movie_id):
      movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

      if movie is None:
          abort(404)
      body = request.get_json()
      if body is None:
             abort(400)

      title = body.get('title', None)
      release_date = body.get('release_date', None)

      try:
          if title is not None:
              movie.title = title
          if release_date is not None:
              movie.release_date = release_date

          movie.update()

          return jsonify({
              'success': True,
              'movie': movie.format()
          }), 200

      except:
          abort(422)
  
  # ENDPOINT: Delete /actors/<id>
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, actor_id):
      actor = Actor.query.filter(Actor.id == actor_id).one_or_none()  
      if actor is None:
              abort(404)

      try:
          actor.delete()

          return jsonify({
              'success': True,
              'delete': actor_id
          }), 200
      except:
          abort(422)

  # ENDPOINT: Delete /movies/<id>
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, movie_id):
      movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
      if movie is None:
              abort(404)  
      try:
          movie.delete()

          return jsonify({
              'success': True,
              'delete': movie_id
          }), 200
      except:
          abort(422)

  #-----------------------------------------------------------------------------

  # Error Handlers

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Error: Bad Request"
      }), 400

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "Error: Resource Not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Error: Unprocessable"
      }), 422

  @app.errorhandler(AuthError)
  def auth_error(AuthError):
      return jsonify({
          "success": False,
          "error": AuthError.status_code,
          "message": AuthError.error['description']
      }), AuthError.status_code

  return app  


app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)