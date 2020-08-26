from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.Str() 
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()