from flask import Blueprint

autores_bp = Blueprint("autores", __name__, template_folder="templates", static_folder='static', static_url_path='/autores/static')

from controllers.autores import routes