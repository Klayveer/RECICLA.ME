from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/servicos", tags=["Serviços"])

@router.post("/")
def criar(servico: schemas.ServicoCreate, db: Session = Depends(database.get_db)):
    novo = models.Servico(**servico.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar(db: Session = Depends(database.get_db)):
    return db.query(models.Servico).all()

@router.get("/{id}")
def buscar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Servico).get(id)
    if not registro:
        raise HTTPException(404, "Serviço não encontrado")
    return registro

@router.put("/{id}")
def atualizar(id: int, dados: schemas.ServicoCreate, db: Session = Depends(database.get_db)):
    registro = db.query(models.Servico).get(id)
    if not registro:
        raise HTTPException(404, "Serviço não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    db.refresh(registro)
    return registro

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Servico).get(id)
    if not registro:
        raise HTTPException(404, "Serviço não encontrado")
    db.delete(registro)
    db.commit()
    return {"mensagem": "Serviço deletado com sucesso"}
