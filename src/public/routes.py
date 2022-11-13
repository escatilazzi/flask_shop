from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from src import create_app, db
from src.models import Product, Category

public_bp = Blueprint('public', __name__)

@public_bp.route("/")
@public_bp.route("/home")
def home():
    # prod_data = db.session.query(Product.prod_name, Product.prod_price )
    prod_data =  db.session.query(Product).all()
    # categories = db.session.query(Category).all()
    categories = Category.categories()
    return render_template("home.html", prod_data=prod_data, categories=categories)


