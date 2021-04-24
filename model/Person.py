

class Person():
    @staticmethod
    def person_total(db):
        query = """SELECT COUNT(*) from person"""
        result = db.execute(query)
        return result.to_json()

    @staticmethod
    def person_gender(db):
        query = """SELECT gender_concept_id, COUNT(*) from person group by gender_concept_id"""
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def person_ethnicity(db):
        query = """SELECT ethnicity_concept_id, COUNT(*) from person group by ethnicity_concept_id"""
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def person_race(db):
        query = """SELECT race_concept_id, COUNT(*) from person group by race_concept_id"""
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def person_death(db):
        query = """SELECT COUNT(*) from death"""
        df = db.execute(query)
        return df.to_json()
