from models.models import Autor, Livro, Leitor, Usuario
from sqlalchemy import select

def popular_banco(session):
    if session.scalar(select(Usuario).limit(1)):
        return
    
    usuario = Usuario(login="admin@admin", senha="123")
    session.add(usuario)
    session.flush()

    autor1 = Autor(nome="Romerito", pais="Brasil", usuario_id=usuario.id)
    autor2 = Autor(nome="Hugo", pais="Estados Unidos", usuario_id=usuario.id)
    autor3 = Autor(nome="Ciro", pais="Espanha", usuario_id=usuario.id)

    livro1 = Livro(titulo="Dart", ano=2026, autor=autor3, usuario_id=usuario.id)
    livro2 = Livro(titulo="Flutter", ano=2000, autor=autor3, usuario_id=usuario.id)
    livro3 = Livro(titulo="Flask", ano=1900, autor=autor1, usuario_id=usuario.id)
    livro4 = Livro(titulo="SQLAlchemy", ano=2076, autor=autor1, usuario_id=usuario.id)
    livro5 = Livro(titulo="MySQL", ano=1800, autor=autor2, usuario_id=usuario.id)
    livro6 = Livro(titulo="JavaScript", ano=2027, autor=autor2, usuario_id=usuario.id)

    leitor1 = Leitor(nome="Ana", usuario_id=usuario.id, livros=[livro1, livro3, livro4])
    leitor2 = Leitor(nome="Bruno", usuario_id=usuario.id, livros=[livro2, livro5])
    leitor3 = Leitor(nome="Carla", usuario_id=usuario.id, livros=[livro1, livro6])

    session.add_all([
        autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6, leitor1, leitor2, leitor3,
    ])

    session.commit()