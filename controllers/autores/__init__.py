from flask import Blueprint

autores_bp = Blueprint("autores", __name__, template_folder="templates")

from controllers.autores import routes