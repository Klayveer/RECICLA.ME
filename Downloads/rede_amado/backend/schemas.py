from pydantic import BaseModel, EmailStr
from typing import Optional


# === ATENDIMENTO ===
class AtendimentoBase(BaseModel):
    nome: str
    email: EmailStr
    tipo: str
    mensagem: str

class AtendimentoCreate(AtendimentoBase):
    pass

class Atendimento(AtendimentoBase):
    id: int

    class Config:
        orm_mode = True


# === USUÁRIO / VOLUNTÁRIO ===
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    tipo: str  # Ex: "voluntário", "público", etc.

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True


# === PRODUTO (Loja) ===
class LojaBase(BaseModel):
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem: Optional[str]

class LojaCreate(LojaBase):
    pass

class Loja(LojaBase):
    id: int

    class Config:
        orm_mode = True


# === BLOG / EVENTOS ===
class BlogPostBase(BaseModel):
    titulo: str
    conteudo: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int

    class Config:
        orm_mode = True


# === CONTATO ===
class ContatoBase(BaseModel):
    nome: str
    email: EmailStr
    mensagem: str

class ContatoCreate(ContatoBase):
    pass

class Contato(ContatoBase):
    id: int

    class Config:
        orm_mode = True


# === SERVIÇO (jurídico, psicológico, saúde...) ===
class ServicoBase(BaseModel):
    nome: str
    descricao: str

class ServicoCreate(ServicoBase):
    pass

class Servico(ServicoBase):
    id: int

    class Config:
        orm_mode = True
