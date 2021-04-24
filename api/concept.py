from flask_restx import Resource, Namespace, reqparse
import sys
sys.path.append('..')
from src.Database import DataBase
from model.ConceptTable import ConceptTable

ConceptRouter = Namespace('concept')
db = DataBase()


@ConceptRouter.route('/search_keyword_with_pagination/<string:keyword>/<int:page_num>/<int:limit>',
                     doc={
                         'params': {
                             'keyword': 'Keyword to search.',
                             'page_num': 'Page number to display.',
                             'limit': 'The number of rows to display in a page.'
                         }
                     })
class search_keyword_with_pagination(Resource):

    @staticmethod
    def get(keyword, page_num, limit):
        print(keyword, page_num, limit)
        return ConceptTable.search_keyword_with_pagination(
            db=db,
            keyword=keyword,
            page_num=int(page_num),
            limit=int(limit))


@ConceptRouter.route('/table_with_concept_name/'
                     '<string:table_name>/<string:target_column>/<string:keyword>/<int:page_num>/<int:limit>',
                     doc={
                         'params': {
                             'table_name': 'Table name in Database.\n ex) person, concept, visit_occurrence, and etc',
                             'target_column': 'Target column in table to search.\n ex) race and gender for person.',
                             'keyword': 'Keyword to search.\n ex) Asian for race and FEMALE for gender',
                             'page_num': 'Page number to display.',
                             'limit': 'The number of rows to display in a page.'
                         }
                        }
                     )
class table_with_concept_name(Resource):

    def get(self, table_name, target_column, keyword, page_num, limit):
        return ConceptTable.table_with_concept_name(
            db=db,
            table_name=table_name,
            target_column=target_column,
            keyword=keyword,
            page_num=int(page_num),
            limit=int(limit))
