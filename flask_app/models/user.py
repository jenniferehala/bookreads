from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.author = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL("bookreads_db").query_db(query,data)

    @staticmethod
    def reg_valid(user_data):
        is_valid = True
        query="SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL("bookreads_db").query_db(query,user_data)
        print(results)
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(results) > 1:
            flash("Email exists")
            is_valid = False
        if len(user_data["first_name"]) < 2:
            flash("We need first name filled")
            is_valid = False
        if len(user_data["last_name"]) < 2:
            flash("We need last name filled")
            is_valid = False
        if not email_reg.match(user_data['email']):
            flash("Invalid email Address/Password")
            is_valid = False
        if user_data["confirm_pass"] != user_data["password"]:
            flash("Confirm password doesn't match!")
            is_valid = False

        return is_valid
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("bookreads_db").query_db(query,data)

        if len(user_db) < 1:      #I know there are no users if less than 0
            return False          #if the length of the dictionary < 0, means didn't return anything
        
        return cls(user_db[0])    #if found, return instance of dictionary