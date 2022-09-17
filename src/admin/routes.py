from locale import currency
import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand
from src.admin.forms import AddCategory, AddBrand, AddDiscount, AddProduct
from werkzeug.utils import secure_filename

admin_bp = Blueprint("admin", __name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin_bp.route('/admin/home')
@admin_required
def home():
    q_users = db.session.query(User.username, User.email, User.created)
    return render_template('admin/home.html', users=q_users)

@admin_bp.route('/admin/addCategory', methods=['GET','POST'])
@admin_required
def addCategory(): 
    form = AddCategory()
    if form.validate_on_submit():
        new_cat = Category(cat_name=form.name.data)
        db.session.add(new_cat)
        db.session.commit()
        flash("Add category successfully")
        return redirect(url_for('admin.adminHome'))
    return render_template("admin/addCategory.html", form=form)


@admin_bp.route('/admin/addBrand', methods=['GET','POST'])
@admin_required
def addBrand(): 
    form = AddBrand()
    if form.validate_on_submit():
        new_brand = Brand(bra_name=form.name.data)
        db.session.add(new_brand)
        db.session.commit()
        flash("Add brand successfully")
        return redirect(url_for('admin.adminHome'))
    return render_template("admin/addBrand.html", form=form)

@admin_bp.route('/admin/addDiscount', methods=['GET','POST'])
@admin_required
def addDiscount(): 
    form = addDiscount()
    if form.validate_on_submit():
        new_disc = Discount(disc_name=form.name.data, disc_percent=form.percent.data)
        db.session.add(new_disc)
        db.session.commit()
        flash("Add discount successfully")
        return redirect(url_for('admin.adminHome'))
    return render_template("admin/addDiscount.html", form=form)

@admin_bp.route('/admin/addProduct', methods=['GET','POST'])
@admin_required
def addProduct():
    form = AddProduct()
    form.category.choices = [(c.cat_id, c.cat_name) for c in Category.query.order_by('cat_name')]
    form.brand.choices = [(b.bra_id, b.bra_name) for b in Brand.query.order_by('bra_name')]
    form.discount.choices = [(d.disc_id, d.disc_percent) for d in Discount.query.order_by('disc_percent')]
    if form.validate_on_submit():
        image = request.files['image']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            #image.save(secure_filename(image.filename))
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        imagename = filename
        new_prod = Product(prod_name=form.name.data, prod_price=form.price.data, prod_desc=form.description.data, prod_category_id=form.category.data, prod_quantity=form.inventory.data, prod_discounts_id=form.discount.data, prod_brand_id=form.brand.data, prod_file=imagename)
        db.session.add(new_prod)
        db.session.commit()
        flash("Add product successfully")
        return redirect(url_for('admin.adminHome'))
    return render_template("admin/addProduct.html", form=form)


@admin_bp.route("/admin/home/delete/<string:user>", methods=['POST','GET'])
@admin_required
def delete_user(user):
    if user == 'Admin':
        flash('Required admin privileges')
    else:
        User.query.filter_by(username=user).delete()
        db.session.commit()
        flash('User : {} deleted'.format(user))

