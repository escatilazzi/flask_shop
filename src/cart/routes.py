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
        print(session['Cart'])
    finally:
        return redirect(url_for('public.home'))

@cart_bp.route("/cart")
def showCart():
    subtotal = 0
    total = 0
    if 'Cart' not in session or len(session['Cart']) <=0:
        empty=1
    else:
        empty=0
        for key, product in session['Cart'].items():
            subtotal += float(product['price']) * int(product['quantity'])
            total = float(subtotal)
    return render_template('/cart/cart.html', total=total, subtotal=subtotal, empty=empty)

@cart_bp.route("/deleteItem/<int:id>",  methods=["POST"])
def deleteItem(id):
    try:
        session.modified=True
        for key, item in session['Cart'].items():
            if int(key) == id:
                session['Cart'].pop(key, None)
                return redirect(url_for('cart.showCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('cart.showCart'))
        
@cart_bp.route("/clearCart")
def clearCart():
    try:
        session.pop('Cart', None)
        return redirect(url_for('public.home'))
    except Exception as e:
        print(e)
    