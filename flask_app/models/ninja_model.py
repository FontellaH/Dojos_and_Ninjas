from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#Crud...&... @classmethod below here ↓↓↓↓↓

    @classmethod
    def create(cls, data):       #CREATE  WILL BE USING "INSERT" FOR THIS METHOD
            query = """
                INSERT into ninjas (dojo_id, first_name, last_name, age)  
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
            """
            return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod 
    def get_all(cls):   #Getting all the Ninjas
                query = """
                    SELECT *FROM ninjas;
                """
                results = connectToMySQL(DATABASE).query_db(query)
                print(results)
                all_ninjas = []      #This is the ninja object !IMPORTANT FOR TEST
                for row_from_db in results:
                    ninja_instance = cls(row_from_db)
                    all_ninjas.append(ninja_instance)
                return all_ninjas    #THIS IS RETURNING THE ninjaS OBJECT


