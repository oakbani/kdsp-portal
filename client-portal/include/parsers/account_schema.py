from marshmallow import Schema, fields
from marshmallow.validate import Length

from ..models import Account as AccountModel


# class AccountSchema(ModelSchema):
#     created_at = fields.String()
#     modified_at = fields.String()
#     role = fields.Nested('RoleSchema', only=('id', 'title'))

#     class Meta:
#         model = AccountModel


class AccountRegistrationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True)


class AccountLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class AccountUpdateByAdminSchema(Schema):
    role_id = fields.Integer()
