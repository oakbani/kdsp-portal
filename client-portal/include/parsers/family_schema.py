from marshmallow import Schema, fields


class FamilyDetailsSchema(Schema):
    email = fields.String(required=True)
    father_name = fields.String(required=True)
    mother_name = fields.String(required=True)
    father_occupation = fields.String(required=True)
    mother_occupation = fields.String(required=True)
    father_contact_num = fields.String(required=True)
    mother_contact_num = fields.String(required=True)
