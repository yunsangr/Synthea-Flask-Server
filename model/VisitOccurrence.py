from src.queryCollection import *

class VisitOccurrence():

    @staticmethod
    def visit_by_visit_conecpt_id(db):
        print("VisitOccurrence by visit_concept: ")
        dataframe = db.execute(visit_by_concept_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_gender_concept(db):
        print("VisitOccurrence by gender: ")
        dataframe = db.execute(visit_by_gender_concept_query)
        return dataframe.to_json()

    @staticmethod
    def visit_by_race_concept_id(db):
        print("VisitOccurrence by race_concept_id: ")
        dataframe = db.execute(visit_by_race_query)
        print(dataframe.to_json())
        return dataframe.to_json()

    @staticmethod
    def visit_by_ethnicity_concept_id(db):
        print("VisitOccurrence by ethnicity_concept_id: ")
        dataframe = db.execute(visit_by_ethnicity_query)
        print(dataframe.to_json())
        return dataframe.to_json()

    @staticmethod
    def visit_by_age(db):
        print("VisitOccurrence by age: ")
        _ = db.execute(visit_by_age_query['preprocess'])
        dataframe = db.execute(visit_by_age_query['get_result'])
        print(dataframe.to_json())
        return dataframe.to_json()