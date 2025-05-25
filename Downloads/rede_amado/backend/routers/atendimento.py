from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])

@router.post("/")
def criar(at: schemas.AtendimentoCreate, db: Session = Depends(database.get_db)):
    novo = models.Atendimento(**at.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar(db: Session = Depends(database.get_db)):
    return db.query(models.Atendimento).all()

@router.get("/{id}")
def buscar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Atendimento).get(id)
    if not registro:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return registro

@router.put("/{id}")
def atualizar(id: int, dados: schemas.AtendimentoCreate, db: Session = Depends(database.get_db)):
    registro = db.query(models.Atendimento).get(id)
    if not registro:
        raise HTTPException(status_code=404, detail="Não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    db.refresh(registro)
    return registro

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Atendimento).get(id)
    if not registro:
        raise HTTPException(status_code=404, detail="Não encontrado")
    db.delete(registro)
    db.commit()
    return {"mensagem": "Deletado com sucesso"}
