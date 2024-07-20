from flask import Blueprint
from controllers.order_controller import create_order, get_order_items, get_all_orders

order_bp = Blueprint('orders', __name__)

order_bp.route('/', methods=['POST'])(create_order)
order_bp.route('/<int:id>/items', methods=['GET'])(get_order_items)
order_bp.route('/', methods=['GET'])(get_all_orders)