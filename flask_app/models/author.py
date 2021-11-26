from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
import re

class Author:
    def __init__(self,data):
        self.id = data["id"]
        self.author_fname = data["author_fname"]
        self.author_lname = data["author_lname"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = []
    
    @classmethod
    def get_user_authors(cls,data):
        query="SELECT * FROM users JOIN books ON users.id = user_id WHERE users.id = %(id)s"
        results = connectToMySQL("bookreads_db").query_db(query,data)
        
        user_authors= user.User(results[0])

        for row in results:
            author_data = {
                "id" : row["books.id"],
                "author_fname" : row["author_fname"],
                "author_lname" : row["author_lname"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            user_authors.author.append(Author(author_data))
        return user_authors
    
    @staticmethod
    def validate_author(author):
        is_valid = True
        if len(author["author_fname"]) < 1:
            flash("Author first name needs to be filled in")
            is_valid = False
        if len(author["author_lname"]) < 1:
            flash("Author last name needs to be filled in")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query="INSERT INTO cars (price, model, make, year, description,user_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s,%(description)s,%(user_id)s);"
        return connectToMySQL("cars_db").query_db(query,data)



