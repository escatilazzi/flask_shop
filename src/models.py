from src import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_name = db.Column(db.String(64))
    usr_email = db.Column(db.String(120))
    usr_fname = db.Column(db.String(600))
    usr_lname = db.Column(db.String(600))
    usr_password_hash = db.Column(db.String(128))
    usr_created = db.Column(db.DateTime())
    usr_modified = db.Column(db.DateTime())


    def __init__(self, email, password):
        self.usr_email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.usr_name)

    def checkPassword(self, password):
        boolPasswordCheck = check_password_hash(self.password_hash, password)
        return boolPasswordCheck

class UserAddress(db.Model):
    __tablename__ = "users_address"

    usra_id = db.Column(db.Integer, primary_key=True)
    usra_usr_id = db.Column(db.Integer, db.ForeignKey('users.usr_id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users_address', lazy=True))
    usra_address = db.Column(db.String(5000))
    usra_city = db.Column(db.String(5000))
    usra_postalcode = db.Column(db.String(5000)) 
    usra_country = db.Column(db.String(5000))
    usra_mobile = db.Column(db.String(600))


class UserPay(db.Model):
    __tablename__ ="users_payments"

    usrp_id = db.Column(db.Integer, primary_key=True)
    usrp_usr_id = db.Column(db.Integer, db.ForeingKey('users.usr_id'), nullable=False)
    user = db.relationship('users', backref=db.backref('users_payments'), lazy=True)
    usrp_payment_type = db.Column(db.Text, nullable=False)
    usrp_provider = db.Column(db.String(30000))
    usrp_account_no = db.Column(db.Integer, unique=True)
    usrp_expired = db.Column(db.Date())


class AdminType(db.Model):
    __tablename__ = "admintypes"    

    adt_id = db.Column(db.Integer, primary_key=True)
    adt_type = db.Column(db.String(1500))
    adt_permissions = db.Column(db.String(30000))
    adt_created = db.Column(db.DateTime)

class Admin(db.Model):
    __tablename__ = "admins"

    adm_id = db.Column(db.Integer, primary_key=True)
    adm_name = db.Column(db.String(60))
    adm_fname = db.Column(db.String(600))
    adm_lname = db.Column(db.String(600))
    adm_password = db.Column(db.String(128))
    adm_type = db.Column(db.Integer, db.ForeingKey())
    type = db.relationship('AdminType', backref=db.backref('admins', lazy=True))
    adm_created = db.Column(db.DateTime())

    def __repr__(self):
        return '<Admin {}>'.format(self.adm_name)

class Product(db.Model):
    __tablename__ = "products"
    
    prod_id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(3000), nullable=False)
    prod_price = db.Column(db.Real, nullable=False)
    prod_desc = db.Column(db.Text, nullable=False) 
    prod_image = db.Column(db.LargeBinary)
    prod_category_id = db.Column(db.Integer, db.ForeingKey('categories.cat_id'))
    category = db.relationship('Category', backref=db.backref('products'), lazy=True)
    prod_inventory_id = db.Column(db.Integer, db.ForeingKey('inventory.inv_id'))
    inventory = db.relationship('inventory', backref=db.backref('products'), lazy=True)
    prod_discounts_id= db.Column(db.Integer, db.ForeingKey('discounts.disc_id'))
    discount = db.relationship('discount', backref=db.backref('products'), lazy=True)
    prod_created = db.Column(db.DateTime)
    prod_modified = db.Column(db.DateTime)
    prod_deleted = db.Column(db.DateTime)


    def __repr__(self):
        return '<Addproduct {}>'.format(self.pro_name)

class Category(db.Model):
    __tablename__ = "categories"

    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(600), unique=True)
    cat_created = db.Column(db.DateTime())
    cat_modified = db.Column(db.DateTime())
    cat_deleted = db.Column(db.DateTime())

    def __init__(self,cat_name):
        self.cat_name = cat_name


class Inventory(db.Model):
    __tablename__ = "inventory"

    inv_id = db.Column(db.Integer(), primary_key=True)
    inv_quantity = db.Column(db.Integer)

class Cart(db.Model):
    __tablename__ = "cart"

    cart_id = db.Column(db.Integer(), primary_key=True)
    cart_session_id = db.Column(db.Integer(), db.ForeingKey('sessions.ords_id'))
    session = db.relationship('sessions', backref=db.backref('cart'), lazy=True)
    cart_product_id = db.Column(db.Integer(), db.ForeingKey('products.prod_id'))
    product = db.relationship('products', backref=db.backref('cart'), lazy=True)
    cart_quantity = db.Column(db.Integer)
    cart_created = db.Column(db.DateTime())


class Order(db.Model):
    __tablename__ = "orders"

    ord_id = db.Column(db.Integer, primary_key=True)
    ord_user_id = db.Column(db.Integer, db.ForeingKey('users.usr_id'), nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    ord_product_id = db.Column(db.Integer, db.ForeingKey('products.prod_id'), nullable=False)
    product = db.relationship('products', backref=db.backref('orders'), lazy=True)
    ord_quantity = db.Column(db.Integer, nullable=False)
    ord_created = db.Column(db.DateTime)
    ord_modified = db.Column(db.DateTime)


class OrderDetail(db.Model):
    __tablename__ = "orders_det"

    orddet_id = db.Column(db.Integer, primary_key=True)
    orddet_user_id = db.Column(db.Integer, db.ForeingKey('users.usr_id'), nullable=False)
    order = db.relationship('orders', backref=db.backref('orders_det', lazy=True))
    orddet_total = db.Column(db.Real, nullable=False)
    orddet_created = db.Column(db.DateTime())
    orddet_modified = db.Column(db.DateTime())

class Session(db.Model):
    __tablename__ = "sessions"

    sess_id = db.Column(db.Integer, primary_key=True)
    sess_users_id = db.Column(db.Integer, db.ForeingKey('users.usr_id'))
    user = db.relationship('users', backref=db.backref('sessions'), lazy=True)
    sess_total = db.Column(db.Real, nullable=False)
    sess_created = db.Column(db.DateTime)
    sess_modified = db.Column(db.DateTime)
    
class Payment(db.Model):
    __tablename__ ="payments"

    pay_id = db.Column(db.Integer, primary_key=True)
    pay_ord_id = db.Column(db.Integer, unique=True)
    pay_amount = db.Column(db.Integer, nullable=False)
    pay_provider = db.Column(db.Text, nullable=False)
    pay_status = db.Column(db.Text, nullable=False)
    pay_created = db.Column(db.DateTime())
    pay_modified = db.Column(db.DateTime())


class Discount(db.Model):
    __tablename__ = "discounts"

    disc_id = db.Column(db.Integer(), primary_key=True)
    disc_name = db.Column(db.Text, unique=True, nullable=False)
    disc_percent = db.Column(db.Real, nullable=False)
    disc_active = db.Column(db.Boolean(), nullable=False)
    disc_created = db.Column(db.DateTime)
    disc_modified = db.Column(db.DateTime)
    disc_deleted = db.Column(db.DateTime)
    
