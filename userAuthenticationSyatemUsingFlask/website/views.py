from flask import Blueprint, render_template
#Blueprint means a overall description of the app/thing. Here all the routes, except for authentication routes will be present.
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint("views", __name__)

@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)