from operator import index
from turtle import back
from src import login_manager , db, create_app
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_user import UserManager

@login_manager.user_loader
def load_user(usr_id):
    return User.query.get(int(usr_id))

class User(UserMixin,db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(256), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    roles = db.relationship("Role", secondary="user_roles", viewonly=True)
    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        boolPasswordCheck = check_password_hash(self.password_hash, password)
        return boolPasswordCheck


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    user = relationship("User", secondary="user_roles", viewonly=True)
    
    def __repr__(self):
        return '<Role {}>'.format(self.name)

class UserRoles(db.Model):
    __tablename__='user_roles'
    role_id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    role= db.relationship('Role', backref=backref('user_roles', cascade="all, delete-orphan"))
    user= db.relationship('User', backref=backref('user_roles', cascade="all, delete-orphan"))

class Product(db.Model):
    __tablename__ = "product"
    
    prod_id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(3000), nullable=False)
    prod_price = db.Column(db.DECIMAL(10, 2), nullable=False)
    prod_desc = db.Column(db.Text, nullable=False) 
    prod_quantity = db.Column(db.Integer, nullable=False)
    prod_category_id = db.Column(db.Integer, db.ForeignKey('categories.cat_id'))
    prod_file = db.Column(db.Text)
    image = db.relationship('Image', backref=db.backref('image'), lazy='dynamic')
    category = db.relationship('Category', backref=db.backref('product'), lazy=True)
    prod_discounts_id= db.Column(db.Integer, db.ForeignKey('discounts.disc_id'))
    discount = db.relationship('Discount', backref=db.backref('product'), lazy=True)
    prod_created = db.Column(db.DateTime, default=datetime.utcnow())
    prod_modified = db.Column(db.DateTime, default=datetime.utcnow())
    prod_deleted = db.Column(db.DateTime, default=datetime.utcnow())
    prod_brand_id = db.Column(db.Integer, db.ForeignKey('brands.bra_id'))
    brand = db.relationship('Brand', backref=db.backref('product'), lazy=True)

    def __repr__(self):
        return f"Product('{self.prod_id}','{self.prod_name}','{self.prod_price}','{self.prod_desc}','{self.prod_quantity}','{self.prod_discounts_id}'"

class Category(db.Model):
    __tablename__ = "categories"

    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(600), unique=True)
    cat_created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self,cat_name):
        self.cat_name = cat_name


class Discount(db.Model):
    __tablename__ = "discounts"

    disc_id = db.Column(db.Integer(), primary_key=True)
    disc_name = db.Column(db.Text, unique=True, nullable=False)
    disc_percent = db.Column(db.Float, nullable=False)
    disc_active = db.Column(db.Boolean(), nullable=False)
    disc_created = db.Column(db.DateTime, default=datetime.utcnow())
    disc_modified = db.Column(db.DateTime, default=datetime.utcnow())
    disc_deleted = db.Column(db.DateTime, default=datetime.utcnow())

class Brand(db.Model):
    __tablename__ = "brands"

    bra_id= db.Column(db.Integer(), primary_key=True)
    bra_name= db.Column(db.Text(), unique=True, index=True)
    bra_date= db.Column(db.DateTime, default=datetime.utcnow())

class Image(db.Model):
    __tablename__ = "image"
    img_id = db.Column(db.Integer(), primary_key=True)
    img_file = db.Column(db.Text)
    img_product_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))

class Cart(db.Model):
    __tablename__ = "cart"

    cart_id = db.Column(db.Integer, primary_key=True)
    cart_product_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('cart'), lazy=True)
    cart_user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('cart', lazy=True))
    cart_quantity = db.Column(db.Integer)
    cart_created = db.Column(db.DateTime, default=datetime.now )

    def __repr__(self):
        return f"Cart('{self.cart_user_id},'{self.cart_product_id}','{self.cart_quantity}')"

class Order(db.Model):
    __tablename__ = "order"

    ord_id = db.Column(db.Integer, primary_key=True)
    ord_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('order', lazy=True))
    ord_product_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('order'), lazy=True)
    ord_quantity = db.Column(db.Integer(), nullable=False)
    ord_total = db.Column(db.Integer())
    ord_country = db.Column(db.String(300))
    ord_city = db.Column(db.String(300))
    ord_address = db.Column(db.String(300))
    ord_phone = db.Column(db.String(300))
    ord_email = db.Column(db.String(300))
    ord_payment_method = db.Column(db.String(300))
    ord_start_pay_date = db.Column(db.DateTime)
    ord_create_order_date = db.Column(db.DateTime)
    ord_finish_pay_date = db.Column(db.DateTime)


class Comment(db.Model):
    __tablename__= "comment"

    com_id = db.Column(db.Integer, primary_key=True)
    com_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment', lazy=True))
    com_comment = db.Column(db.String(5000))
    com_product_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))
    product = db.relationship('Product', backref=db.backref('comment', lazy=True))
    com_create_date = db.Column(db.DateTime)