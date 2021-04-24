template_factory = {
    'person': {
        'cols': ['person_id', 'birth_datetime'],
        'concepts': ['gender_concept_id', 'race_concept_id', 'ethnicity_concept_id'],
        'primary_key': 'person_id'

    },
    'visit_occurrence': {
        'cols': ['visit_occurrence_id', 'person_id', 'visit_start_datetime', 'visit_end_datetime'],
        'concepts': ['visit_concept_id'],
        'primary_key': 'visit_occurrence_id'
    },
    'condition_occurrence': {
        'cols': ['person_id', 'condition_start_datetime', 'condition_end_datetime', 'visit_occurrence_id'],
        'concepts': ['condition_concept_id'],
        'primary_key': 'visit_occurrence_id'

    },
    'drug_exposure': {
        'cols': ['person_id', 'drug_exposure_start_datetime', 'drug_exposure_end_datetime', 'visit_occurrence_id'],
        'concepts': ['drug_concept_id'],
        'primary_key': 'visit_occurrence_id'

    },
    'concept': {
        'cols': ['concept_name', 'domain_id'],
        'concepts': 'concept_id',
        'primary_key': 'concept_id'

    },
    'death': {
        'cols': ['person_id', 'death_date'],
        'concepts': '',
        'primary_key': 'person_id'

    }
}

def get_table_template(table_name):
    return template_factory.get(table_name)