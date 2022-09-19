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
def addCart(id):
    if current_user.is_anonymous:
        return redirect(url_for('account.login'))
    kart = Cart(cart_user_id=current_user.id, cart_product_id=id, cart_quantity=1)
    db.session.add(kart)
    db.session.commit()
    return redirect(url_for('public.home'))

@cart_bp.route("/cart",  methods=["GET","POST"])
def show_cart():
    if current_user.is_anonymous:
        return redirect(url_for('account.login'))
    cart_products= db.session.query(Product.prod_name, Product.prod_price, Cart.cart_quantity).join(Cart, Product.prod_id==Cart.cart_id).filter(Cart.cart_user_id)
    return render_template("/cart/cart.html", cart_products=cart_products)


@cart_bp.route("/cart/<int:product_id>", methods=["GET","POST"])
@login_required
def increase_cart(product_id):
    kart = Cart.query.filter(Cart.cart_product_id == product_id, Cart.cart_user_id == current_user.id).first()
    print(kart)
    p = Product.query.filter(Product.prod_id == product_id).first()
    while kart.cart_quantity < p.prod_quantity:
        kart.cart_quantity += 1
        db.session.commit()
        return redirect(url_for('cart.show_cart'))
    else:
        flash("No hay stock")
        return redirect(url_for("cart.show_Cart"))