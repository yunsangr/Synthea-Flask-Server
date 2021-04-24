

class Person():
    @staticmethod
    def person_total(db):
        print("person total: ")

        query = """SELECT COUNT(*) from person"""
        result = db.execute(query)
        print(result)
        return result.to_json()

    @staticmethod
    def person_gender(db):
        print("person by gender_concept_id: ")
        query = """SELECT gender_concept_id, COUNT(*) from person group by gender_concept_id"""
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def person_ethnicity(db):
        print("person by ethnicity_concept_id: ")
        query = """SELECT ethnicity_concept_id, COUNT(*) from person group by ethnicity_concept_id"""
        df = db.execute(query)
        print(df)
        return df.to_json()

    @staticmethod
    def person_race(db):
        print("person by race_concept_id: ")
        query = """SELECT race_concept_id, COUNT(*) from person group by race_concept_id"""
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def person_death(db):
        print("person who died: ")
        query = """SELECT COUNT(*) from death"""
        df = db.execute(query)
        return df.to_json()
