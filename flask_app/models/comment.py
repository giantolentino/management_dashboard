from flask_app.config.mysqlconnection import connectToMySQL
from .user import User
from flask import flash
from datetime import datetime
import math


class Comment:
    db = "residential"

    def __init__(self, data):
        self.id = data["id"]
        self.comment = data["comment"]
        self.vendors_id = data["vendors_id"]
        self.users_id = data["users_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.submitter = data["submitter"]

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days}d"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)}h"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)}m"
        else:
            return f"{math.floor(delta.total_seconds())}s"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (comment, vendors_id, users_id) VALUES (%(comment)s, %(vendors_id)s, %(users_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_comments_by_vendors_id(cls, data):
        query = (
            "SELECT users.first_name AS submitter, comments.* FROM comments LEFT JOIN users ON users_id= users.id WHERE vendors_id ="
            + str(data["id"])
            + " ORDER BY id DESC;"
        )

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        vendors = []

        for row in results:
            vendors.append(cls(row))
        print(vendors)
        return vendors

    @classmethod
    def destroy_comment(cls, data):
        query = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
