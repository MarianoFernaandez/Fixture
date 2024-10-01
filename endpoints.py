from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Equipo

router = APIRouter()

@router.get("/equipos/")
def get_equipos(db : Session = Depends(get_db)):
    equipos = db.query(Equipo).all()
    return equipos