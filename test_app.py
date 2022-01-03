import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor, db_drop_and_create_all

#Access Tokens

CASTING_ASSISTANT = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwYzBlMDljODMwMDZmMWIyMjQ2IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTEyMzA1OSwiZXhwIjoxNjQxMTMwMjU5LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.L-meuT-NgQn82c4aLSGAu9meV0nf1yBtfksepFbYt4_oqqoAe8YRQqzzJ7EHiOkED81Ah1A64hv4TXrAZ-M5AeCSZbHDGB-o-bTQ9oHvmlP3AR5Aoy9pxJTTpRWX0vhkqf5fv98aZSpGWY2EAxCz2-zF-t-FkwUNzPYwVkzsH4WEx1kAQ16gQ-WLC3j6ZcV8tpNZtJ3dzzgHtIYbzy_-acXRGa7GsmLrhTNaxljy0103nXNk8ftg1wPbwn2D8gvQwLwEh2yoI7gFDf2b7k22jprGigHn7eY4urTXBzvrQbSwyedDIMk719EFCgAVa85hcLoviaOVUyOZh1b5dbkRUw')

CASTING_DIRECTOR = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwOTRmYTJjZDEwMDY5ZWU2Mjc5IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTEyMjk5MSwiZXhwIjoxNjQxMTMwMTkxLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.qwXcj2o-kKdoIehkXl5UUciWJTB4YhLy_Y4OoshoyaY6BRD9-nDaBqfcc8owcmHArzeynpHTvTDxY3kAsx4AKGZXX8mmPaYIeorGCsNIs8wjnunD7fQtJkvO4zlMogAEo7nAYsFS0mEmOXCOMG8ZZ4t6DdraCC6bfgt-usHCeUfvFKHXQjHT3owcETdEvtDiVaDmOcESwrHhllkWMegnoHr5rBnasJKWD9fbvBm7XAnFQnduEqEAg51iD6E14DzLUBiT1rGV4MnxL1CxEIHQmJIKic81tMnHpbOpsE4VxoymaKfY0G6syCKbtTDsFhnnKZyYy7_TljQ_GbKvs50gKA')
EXECUTIVE_PRODUCER = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwNWZmYTJjZDEwMDY5ZWU2MjZlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTEyMjg1NSwiZXhwIjoxNjQxMTMwMDU1LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.mhShLhSqKR3kMihTZXFIHqshA5bZmy-YosAmc45N6LZ4LkwQ9ZRk0zNQusSsW1EQ_4Ow4484TyjPDOKcWiOKfRfRiVN7q3HL5z0A2fw_L_1yxO-suCLspW9nbrEweS2ZodNrZfMr0V1MSvw7Ns6VGUoz3oPCaMOHvKDGbir2c-Vy8BcqL8_uI0XLfE06J-6s82wKxLsOVi35qvlo6YeWN_sqebEgjJzu4meaTOhimmoGZKG_LP4dIUhUvpy_aoKYthNbHtUHHyhMR0SNTpOdUqafy_EIagP3VWQBiJw13cqfZdFGj-9hV0PoUUKCNKD6P4fZy5ETJ-xxQQh0UEl_3A')

#Creating headers from above tokens

cast_assis_header = {
    'Authorization': "Bearer " + CASTING_ASSISTANT
}

cast_dir_header = {
    'Authorization': "Bearer " + CASTING_DIRECTOR
}

exec_prod_header = {
    'Authorization': "Bearer " + EXECUTIVE_PRODUCER
}

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            # self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    # test endpoint: get:actors

    #role: executive producer
    def test_get_actors1(self):
        res = self.client().get('/actors',
                                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #role: casting director
    def test_get_actors2(self):
        res = self.client().get('/actors',
                                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #role: casting assistant
    def test_get_actors3(self):
        res = self.client().get('/actors',
                                headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    # test endpoint: get:movies

    #role: executive producer
    def test_get_movies1(self):
        res = self.client().get('/movies',
                                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #role: casting director
    def test_get_movies2(self):
        res = self.client().get('/movies',
                                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #role: casting assistant
    def test_get_movies3(self):
        res = self.client().get('/movies',
                                headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    # test endpoint: post:actors

    #role: executive producer

    def test_create_actor(self):
        actor = {'name': 'Shahrukh', 'age': '38',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                                 headers=exec_prod_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: casting director
    #negative scenario: 422

    def test_create_actor_error_422(self):
        actor = {'name': 'Error',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                                 headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Unprocessable")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_create_actor_casting_assistant(self):
        actor = {'name': 'Aamir', 'age': '40',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                                 headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # test endpoint: post:movies

    #role: executive producer

    def test_create_movies(self):
        movie = {'title': 'Walking_dead',
                     'release_date': '17/6/2021'}
        res = self.client().post('/movies', json=movie,
                                 headers=exec_prod_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: executive producer
    #negative scenario: 422

    def test_create_movies_error_422(self):
        movie = {'title': 'Life'}
        res = self.client().post('/movies', json=movie,
                                 headers=exec_prod_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Unprocessable")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_create_movies_casting_assistant(self):
        movie = {'title': 'Life of Pie',
                     'release_date': '17/6/2021'}
        res = self.client().post('/actors', json=movie,
                                 headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # test endpoint: delete:actors

    #role: executive producer

    def test_delete_actors(self):
        res = self.client().delete('/actors/1', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    #role: casting director
    #negative scenario: 404

    def test_delete_actors_error_404(self):
        res = self.client().delete('/actors/400', headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Resource Not found")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_delete_actors_casting_assistant(self):
        res = self.client().delete('/actors/1', headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # test endpoint: delete:movie

    #role: executive producer

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    #role: executive producer
    #negative scenario: 404

    def test_delete_movie_error_404(self):
        res = self.client().delete('/movies/400', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Resource Not found")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_delete_movie_casting_assistant(self):
        res = self.client().delete('/movies/1', headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # test endpoint: update:actors

    #role: executive producer

    def test_update_actor(self):
        actor = {'name': 'Vicky'}
        res = self.client().patch('/actors/2', json=actor,
                                  headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: castig director
    #negative scenario: 400

    def test_update_actor_error_400(self):
        res = self.client().patch('/actors/1', json=None,
                                  headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Bad Request")

    # test endpoint: update:movies

    #role: executive producer

    def test_update_movies(self):
        actor = {'name': 'Vicky'}
        res = self.client().patch('/movies/2', json=actor,
                                  headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: castig director
    #negative scenario: 400

    def test_update_movies_error_400(self):
        res = self.client().patch('/movies/1', json=None,
                                  headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Bad Request")

    