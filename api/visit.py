from flask_restx import Resource, Namespace
import sys
sys.path.append('..')
from src.Database import DataBase
from model.VisitOccurrence import VisitOccurrence

VisitRouter = Namespace('visit')
db = DataBase()

@VisitRouter.route('/visit_concept_id')
class visit_concept_id(Resource):
    def get(self):
        return VisitOccurrence.visit_by_ethnicity_concept_id(db)

@VisitRouter.route('/visit_by_gender_concept')
class visit_by_gender_concept(Resource):
    def get(self):
        return VisitOccurrence.visit_by_gender_concept(db)

@VisitRouter.route('/visit_by_race_concept_id')
class visit_by_race_concept_id(Resource):
    def get(self):
        return VisitOccurrence.visit_by_race_concept_id(db)

@VisitRouter.route('/visit_by_ethnicity_concept_id')
class visit_by_ethnicity_concept_id(Resource):
    def get(self):
        return VisitOccurrence.visit_by_ethnicity_concept_id(db)

@VisitRouter.route('/visit_by_age')
class visit_by_age(Resource):
    def get(self):
        return VisitOccurrence.visit_by_age(db)