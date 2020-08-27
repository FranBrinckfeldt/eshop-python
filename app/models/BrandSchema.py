from marshmallow import Schema, fields

class BrandSchema(Schema):
    id = fields.Integer()
    name = fields.Str() 
    description = fields.Str(allow_none=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()