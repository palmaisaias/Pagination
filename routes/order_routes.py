from flask import Blueprint
from controllers.order_controller import save_order, get_order_items, find_all_orders, find_all_paginate

order_bp = Blueprint('orders', __name__)

order_bp.route('/', methods=['POST'])(save_order)
order_bp.route('/<int:id>/items', methods=['GET'])(get_order_items)
order_bp.route('/', methods=['GET'])(find_all_orders)
order_bp.route('/paginate', methods= ['GET'])(find_all_paginate)