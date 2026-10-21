from flask import request, redirect, url_for, render_template, flash
from controllers.livros import livros_bp
from database import session
from models import Livro, Autor, Leitor

@livros_bp.route('/listar_livros')
def listar_livros():
    livros = session.query(Livro).all()
    return render_template('livros/listar_livros.html', livros=livros)

@livros_bp.route('/cadastrar_livro', methods=['POST', 'GET'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')
        autor_id = request.form.get('autor_id')

        if titulo and ano and autor_id:
            novo_livro = Livro(titulo=titulo, ano=int(ano), autor_id=int(autor_id))
            session.add(novo_livro)
            session.commit()
            return redirect(url_for('livros.listar_livros'))

    autores = session.query(Autor).all()
    return render_template('livros/cadastrar_livro.html', autores=autores)

@livros_bp.route('/editar_livro/<int:id_livro>', methods=['POST', 'GET'])
def editar_livro(id_livro):
    livro = session.query(Livro).get(id_livro)
    
    if not livro:
        flash("Livro não encontrado.")
        return redirect(url_for('livros.listar_livros'))

    if request.method == 'POST':
        livro.titulo = request.form.get('titulo')
        livro.ano = int(request.form.get('ano'))
        livro.autor_id = int(request.form.get('autor_id'))
        
        session.commit()
        return redirect(url_for('livros.listar_livros'))

    autores = session.query(Autor).all()
    return render_template('livros/editar_livro.html', livro=livro, autores=autores)

@livros_bp.route('/remover_livro/<int:id_livro>', methods=['POST'])
def remover_livro(id_livro):
    livro = session.query(Livro).get(id_livro)
    if livro:
        session.delete(livro)
        session.commit()
    return redirect(url_for('livros.listar_livros'))