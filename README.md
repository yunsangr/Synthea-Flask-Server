# Synthea-Flask-Server

## Description
This project implements Flask API server that serves medical information from database provided **Synthea**.
For more information about **Synthea**, click [here](https://synthetichealth.github.io/synthea/)

## Development Environments
- Python Version: 3.7 and above.
- Flask==1.1.2
- SQLAlchemy==1.4.11
- pandas==1.2.4
> This project does not provide PostgreSQL server. 

## How to Install and Setup
```
$ git clone https://github.com/yunsangr/Synthea-Flask-Server.git
$ pip install -r requirements.txt
```
Once you cloned this repository and installed all required packages, then you have to put PostgreSQL information to access.
Go to `src/database.py` , then you will see the following codes.
```python
class DataBase():  
    def __init__(self):  			# Put your PostgreSQL information here.
        host = "host"            	# ex) 12.34.56.78
		user = "user"  				# ex) userName
		password = "password"  		# ex) userPassword
		database = "database"  		# ex) databaseName
		self.engine = self.connect(user, password, database, host)
```

## How to run
```
$ python app.py
```

## APIs 
Once you ran the flask server, you can access to swagger server through the following url:
- http://127.0.0.1:5000/	(Swagger)


#### Concept

`GET`:  */concept/search_keyword_with_pagination/{keyword}/{page_num}/{limit}*

-  Provide information about **concept** table  with the following features
		- Pagination with `page_num` and `limit` from url parameters.
		- Search with `keyword` from url parameters.


`GET`:   */concept​/table_with_concept_name​/{table_name}​/{target_column}​/{keyword}​/{page_num}​/{limit}*
			
- Provide a database information with the following features.
		-  `table_name` indicates a name of database table . ex) person, concept, and so on.
		-  `concept_name` corresponding with `concept_id`.
		- Pagination with `page_num` and `limit` from url parameters.
		- Search with `keyword` and `target_column` from url parameters. where `target_column` is the column you want to search for the `keyword`.
	
#### Person
`GET`:  */person/by_ethnicity*
	-	Provide information about the number of person by ethnicity group.

`GET`:  */person/by_gender*
	-	Provide information about the number of person by gender group.

`GET`:  */person/by_race*
	-	Provide information about the number of person by race group.

`GET`:  */person/death*
	-	Provide information about the number of dead.

`GET`:  */person/total*
	-	Provide information about the total number of person in the person database table.

####  Visit
`GET`:  */visit/visit_by_age*
	-	Provide information about the number of visit-occurrence by age group (10 years)

`GET`:  */visit/visit_by_ethnicity_concept_id*
	-	Provide information about the number of visit-occurrence by ethnicity group.

`GET`:  */visit/visit_by_gender_concept*
	-	Provide information about the number of visit-occurrence by gender group.

`GET`:  */visit/visit_by_race_concept_id*
	-	Provide information about the number of visit-occurrence by race group.

`GET`:  */visit/visit_concept_id*
	-	Provide information about the number of visit-occurrence by the type of visit.

> For more defails about APIs,  refer to the Swagger service.


