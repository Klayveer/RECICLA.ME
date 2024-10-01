import pandas as pd
from sqlalchemy.orm import Session
from . import models, schemas

def get_residuo(db: Session, residuo_id: int):
    return db.query(models.Residuo).filter(models.Residuo.id == residuo_id).first()

def create_residuo(db: Session, residuo: schemas.ResiduoCreate):
    db_residuo = models.Residuo(**residuo.dict())
    db.add(db_residuo)
    db.commit()
    db.refresh(db_residuo)
    return db_residuo

def update_residuo(db: Session, residuo_id: int, residuo: schemas.ResiduoUpdate):
    db_residuo = db.query(models.Residuo).filter(models.Residuo.id == residuo_id).first()
    if db_residuo:
        for key, value in residuo.dict(exclude_unset=True).items():
            setattr(db_residuo, key, value)
        db.commit()
        db.refresh(db_residuo)
    return db_residuo

def delete_residuo(db: Session, residuo_id: int):
    db_residuo = db.query(models.Residuo).filter(models.Residuo.id == residuo_id).first()
    if db_residuo:
        db.delete(db_residuo)
        db.commit()
    return db_residuo

def insert_xlsx_data(db: Session, file_path: str):
    df = pd.read_excel(file_path)
    df.columns = ['Data', 'Tipo_Residuo', 'Peso']
    df['Peso'] = df['Peso'].str.replace(',', '.').astype(float)

    for _, row in df.iterrows():
        db_residuo = models.Residuo(
            data=row['Data'],
            tipo_residuo=row['Tipo_Residuo'],
            peso=row['Peso']
        )
        db.add(db_residuo)
    
    db.commit()
    return {"status": "Dados inseridos com sucesso"}