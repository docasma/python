from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask_app.models.ninja_oop import Ninja





class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name =data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninja =None

#get all method   
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        dojos=[]
        for row in results:           
            dojos.append(cls(row))
        return dojos
    
#get by  method  

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        ninjas = []  # Liste pour stocker les objets Ninja
        if results!=[0]:
         for row in results:
            ninja=cls(row)
            new_data_n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
            }

            ninja= Ninja(new_data_n)
            ninjas.append(ninja)
            return results

       
        

    
#create / insert method
    @classmethod
    def create_d(cls,data):
        query= "INSERT INTO dojos (name) VALUES(%(name)s);"
        results= connectToMySQL(DB).query_db(query,data)
        return results
