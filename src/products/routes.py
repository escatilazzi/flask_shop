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
def displayProduct(prod_id, prod_cat_id):
	prod_detail = Product.query.filter_by(prod_id=prod_id)
	category = Category.query.filter_by(id=prod_cat_id)
	return render_template("product.html", category=category.name, prod_detail=prod_detail)