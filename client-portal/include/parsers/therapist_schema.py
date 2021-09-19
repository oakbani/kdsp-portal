from marshmallow import Schema, fields


class TherapistDetailsSchema(Schema):
    name = fields.String(required=True)
    contact_num = fields.String(required=True)
