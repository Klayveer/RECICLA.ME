from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/contato", tags=["Contato"])

@router.post("/")
def criar(contato: schemas.ContatoCreate, db: Session = Depends(database.get_db)):
    novo = models.Contato(**contato.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar(db: Session = Depends(database.get_db)):
    return db.query(models.Contato).all()

@router.get("/{id}")
def buscar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Contato).get(id)
    if not registro:
        raise HTTPException(404, "Contato não encontrado")
    return registro

@router.put("/{id}")
def atualizar(id: int, dados: schemas.ContatoCreate, db: Session = Depends(database.get_db)):
    registro = db.query(models.Contato).get(id)
    if not registro:
        raise HTTPException(404, "Contato não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    db.refresh(registro)
    return registro

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Contato).get(id)
    if not registro:
        raise HTTPException(404, "Contato não encontrado")
    db.delete(registro)
    db.commit()
    return {"mensagem": "Contato deletado com sucesso"}
