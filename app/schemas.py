from pydantic import BaseModel
from datetime import date
from typing import Optional

class ResiduoBase(BaseModel):
    data: date
    tipo_residuo: str
    peso: float

class ResiduoCreate(ResiduoBase):
    pass

class ResiduoUpdate(ResiduoBase):
    pass

class Residuo(ResiduoBase):
    id: int

    class Config:
        orm_mode = True