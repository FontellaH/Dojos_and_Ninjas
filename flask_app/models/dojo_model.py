from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE    # this is sotred in my init.py

from flask_app.models import ninja_model  # avoid cirrcular import


class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#Crud...&... @classmethod below here ↓↓↓↓↓



    
    @classmethod 
    def get_all(cls):   #Getting all the dojos
                query = """
                    SELECT *FROM dojos;
                """
                results = connectToMySQL(DATABASE).query_db(query)
                print(results)
                all_dojos = []      #This is the dojo object !IMPORTANT FOR TEST
                for row_from_db in results:
                    dojo_instance = cls(row_from_db)
                    all_dojos.append(dojo_instance)
                return all_dojos    #THIS IS RETURNING THE dojoS OBJECT
    

    
    @classmethod
    def create(cls, data):       #CREATE  WILL BE USING "INSERT" FOR THIS METHOD
            query = """
                INSERT into dojos (name)  
                VALUES (%(name)s);
            """
            return connectToMySQL(DATABASE).query_db(query,data)
    

    
    @classmethod
    def get_one(cls,data):     #Getting one user from the db this is linked to get_0ne route
        query = """
            SELECT * FROM dojos WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:        #Asking if results comes back empty i didnt find my results
            dojo_instance = cls(results[0])    #Telling it to give back user in index[0]
            return dojo_instance
        return results    
    
    @classmethod
    def create(cls, data):       #CREATE  WILL BE USING "INSERT" FOR THIS METHOD
            query = """
                INSERT into dojos (name)  
                VALUES ( %(name)s);
            """
            return connectToMySQL(DATABASE).query_db(query,data)



    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
          SELECT * FROM dojos LEFT JOIN  ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            
            dojo = cls( results[0] )  # results will be a list of  objects with the ninja attached to each row. 
            dojo.ninjas = []  
            for row_from_db in results:
                ninja_data = {     # Now we parse the ninja data to make instances of ninjas and add them into our list.    
                    "id" : row_from_db["ninjas.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "dojo_id" : row_from_db["dojo_id"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"]
                }
                dojo.ninjas.append(ninja_model.Ninja(ninja_data) )
            return dojo
        return  False
