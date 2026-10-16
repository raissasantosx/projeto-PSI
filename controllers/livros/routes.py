from flask import request, redirect, url_for, render_template
from controllers.livros import livros_bp
import models

@livros_bp.route('/listar_livros')
def listar_livros():
    pass

@livros_bp.route('/cadastrar_livro', methods=['POST', 'GET'])
def cadastrar_livro():
    pass

@livros_bp.route('/editar_livro', methods=['POST', 'GET'])
def cadastrar_livro():
    pass

@livros_bp.route('/remover_livro')
def remover_livro():
    pass

