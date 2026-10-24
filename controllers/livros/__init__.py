from flask import Blueprint

livros_bp = Blueprint("livros", __name__, template_folder="templates", static_folder='static', static_url_path='/livros/static')

from controllers.livros import routes