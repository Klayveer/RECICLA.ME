from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
import shutil

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/upload-xlsx/")
async def upload_xlsx(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    try:
        result = crud.insert_xlsx_data(db=db, file_path=file_location)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo XLSX: {str(e)}")

@app.post("/residuos/", response_model=schemas.Residuo)
def create_residuo(residuo: schemas.ResiduoCreate, db: Session = Depends(get_db)):
    return crud.create_residuo(db=db, residuo=residuo)

@app.get("/residuos/{residuo_id}", response_model=schemas.Residuo)
def read_residuo(residuo_id: int, db: Session = Depends(get_db)):
    db_residuo = crud.get_residuo(db=db, residuo_id=residuo_id)
    if db_residuo is None:
        raise HTTPException(status_code=404, detail="Resíduo não encontrado")
    return db_residuo

@app.put("/residuos/{residuo_id}", response_model=schemas.Residuo)
def update_residuo(residuo_id: int, residuo: schemas.ResiduoUpdate, db: Session = Depends(get_db)):
    db_residuo = crud.update_residuo(db=db, residuo_id=residuo_id, residuo=residuo)
    if db_residuo is None:
        raise HTTPException(status_code=404, detail="Resíduo não encontrado")
    return db_residuo

@app.delete("/residuos/{residuo_id}", response_model=schemas.Residuo)
def delete_residuo(residuo_id: int, db: Session = Depends(get_db)):
    db_residuo = crud.delete_residuo(db=db, residuo_id=residuo_id)
    if db_residuo is None:
        raise HTTPException(status_code=404, detail="Resíduo não encontrado")
    return db_residuo