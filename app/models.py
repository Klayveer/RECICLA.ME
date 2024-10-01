from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Residuo(Base):
    __tablename__ = "residuos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    tipo_residuo = Column(String(255), nullable=False)
    peso = Column(Float, nullable=False)