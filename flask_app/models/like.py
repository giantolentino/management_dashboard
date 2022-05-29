from flask_app.config.mysqlconnection import connectToMySQL
from .user import User
from flask import flash


class Like:
    db = "residential"

    def __init__(self, data):
        self.comments_id = data["comments_id"]
        self.users_id = data["users_id"]
        self.liker = data["liker"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM likes;"

        results = connectToMySQL(cls.db).query_db(query)
        likes = []

        for row in results:
            likes.append(cls(row))

        return likes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO likes (comments_id, users_id) VALUES (%(comments_id)s, %(users_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
