from flask import Blueprint, render_template

main_bp = Blueprint('players', __name__)

@main_bp.route('/')
def home():
    return render_template('main.html')
