from marshmallow import Schema, fields


class DonorRegistrationSchema(Schema):
    name = fields.String(required=True)
    contact_num = fields.String(required=True)


class FinancialAidRecipientRegistrationSchema(Schema):
    family_id = fields.Integer(required=True)
    family_income = fields.Integer(required=True)
    expenses = fields.Integer(required=True)


class FinancialAidRecipientUpdateByAdminSchema(Schema):
    eligible_for_aid = fields.Boolean(required=True)


class FinancialAidRecipientSchema(Schema):
    email = fields.String(required=True)
    family_income = fields.Integer(required=True)
    expenses = fields.Integer(required=True)
    eligible_for_aid = fields.Boolean(required=True)
