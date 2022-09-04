import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand
from src.admin.forms import AddCategory, AddBrand, AddDiscount, AddProduct
from werkzeug.utils import secure_filename

cart_bp = Blueprint("cart",__name__)

@cart_bp.route("/cart",  methods=["GET","POST"])
@login_required
def show_cart():
    user_cart = current_user.cart
    if not user_cart:
        flash("Debes estar logueado")
    cart_products= [
        Product.query.filter(Product.prod_id=i.product_id).first()
        for i in current_user.cart
    ]
    render_template("cart/cart.html", cart_products=cart_products, user_cart=user_cart)    
