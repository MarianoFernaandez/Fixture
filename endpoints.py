from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Equipo
from fastapi.responses import HTMLResponse
import os
from models import VistaEquiposEstadisticas  # Asegúrate de que este modelo esté bien importado
from database import SessionLocal

router = APIRouter()

@router.get("/vista-equipos/")
async def get_vista_equipos():
    db: Session = SessionLocal()
    vista_equipos = db.query(VistaEquiposEstadisticas).all()

    # Reemplazar None por 0
    for equipo in vista_equipos:
        equipo.GolesAFavor = equipo.GolesAFavor if equipo.GolesAFavor is not None else 0
        equipo.GolesEnContra = equipo.GolesEnContra if equipo.GolesEnContra is not None else 0
        equipo.DiferenciaDeGoles = equipo.DiferenciaDeGoles if equipo.DiferenciaDeGoles is not None else 0

    return vista_equipos


# Endpoint para servir la página HTML
@router.get("/pagina/", response_class=HTMLResponse)
async def get_pagina():
    file_path = os.path.join("static", "index.html")  # Cambia "index.html" si tu archivo tiene otro nombre
    with open(file_path, "r") as f:
        return f.read()