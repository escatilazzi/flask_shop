import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand, Cart
from src.admin.forms import AddCategory, AddBrand, AddDiscount, AddProduct
from werkzeug.utils import secure_filename

cart_bp = Blueprint("cart",__name__)

@cart_bp.route("/addCart/<int:id>",  methods=["GET","POST"])
@login_required
def addCart(id):
    kart = Cart(cart_user_id=current_user.id, cart_product_id=current_user.id, cart_quantity=1)
    db.session.add(kart)
    db.session.commit()
    return redirect(url_for('public.home'))

@cart_bp.route("/cart",  methods=["GET","POST"])
@login_required
def show_cart():
    items = Product.query.join(Cart).filter(Product.prod_id == Cart.cart_product_id, Cart.cart_user_id == current_user.id)
    return render_template("/cart/cart.html", items=items, name=items.prod_name, price=items.prod_price, quantity=items.cart_quantity)
