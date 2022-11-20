from flask import render_template, redirect, Blueprint, request, session, url_for, flash, current_app
from src import create_app, db
from src.models import Product, Category
from flask_mail import Mail, Message

public_bp = Blueprint('public', __name__)

def send_message(message):
    print(message.get('name'))
    msg = Message(message.get('Contact US'), sender = message.get('email'),
            recipients = ['@gmail.com'],
            body= message.get('message'))  
    Mail.send(msg)

@public_bp.route("/")
@public_bp.route("/home")
def home():
    # prod_data = db.session.query(Product.prod_name, Product.prod_price )
    prod_data =  db.session.query(Product).all()
    # categories = db.session.query(Category).all()
    categories = Category.categories()
    return render_template("home.html", prod_data=prod_data, categories=categories)

@public_bp.route("/contact")
def contact():
    