from flask import Flask
from flask_restx import Api
from src.Database import DataBase
from model.VisitOccurrence import VisitOccurrence
from model.ConceptTable import ConceptTable

from api.concept import ConceptRouter
from api.person import PersonRouter
from api.visit import VisitRouter

app = Flask(__name__)
api = Api(app = app,
          version = "1.0",
          title = "Synthea Data Flask APIs",
          description = "Provides various types of medical information provided by Synthea Database.")

api.add_namespace(ConceptRouter, '/concept')
api.add_namespace(VisitRouter, '/visit')
api.add_namespace(PersonRouter, '/person')


if __name__ == '__main__':
    app.run()
