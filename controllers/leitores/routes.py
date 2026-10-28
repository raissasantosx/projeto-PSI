from flask import request, redirect, url_for, render_template, flash, session as flask_session
from database import session
from controllers.leitores import leitores_bp
from models.models import Autor, Livro, Leitor

@leitores_bp.route('/cadastrar_leitor', methods = ['POST', 'GET'])
def cadastrar_leitor():
    if request.method == 'POST':
       nome = request.form.get('nome')

       if not nome:
           flash('Preencha todos os campos!')
           return render_template('leitores/cadastrar_leitor.html')

       usuario_id = flask_session['usuario_id']
       n_leitor = Leitor(nome=nome, usuario_id=int(usuario_id))
       session.add(n_leitor)
       session.commit()

       flash('Leitor cadastrado.')
       return redirect(url_for('leitores.listar_leitores'))
    return render_template('leitores/cadastrar_leitor.html')

@leitores_bp.route('/leitores')
def listar_leitores():
    leitores = session.query(Leitor).all()
    return render_template('leitores/listar_leitores.html', leitores=leitores)

@leitores_bp.route('/leitores_do_usuario')
def listar_leitores_do_usuario():
    usuario_id = flask_session['usuario_id']
    leitores = session.query(Leitor).filter_by(usuario_id=usuario_id).all()
    return render_template('leitores/listar_leitores.html', leitores=leitores, usuario=usuario_id)

@leitores_bp.route('/livros_do_leitor/<int:leitor_id>')
def livros_emprestados(leitor_id):
    leitor = session.query(Leitor).get(leitor_id)
    if not leitor:
        flash("Leitor não encontrado")
        return redirect(url_for('leitores.listar_leitores'))
    livros = leitor.livros

    return render_template('leitores/livros_emprestados.html', leitor=leitor, livros=livros)

@leitores_bp.route('/editar_leitor/<int:leitor_id>', methods = ['POST', 'GET'])
def editar_leitor(leitor_id):
    leitor = session.query(Leitor).get(leitor_id)
    if not leitor:
        return redirect(url_for('leitores.listar_leitores'))

    if request.method == 'POST':
        nome = request.form.get('nome')

        if nome:
            leitor.nome = nome
            session.commit()
            return redirect(url_for('leitores.listar_leitores'))

        flash('Preencha os campos!')

    return render_template('leitores/editar_leitor.html', leitor=leitor)

@leitores_bp.route('/excluir_leitor/<int:leitor_id>')
def excluir_leitor(leitor_id):
    leitor = session.query(Leitor).get(leitor_id)
    if leitor:
        session.delete(leitor)
        session.commit()
    return redirect(url_for('leitores.listar_leitores'))
