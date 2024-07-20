from models.schemas.schema import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_name = fields.String(required=True)
    email = fields.String(required=False)
    phone = fields.String(required=False)

    class Meta:
        fields = ('id', 'customer_name', 'email', 'phone')

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
