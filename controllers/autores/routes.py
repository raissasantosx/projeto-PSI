from flask import request, redirect, url_for, render_template, flash
from database import session
from controllers.autores import autores_bp
import models

@autores_bp.route('/autores')
def listar_autores():
    autores = session.query(models.Autor).all()
    return render_template('autores/listar_autores.html', autores=autores)

@autores_bp.route('/livros_do_autor/<int:autor_id>')
def livros_do_autor(autor_id):
    autor = session.query(models.Autor).get(autor_id)
    if not autor:
        flash("Autor não encontrado")
        return redirect(url_for('autores.listar_autores'))

    return render_template('autores/livros_do_autor.html', autor=autor)
