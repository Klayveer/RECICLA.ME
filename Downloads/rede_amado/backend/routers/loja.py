from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/loja", tags=["Loja"])

@router.post("/")
def criar(loja: schemas.LojaCreate, db: Session = Depends(database.get_db)):
    novo = models.Loja(**loja.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar(db: Session = Depends(database.get_db)):
    return db.query(models.Loja).all()

@router.get("/{id}")
def buscar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Loja).get(id)
    if not registro:
        raise HTTPException(404, "Loja não encontrada")
    return registro

@router.put("/{id}")
def atualizar(id: int, dados: schemas.LojaCreate, db: Session = Depends(database.get_db)):
    registro = db.query(models.Loja).get(id)
    if not registro:
        raise HTTPException(404, "Loja não encontrada")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    db.refresh(registro)
    return registro

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Loja).get(id)
    if not registro:
        raise HTTPException(404, "Loja não encontrada")
    db.delete(registro)
    db.commit()
    return {"mensagem": "Loja deletada com sucesso"}
