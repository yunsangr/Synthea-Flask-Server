from pypika import Query, Table


# Table with Concept Name.
#   Drop view.
drop_views = """
DROP VIEW IF EXISTS {views_to_drop}, unioned_table,searched_table CASCADE;
"""
#   Create concept views.
create_concept_view_with_name = """

CREATE VIEW {concept_type} AS
	SELECT  {concept_type_id}, 
		concept.concept_name as {concept_type},  
		{table_primary_key}
	FROM {table_name} INNER JOIN concept 
	ON  {table_name}.{concept_type_id} = concept.concept_id;

"""
#   Extract wanted columns from table.
extracted_table = """
CREATE VIEW {table_name}_table AS
	SELECT {columns}
	FROM {table_name};
"""
#   Join Views
joined_table = """
CREATE VIEW unioned_table AS
	SELECT * FROM 
	{join_all_views}; 
"""
#   Search Keyword
search_keyword_from_joined_table = """

CREATE VIEW searched_table AS
	SELECT * FROM unioned_table 
	WHERE {target_column} LIKE '%%{keyword}%%';
"""

#   Pagination
paginated_result = """
SELECT * FROM searched_table ORDER BY {table_primary_key} OFFSET {offset} LIMIT {limit};
"""




# Concept Table
# todo: Pagination

search = "Visit"
concept = Table('concept')
concept_table_keyword = str(Query.from_(concept).select(concept.concept_id, concept.concept_name).
                            where(
                                        concept.concept_name.regex(f"_{search}_")

                        ))


concept_table_all = """SELECT concept_id, concept_name, domain_id FROM concept LIMIT 10;"""

concept_table_keyword_search = '''SELECT concept_id, concept_name, domain_id FROM concept WHERE concept_name LIKE '%%{keyword}%%';'''

concept_table_keyword_search_with_pagination = '''SELECT concept_id, concept_name, domain_id FROM concept WHERE concept_name LIKE '%%{keyword}%%' ORDER BY concept_id OFFSET {offset} LIMIT {limit};'''

concept_table_pagination_query = """SELECT concept_id, concept_name, domain_id FROM concept ORDER BY concept_id OFFSET {offset} LIMIT {limit};"""


# Visit Table
visit_by_concept_query = """
                                        SELECT visit_concept_id, count(*) 
                                        from visit_occurrence 
                                        GROUP BY visit_concept_id"""
visit_by_gender_concept_query = """
                                        SELECT person.gender_concept_id, count(*)
	                                    FROM person INNER JOIN visit_occurrence 
	                                    ON person.person_id = visit_occurrence.person_id
	                                    GROUP BY person.gender_concept_id;"""
visit_by_race_query = """
                                        SELECT person.race_concept_id, count(*)
                                        FROM person INNER JOIN visit_occurrence 
                                        ON person.person_id = visit_occurrence.person_id
                                        GROUP BY person.race_concept_id;"""
visit_by_ethnicity_query = """
                                        SELECT person.ethnicity_concept_id, count(*)
                                            FROM person INNER JOIN visit_occurrence 
                                            ON person.person_id = visit_occurrence.person_id
                                            GROUP BY person.ethnicity_concept_id;

                                """


visit_by_age_query = {
        'preprocess': """
DROP VIEW IF EXISTS person_visit, age_visit_count, decade_age_visit_count CASCADE;

CREATE VIEW person_visit(person_id, visit_occurrence_id, birth_datetime, visit_start_datetime, age)
	AS SELECT visit_occurrence.person_id, 
			  visit_occurrence.visit_occurrence_id, 
			  person.birth_datetime, 
			  visit_occurrence.visit_start_datetime,
			  EXTRACT(YEAR FROM age(visit_occurrence.visit_start_datetime, person.birth_datetime)) as "age"
    FROM person INNER JOIN visit_occurrence
	ON person.person_id = visit_occurrence.person_id
	;

CREATE VIEW age_visit_count(age, visit_count)
	AS SELECT age, count(*) FROM person_visit GROUP BY age;

CREATE VIEW decade_age_visit_count
	AS SELECT 
		SUM(visit_count) FILTER (WHERE (age >= 0 AND age <10)) AS "0-9",
		SUM(visit_count) FILTER (WHERE (age >= 10 AND age <20)) AS "10-19",
		SUM(visit_count) FILTER (WHERE (age >= 20 AND age <30)) AS "20-29",
		SUM(visit_count) FILTER (WHERE (age >= 30 AND age <40)) AS "30-39",
		SUM(visit_count) FILTER (WHERE (age >= 40 AND age <50)) AS "40-49",
		SUM(visit_count) FILTER (WHERE (age >= 50 AND age <60)) AS "50-59",
		SUM(visit_count) FILTER (WHERE (age >= 60 AND age <70)) AS "60-69",
		SUM(visit_count) FILTER (WHERE (age >= 70 AND age <80)) AS "70-79",
		SUM(visit_count) FILTER (WHERE (age >= 80 AND age <90)) AS "80-89",
		SUM(visit_count) FILTER (WHERE (age >= 90 AND age <100)) AS "90-99",
		SUM(visit_count) FILTER (WHERE (age >= 100)) AS "above 100"
	FROM age_visit_count;
        """,
        'get_result': """SELECT * FROM decade_age_visit_count;""",
        'drop': """
        DROP TABLE pv;
        """
}