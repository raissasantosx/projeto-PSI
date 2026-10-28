from flask import request, redirect, url_for, render_template, flash
from database import session
from controllers.autores import autores_bp
from models.models import Autor, Livro

@autores_bp.route('/cadastrar_autores', methods = ['POST', 'GET'])
def cadastrar_autores():
    if request.method == 'POST':
       nome = request.form.get('nome')
       pais = request.form.get('pais')

       if not nome or not pais:
           flash('Preencha todos os campos!')
           return render_template('autores/cadastrar_autores.html')
       
       autor_cadastrado = session.query(Autor).filter_by(nome=nome).first()
       if autor_cadastrado:
           flash('Esse autor já está cadastrado.')
           return render_template('autores/cadastrar_autores.html')
       
       n_autor = Autor(nome=nome, pais=pais)
       session.add(n_autor)
       session.commit()

       flash('Autor cadastrado.')
       return redirect(url_for('autores.listar_autores'))
    return render_template('autores/cadastrar_autores.html')

@autores_bp.route('/autores')
def listar_autores():
    autores = session.query(Autor).all()
    return render_template('autores/listar_autores.html', autores=autores)

@autores_bp.route('/livros_do_autor/<int:autor_id>')
def livros_do_autor(autor_id):
    autor = session.query(Autor).get(autor_id)
    if not autor:
        flash("Autor não encontrado")
        return redirect(url_for('autores.listar_autores'))
    livros = autor.livros

    return render_template('autores/livros_do_autor.html', autor=autor, livros=livros)

@autores_bp.route('/editar_autor/<int:autor_id>', methods = ['POST', 'GET'])
def editar_autor(autor_id):
    autor = session.query(Autor).get(autor_id)
    if not autor:
        return redirect(url_for('autores.listar_autores'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        pais = request.form.get('pais')

        if nome and pais:
            autor.nome = nome
            autor.pais = pais
            session.commit()
            return redirect(url_for('autores.listar_autores'))

        flash('Preencha os campos!')

    return render_template('autores/editar_autor.html', autor=autor)

@autores_bp.route('/excluir_autor/<int:autor_id>')
def excluir_autor(autor_id):
    autor = session.query(Autor).get(autor_id)
    if autor:
        session.delete(autor)
        session.commit()
    return redirect(url_for('autores.listar_autores'))
