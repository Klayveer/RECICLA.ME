from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/blog", tags=["Blog"])

@router.post("/")
def criar(blog: schemas.BlogPostCreate, db: Session = Depends(database.get_db)):
    novo = models.Blog(**blog.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar(db: Session = Depends(database.get_db)):
    return db.query(models.Blog).all()

@router.get("/{id}")
def buscar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Blog).get(id)
    if not registro:
        raise HTTPException(404, "Blog não encontrado")
    return registro

@router.put("/{id}")
def atualizar(id: int, dados: schemas.BlogPostCreate, db: Session = Depends(database.get_db)):
    registro = db.query(models.Blog).get(id)
    if not registro:
        raise HTTPException(404, "Blog não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    db.refresh(registro)
    return registro

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(database.get_db)):
    registro = db.query(models.Blog).get(id)
    if not registro:
        raise HTTPException(404, "Blog não encontrado")
    db.delete(registro)
    db.commit()
    return {"mensagem": "Blog deletado com sucesso"}
