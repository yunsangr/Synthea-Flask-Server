from src.queryCollection import *

class VisitOccurrence():

    @staticmethod
    def visit_by_visit_conecpt_id(db):
        dataframe = db.execute(visit_by_concept_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_gender_concept(db):
        dataframe = db.execute(visit_by_gender_concept_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_race_concept_id(db):
        dataframe = db.execute(visit_by_race_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_ethnicity_concept_id(db):
        dataframe = db.execute(visit_by_ethnicity_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_age(db):
        _ = db.execute(visit_by_age_query['preprocess'])
        dataframe = db.execute(visit_by_age_query['get_result'])
        return dataframe.to_json()