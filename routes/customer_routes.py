from flask import Blueprint
from controllers.customer_controller import create_customer, get_customers

customer_bp = Blueprint('customers', __name__)

customer_bp.route('/', methods=['POST'])(create_customer)
customer_bp.route('/', methods=['GET'])(get_customers)

