from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Atendimento(Base):
    __tablename__ = "atendimentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    tipo = Column(String)
    mensagem = Column(Text)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    tipo = Column(String)

class Loja(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(Text)
    preco = Column(String)
    categoria = Column(String)
    imagem = Column(String)

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    conteudo = Column(Text)

class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    mensagem = Column(Text)

class Servico(Base):
    __tablename__ = "servicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(Text)
