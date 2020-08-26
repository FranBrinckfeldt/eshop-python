from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.Str() 
    description = fields.Str()
    price = fields.Number()
    id_category = fields.Integer()
    id_brand = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
