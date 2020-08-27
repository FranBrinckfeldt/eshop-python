from marshmallow import Schema, fields
from . import CategorySchema, BrandSchema

class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.Str() 
    description = fields.Str(allow_none=True)
    price = fields.Number()
    category = fields.Nested(CategorySchema())
    brand = fields.Nested(BrandSchema())
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
