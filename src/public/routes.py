from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from src import create_app, db
from src.models import Product

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
@public_bp.route('/home')
def home():
    products = db.session.query(Product.prod_name, Product.prod_price )
    return render_template("home.html", products=products)