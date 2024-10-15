from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar o blueprint da home (página inicial)
    from app.blueprints.home.routes import home_bp
    app.register_blueprint(home_bp)

    # Registrar o blueprint players
    from app.blueprints.players.routes import players_bp
    app.register_blueprint(players_bp, url_prefix='/players')

    return app
