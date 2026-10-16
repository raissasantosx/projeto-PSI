from flask import request, redirect, url_for, render_template
from controllers.autores import autores_bp
import models

@autores_bp.route('/autores')
def listar_autores():
    pass

@autores_bp.route('/livros_do_autor/<autor>')
def livros_do_autor(autor):
    pass