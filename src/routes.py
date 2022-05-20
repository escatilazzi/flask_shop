from flask import Blueprint, render_template
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template("index.html")