from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar o blueprint da home (página inicial)
    from app.blueprints.home.routes import home_bp
    app.register_blueprint(home_bp)

    # Registrar o blueprint players
    from app.blueprints.main.routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    # Registrar o blueprint registro
    from app.blueprints.register.routes import register_bp
    app.register_blueprint(register_bp, url_prefix='/register')   

    # Registrar o blueprint do login
    from app.blueprints.login.routes import login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    return app
