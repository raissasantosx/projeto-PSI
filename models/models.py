from sqlalchemy import ForeignKey, String, JSON, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from typing import List

tabela_associativa = Table(
    "tabela_associativa",
    Base.metadata,
    Column("livro_id", ForeignKey("livros.id"), primary_key=True),
    Column("leitor_id", ForeignKey("leitores.id"), primary_key=True),
)

class Autor(Base):

    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(unique=True)
    pais: Mapped[str]

    livros: Mapped[List["Livro"]] = relationship(back_populates="autor")

class Livro(Base):

    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str]
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    autor: Mapped["Autor"] = relationship(back_populates="livros")
    leitores: Mapped[List["Leitor"]] = relationship(secondary=tabela_associativa, back_populates="livros")

class Leitor(Base):

    __tablename__ = "leitores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80))

    livros: Mapped[List["Livro"]] = relationship(secondary=tabela_associativa, back_populates="leitores")

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(80), unique=True)
    senha: Mapped[str] = mapped_column(String(200))
