from flask import Blueprint, render_template, request
public_bp = Blueprint('public', __name__)

@public_bp.route('/')
@public_bp.route('/home')
def home():
    return render_template("home.html")