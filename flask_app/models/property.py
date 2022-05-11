from flask_app.config.mysqlconnection import connectToMySQL
from .user import User
from flask import flash

class Property:
  db = "residential"
  def __init__(self, data):
      self.id = data['id']
      self.code = data['code']
      self.street_address = data['street_address']
      self.zipcode = data['zipcode']
      self.city = data['city']
      self.users_id = data['users_id']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
      query = "SELECT * FROM properties;"

      results = connectToMySQL(cls.db).query_db(query)
      properties = []

      for property in results:
          properties.append( cls(property) )
      return properties

  @classmethod
  def save(cls, data):
      query= "INSERT INTO properties (code, street_address, zipcode, city) VALUES (%(code)s,%(street_address)s,%(zipcode)s,%(city)s);"
      result = connectToMySQL(cls.db).query_db(query,data)
      return result

  @classmethod
  def destroy(cls,data):
      query  = "DELETE FROM properties WHERE id = %(id)s;"
      return connectToMySQL(cls.db).query_db(query,data)

  @classmethod
  def get_property_by_id(cls, data ):
      query = "SELECT * FROM properties WHERE properties.id = %(id)s;"
      result = connectToMySQL(cls.db).query_db(query,data)
      property = cls(result[0])
      return property

  # @staticmethod
  # def validate_car(car):
  #   is_valid = True

  #   if int(car['price']) <= 0:
  #       is_valid = False
  #       flash("Price must be more than 0.")
  #   if len(car['make']) < 3:
  #       is_valid = False
  #       flash("Make must be at least 3 characters.")
  #   if len(car['model']) < 3:
  #       is_valid = False
  #       flash("Model must be at least 3 characters.")
  #   if int(car['year']) <= 0:
  #       is_valid = False
  #       flash("Year must be more than 0.")
  #   if len(car['description']) < 3:
  #       is_valid = False
  #       flash("Description must be at least 3 characters.")
  #   return is_valid

  # @classmethod
  # def update(cls,data):
  #     query = "UPDATE cars SET price=%(price)s,model=%(model)s,make=%(make)s,year=%(year)s,updated_at=NOW(),description=%(description)s, users_id=%(users_id)s WHERE id = %(id)s;"
  #     return connectToMySQL(cls.db).query_db(query,data)