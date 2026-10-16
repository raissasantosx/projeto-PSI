from flask import request, redirect, url_for, render_template
from controllers.auth import auth_bp
import models

@auth_bp.route('/cadastro', methods=['POST', 'GET'])
def cadastrar_usuario():
    pass

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    pass

@auth_bp.route('/logout')
def logout():
    pass