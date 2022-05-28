from flask_app.config.mysqlconnection import connectToMySQL
from .user import User
from flask import flash


class Building:
    db = "residential"

    def __init__(self, data):
        self.id = data["id"]
        self.code = data["code"]
        self.name = data["name"]
        self.street_address = data["street_address"]
        self.zipcode = data["zipcode"]
        self.city = data["city"]
        self.users_id = data["users_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM buildings;"

        results = connectToMySQL(cls.db).query_db(query)
        buildings = []

        for row in results:
            buildings.append(cls(row))

        print(buildings)
        return buildings

    @classmethod
    def save(cls, data):
        query = "INSERT INTO buildings (code, name, street_address, zipcode, city) VALUES (%(code)s, %(name)s,%(street_address)s,%(zipcode)s,%(city)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def destroy_building(cls, data):
        query = "DELETE FROM buildings WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_building_by_id(cls, data):
        query = "SELECT * FROM buildings WHERE buildings.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        property = cls(result[0])
        return property

    @classmethod
    def update(cls, data):
        query = "UPDATE buildings SET code=%(code)s,name=%(name)s,street_address=%(street_address)s,zipcode=%(zipcode)s, city=%(city)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_building(building):
        is_valid = True
        if len(building["code"]) < 2:
            flash("Building Code must be at least 2 characters", "building")
            is_valid = False
        if len(building["name"]) < 3:
            flash("Name must be at least 3 characters", "building")
            is_valid = False
        if len(building["street_address"]) < 8:
            flash("Street Address must be at least 8 characters", "building")
            is_valid = False
        if len(building["zipcode"]) <= 5:
            flash("Zipcode must be at least 5 digits", "building")
            is_valid = False
        if len(building["city"]) < 3:
            flash("City must be at least 3 characters", "building")
            is_valid = False
        return is_valid
