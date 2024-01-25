from marshmallow import Schema, fields,validate
from config.config import Config

class LoginSchema(Schema):
    username = fields.Str(required = True, validate = validate.Regexp(Config.USERNAME_REGEX))
    password = fields.Str(required = True)

class LoginSuccessSchema(Schema):
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)

class UserRegisterSchema(Schema):
    username = fields.Str(required = True, validate = validate.Regexp(Config.USERNAME_REGEX))
    password = fields.Str(required = True, validate = validate.Regexp(Config.PASSWORD_REGEX))
    city = fields.Str(required = True, validate = validate.Regexp(Config.CITY_REGEX))
    zipcode = fields.Str(required = True, validate = validate.Regexp(Config.ZIPCODE_REGEX))
    