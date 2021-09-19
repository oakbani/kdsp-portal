from marshmallow import Schema, fields


class ContactSchema(Schema):
    email = fields.String(required=True)
    name = fields.String(required=True)
    message = fields.String(required=True)
