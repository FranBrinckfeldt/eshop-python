from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.Str()
    firstname = fields.Str()
    lastname = fields.Str()
    birth = fields.Date()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()