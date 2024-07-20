from models.schemas.schema import ma
from marshmallow import fields
from models.schemas.product_schema import ProductSchema

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.List(fields.Nested(ProductSchema))

    class Meta:
        fields = ('id', 'order_date', 'customer_id', 'products')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
