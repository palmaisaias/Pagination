from flask import Blueprint
from controllers.product_controller import create_product, get_products

product_bp = Blueprint('products', __name__)

product_bp.route('/', methods=['POST'])(create_product)
product_bp.route('/', methods=['GET'])(get_products)
