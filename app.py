from flask import Flask, render_template
from database import criar_banco
from controllers.auth import auth_bp
from controllers.livros import livros_bp
from controllers.autores import autores_bp

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.register_blueprint(auth_bp)
app.register_blueprint(livros_bp)
app.register_blueprint(autores_bp)

criar_banco()

@app.route('/')
def index():
    return render_template('index.html')
