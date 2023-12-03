from flask_app.config.mysqlconnection import connectToMySQL,DB


class User:
    def __init__( self , data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.e_mail=data["e_mail"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]


#get all method
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        users=[]
        for row in results:           
            users.append(cls(row))
        return users
        


        
#insert new user
    @classmethod
    def insert_user(cls,data):
        query= "INSERT INTO users (first_name,last_name,e_mail) VALUES(%(first_name)s, %(last_name)s,%(e_mail)s);"
        results= connectToMySQL(DB).query_db(query,data)
        return results
    
#update user
    @classmethod
    def update(cls,data):
        query="UPDATE users SET first_name %(first_name)s,last_name %(last_name)s,e_mail %(e_mail)s WHERE id=%(id)s;" 
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_by_id(cls,data):
        query="SELECT*FROM users WHERE id=%(id)s;"
        results=connectToMySQL(DB).query_db(query,data)
        user=None
        if results!=[]:
            user=cls(results[0])
        return user    
    
#delete user
    @classmethod
    def delete(cls,data):
        query="DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(DB).query_db(query,data)



    


