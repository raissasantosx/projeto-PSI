from flask import request, redirect, url_for, render_template, flash, session as flask_session
from werkzeug.security import generate_password_hash, check_password_hash
from controllers.auth import auth_bp
from database import session
from models.models import Usuario

@auth_bp.route('/cadastro', methods=['POST', 'GET'])
def cadastrar_usuario():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        if not login or not senha:
            flash("Preencha os campos")
            return redirect(url_for('auth.cadastrar_usuario'))

        usuario_cadastrado = session.query(Usuario).filter_by(login=login).first()
        if usuario_cadastrado:
            flash("O usuário já existe!")
            return redirect(url_for('auth.cadastrar_usuario'))

        senha = generate_password_hash(senha)

        novo_usuario = Usuario(login=login, senha=senha)
        session.add(novo_usuario)
        session.commit()

        flash("Cadastro realizado!")
        return redirect(url_for('auth.login'))
    
    return render_template('auth/cadastro.html')
        
@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        usuario = session.query(Usuario).filter_by(login=login).first()

        if usuario and check_password_hash(usuario.senha, senha):
            flask_session['usuario_id'] = usuario.id
            flask_session['usuario_login'] = usuario.login
            return redirect(url_for('index'))
        else:
            flash("Usuário ou senha incorreto(s)")
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    flask_session.clear()
    flash("Logout realizado com sucesso.")
    return redirect(url_for('index'))
