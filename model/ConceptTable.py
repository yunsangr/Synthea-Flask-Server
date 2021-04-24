from src.queryCollection import *
from src.TableTemplate import get_table_template
class ConceptTable():

    @staticmethod
    def get_all(db):
        dataframe = db.execute(concept_table_all)
        return dataframe.to_json()

    @staticmethod
    def get_by_page(db, page_num, limit):
        query = concept_table_pagination_query.format(offset=page_num * limit, limit=limit)
        dataframe = db.execute(query)
        return dataframe.to_json()

    @staticmethod
    def search_keyword(db, keyword):
        query = concept_table_keyword_search.format(keyword=keyword)
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def search_keyword_with_pagination(db, keyword, page_num, limit):
        query = concept_table_keyword_search_with_pagination.format(keyword=keyword, offset=page_num, limit=limit)
        df = db.execute(query)
        return df.to_json()

    @staticmethod
    def table_with_concept_name(db, table_name, target_column, keyword, page_num, limit):
        template = get_table_template(table_name)

        create_concept_view_with_name_query_lst = []
        table_primary_key = template['primary_key']
        columns = template['concepts'] + template['cols']
        concept_views = []
        join_all_views = ""
        views_to_drop = ""

        # Create concept views.
        for concept_type_id in template['concepts']:

            concept_type = concept_type_id[:-11] # where 11 is the length of "_concept_id"
            views_to_drop = views_to_drop + " , " + concept_type
            create_concept_view_with_name_query = create_concept_view_with_name.format(
                concept_type=concept_type,
                concept_type_id=concept_type_id,
                table_primary_key=table_primary_key,
                table_name=table_name
            )
            concept_views.append(concept_type)
            create_concept_view_with_name_query_lst.append(create_concept_view_with_name_query)
        views_to_drop = views_to_drop + f", {table_name}_table"

        # Extract wanted columns from table
        columns_str = ""
        for index, column in enumerate(columns):
            if index is 0:
                columns_str = column
            else:
                columns_str = columns_str + ", " + column
        extracted_table_query = extracted_table.format(
            table_name=table_name,
            columns=columns_str
        )

        # Join Views
        for concept_type in concept_views:
            join_all_views = join_all_views + " NATURAL JOIN " + concept_type;
        join_all_views = join_all_views + " NATURAL JOIN " + f"{table_name}_table"
        join_all_views = join_all_views[len(" NATURAL JOIN ") : ]
        joined_table_query = joined_table.format(
            join_all_views=join_all_views
        )


        # Search Keyword
        search_keyword_from_joined_table_query = search_keyword_from_joined_table.format(
            target_column=target_column,
            keyword=keyword
        )

        # Pagination [ Final query ]
        paginated_result_query = paginated_result.format(
            table_primary_key=table_primary_key,
            offset=page_num * limit,
            limit=limit
        )
        # Drop View
        drop_views_query = drop_views.format(
            views_to_drop=views_to_drop[2:]
        )

        # Execute all query

        db.execute(drop_views_query)
        for qry in create_concept_view_with_name_query_lst:
            db.execute(qry)
        db.execute(extracted_table_query)
        db.execute(joined_table_query)
        db.execute(search_keyword_from_joined_table_query)
        df = db.execute(paginated_result_query)
        if df is None:
            return "No matching result."
        return df.to_json()