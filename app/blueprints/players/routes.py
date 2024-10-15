from flask import Blueprint, render_template

players_bp = Blueprint('players', __name__)

@players_bp.route('/players')
def home():
    return render_template('home.html')
