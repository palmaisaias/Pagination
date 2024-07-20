from flask import Blueprint
from controllers.product_controller import save_product, get_products, find_all_paginate

product_bp = Blueprint('products', __name__)

product_bp.route('/', methods=['POST'])(save_product)
product_bp.route('/', methods=['GET'])(get_products)
product_bp.route('/paginate', methods= ['GET'])(find_all_paginate)
