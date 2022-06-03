from locale import currency
from src import db
from flask import render_template, redirect, Blueprint, session, url_for
from flask_login import current_user, login_required
from src.admin.utils import admin_required
from src.models import User

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/home")
@admin_required
def adminHome():
    data = db.session.query(User.username, User.email, User.created)
    return render_template('admin/home.html', users=data)