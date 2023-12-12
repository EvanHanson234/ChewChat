from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from .models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    # Register new user
    pass

@auth.route('/login', methods=['POST'])
def login():
    # Login user
    pass

@auth.route('/logout')
@login_required
def logout():
    # Logout user
    pass
