from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # A secret key is required for session management and other security features
    # In a real app, this should be loaded from a config file and not hardcoded
    app.config['SECRET_KEY'] = 'dev'

    # Register the routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app
