import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand
from src.admin.forms import AddCategory, AddBrand, AddDiscount, AddProduct
from werkzeug.utils import secure_filename

product_bp = Blueprint("product",__name__)


@product_bp.route("/product/<int:product_id>", methods=["GET","POST"])
def product_detail(product_id):
	product = Product.query.filter_by(prod_id=product_id).first()
	category = Category.query.filter_by(cat_id=product.prod_category_id).first()
	return render_template("products/product_detail.html", product=product, name=product.prod_name, image=product.prod_file, price=product.prod_price, quantity=product.prod_quantity, category=category, cat_name=category.cat_name)