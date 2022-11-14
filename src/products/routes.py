import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand, Comment
from src.products.forms import AddComment
from werkzeug.utils import secure_filename

product_bp = Blueprint("product",__name__)


@product_bp.route("/product/<int:product_id>", methods=["GET","POST"])
def product_detail(product_id):
	product = Product.query.filter_by(prod_id=product_id).first()
	category = Category.query.filter_by(cat_id=product.prod_category_id).first()
	return render_template("products/product_detail.html", product=product, name=product.prod_name, image=product.prod_file, price=product.prod_price, quantity=product.prod_quantity, category=category, cat_name=category.cat_name)

@product_bp.route("/category/<int:cat_id>", methods=["GET","POST"])
def showCategory(cat_id):
	prod_cat = db.session.query(Product.prod_id, Product.prod_name, Product.prod_file, Product.prod_desc, Product.prod_price, Category.cat_name).join(Category).filter(Product.prod_category_id == cat_id).all()
	category = db.session.query(Category.cat_name).filter_by(cat_id=cat_id).first()
	return render_template("products/category.html", prod_cat=prod_cat, category=category.cat_name)

@product_bp.route("/product/<int:product_id>/<int:usr_id>/comment", methods=["GET","POST"])
@login_required
def comment(product_id):
	product_id = request.form.get('product_id')
	form = AddComment()
	if form.validate_on_submit():
		user_id=current_user.id
		new_comment = Comment(com_comment=form.comment.data,com_user_id=user_id,com_product_id=product_id )
		db.session.add(new_comment)
		flash("Gracias por dejar tu comentario")
		return redirect(request.referrer)