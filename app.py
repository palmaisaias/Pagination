from flask import Flask
from config import Config
from database import db
from models.schemas.schema import ma
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    #limiter requires key_func to tell it how to target people. using a remote address tells it to target based in IP addresses
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["200 per day", "3 per second"]
    )
    limiter.init_app(app)

    from routes.customer_routes import customer_bp
    from routes.order_routes import order_bp
    from routes.product_routes import product_bp

    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(product_bp, url_prefix='/products')

    limiter.limit("5 per minute")(customer_bp)
    limiter.limit("5 per minute")(order_bp)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
