from flask import Blueprint

leitores_bp = Blueprint("leitores", __name__, template_folder="templates", static_folder='static', static_url_path='/leitores/static')

from controllers.leitores import routes