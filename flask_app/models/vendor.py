from flask_app.config.mysqlconnection import connectToMySQL
from .user import User
from flask import flash


class Vendor:
    db = "residential"

    def __init__(self, data):
        self.id = data["id"]
        self.vendor_type = data["vendor_type"]
        self.business_name = data["business_name"]
        self.contact_name = data["contact_name"]
        self.contact_number = data["contact_number"]
        self.contact_email = data["contact_email"]
        self.properties_id = data["properties_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM vendors;"

        results = connectToMySQL(cls.db).query_db(query)
        vendors = []

        for row in results:
            vendors.append(cls(row))
        return vendors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO vendors (vendor_type, business_name, contact_name, contact_number, contact_email) VALUES (%(vendor_type)s, %(business_name)s,%(contact_name)s,%(contact_number)s,%(contact_email)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def destroy_vendor(cls, data):
        query = "DELETE FROM vendors WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_vendor_by_id(cls, data):
        query = "SELECT * FROM vendors WHERE vendors.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        vendor = cls(result[0])
        return vendor

    @classmethod
    def update(cls, data):
        query = "UPDATE vendors SET vendor_type=%(vendor_type)s,business_name=%(business_name)s,contact_name=%(contact_name)s,contact_number=%(contact_number)s, contact_email=%(contact_email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_vendor(vendor):
        is_valid = True

        if len(vendor["vendor_type"]) < 3:
            is_valid = False
            flash("Vendor type must be more than 3 characters.")
        if len(vendor["business_name"]) < 3:
            is_valid = False
            flash("Business name must be at least 3 characters.")
        if len(vendor["contact_name"]) < 3:
            is_valid = False
            flash("Contact name must be at least 3 characters.")
        if len(vendor["contact_number"]) <= 0:
            is_valid = False
            flash("Contact number must be more than 0.")
        if len(vendor["contact_email"]) < 3:
            is_valid = False
            flash("Email must be at least 3 characters.")
        return is_valid
