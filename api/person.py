from flask_restx import Resource, Namespace
import sys
sys.path.append('..')
from src.Database import DataBase
from model.Person import Person

PersonRouter = Namespace('person')
db = DataBase()

@PersonRouter.route('/total')
class person_total(Resource):
    def get(self):
        return Person.person_total(db)

@PersonRouter.route('/by_gender')
class person_gender(Resource):
    def get(self):
        return Person.person_gender(db)

@PersonRouter.route('/by_ethnicity')
class person_ethnicity(Resource):
    def get(self):
        return Person.person_ethnicity(db)

@PersonRouter.route('/by_race')
class person_race(Resource):
    def get(self):
        return Person.person_race(db)

@PersonRouter.route('/death')
class person_death(Resource):
    def get(self):
        return Person.person_death(db)