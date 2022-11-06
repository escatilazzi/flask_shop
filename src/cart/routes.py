import os
from src import create_app, db
from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import Discount, User, Category, Product, Brand, Cart
from src.admin.forms import AddCategory, AddBrand, AddDiscount, AddProduct
from werkzeug.utils import secure_filename

cart_bp = Blueprint("cart",__name__)

def MagerDicts(dict1,dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1  + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False
    
@cart_bp.route("/addCart", methods=["POST"])
def addCart():
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        product = Product.query.filter_by(prod_id=product_id).first()

        if product_id and quantity and request.method=="POST":
            DictItems= {product_id:{'name':product.prod_name,'price':float(product.prod_price),'quantity':quantity,'image':product.prod_file}}            
            if 'Cart' in session:
                print(session['Cart'])
                if product_id in session['Cart']:
                    print("This product already in your cart")
                    for item in session['Cart'].DictItems():
                        session.modified = True
                        item['quantity'] += 1
                else:
                    session['Cart'] = MagerDicts(session['Cart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Cart'] = DictItems
                return redirect(request.referrer)
            
    except Exception as e:
        print(e)
    finally:
        return redirect(url_for('public.home'))

@cart_bp.route("/cart", methods=["GET","POST"])
def showCart():
    if 'Cart' not in session:
        return redirect(request.referrer)
    subtotal = 0
    total = 0
    for key, product in session['Cart'].items():
        subtotal += float(product['price']) * int(product['quantity'])
        total = float(subtotal)
    return render_template('/cart/cart.html', total=total, subtotal=subtotal)





# @cart_bp.route("/addCart/<int:id>",  methods=["GET","POST"])
# def addCart(id):
#     if current_user.is_anonymous:
#         return redirect(url_for('account.login'))
#     kart = Cart(cart_user_id=current_user.id, cart_product_id=id, cart_quantity=1)
#     db.session.add(kart)
#     db.session.commit()
#     return redirect(url_for('public.home'))

# @cart_bp.route("/cart",  methods=["GET","POST"])
# def show_cart():
#     if current_user.is_anonymous:
#         return redirect(url_for('account.login'))
#     cart_products= db.session.query(Product.prod_name, Product.prod_price, Cart.cart_quantity).join(Cart, Product.prod_id==Cart.cart_id).filter(Cart.cart_user_id)
#     return render_template("/cart/cart.html", cart_products=cart_products)


# @cart_bp.route("/cart/<int:product_id>", methods=["GET","POST"])
# @login_required
# def increase_cart(product_id):
#     qty = db.session.query(Cart.cart_quantity).filter(Cart.cart_product_id == product_id, Cart.cart_user_id == current_user.id).first()
#     inv = Product.query.query(Product.filter(Product.prod_id == product_id).first()
#     while qty < inv:
#         kart.cart_quantity += 1
#         db.session.commit()
#         return redirect(url_for('cart.show_cart'))
#     else:
#         flash("No hay stock")
#         return redirect(url_for("cart.show_Cart"))