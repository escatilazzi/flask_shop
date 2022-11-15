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
	comments = Comment.query.filter_by(com_product_id=product_id).all()
	if request.method == "POST":
		user_id=current_user.id
		comment = request.form.get('comment')
		new_comment = Comment(com_comment=comment,com_user_id=user_id, com_product_id=product_id )
		db.session.add(new_comment)
		db.session.commit()
		flash("Gracias por dejar tu comentario")
	return render_template("products/product_detail.html", product=product, name=product.prod_name, image=product.prod_file, price=product.prod_price, quantity=product.prod_quantity, category=category, cat_name=category.cat_name, comments=comments)

@product_bp.route("/category/<int:cat_id>", methods=["GET","POST"])
def showCategory(cat_id):
	prod_cat = db.session.query(Product.prod_id, Product.prod_name, Product.prod_file, Product.prod_desc, Product.prod_price, Category.cat_name).join(Category).filter(Product.prod_category_id == cat_id).all()
	category = db.session.query(Category.cat_name).filter_by(cat_id=cat_id).first()
	return render_template("products/category.html", prod_cat=prod_cat, category=category.cat_name)
