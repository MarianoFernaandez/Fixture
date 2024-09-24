from pydantic import BaseModel
from typing import List, Optional
from datetime import date

#===================================== T O R N E O S ========================================

class TorneoBase(BaseModel):
    nombre: str
    fechaInicio: Optional[date] = None
    fechaFin: Optional[date] = None
    cantidadEquipos: int

class TorneoCreate(TorneoBase):
    pass

class TorneoUpdate(TorneoBase):
    pass

class Torneo(TorneoBase):
    id: int
    class Config:
        from_attributes = True

#===================================== E Q U I P O S ========================================

class EquipoBase(BaseModel):
    nombre: str
    escudo: Optional[str] = None  # URL o descripción del escudo
    ciudad: Optional[str] = None
    fechaFundacion: Optional[date] = None

class EquipoCreate(EquipoBase):
    pass

class EquipoUpdate(EquipoBase):
    pass

class Equipo(EquipoBase):
    id: int
    jugadores: List['Jugador'] = []
    class Config:
        from_attributes = True

#===================================== J U G A D O R E S ========================================

class JugadorBase(BaseModel):
    apellido: str
    nombre: str
    fechaNacimiento: Optional[date] = None
    posicion: Optional[str] = None  # arquero, defensor, central, delantero
    numeroDeCamiseta: Optional[int] = None
    equipo_id: int

class JugadorCreate(JugadorBase):
    pass

class JugadorUpdate(JugadorBase):
    pass

class Jugador(JugadorBase):
    id: int
    equipo: Equipo
    class Config:
        from_attributes = True

#===================================== R O L E S ========================================

class RolBase(BaseModel):
    rol: str  # titular/capitan, titular, suplente

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    id: int
    class Config:
        from_attributes = True

#===================================== F I X T U R E ========================================

class FixtureBase(BaseModel):
    idTorneo: int

class FixtureCreate(FixtureBase):
    pass

class FixtureUpdate(FixtureBase):
    pass

class Fixture(FixtureBase):
    id: int
    torneo: Torneo
    class Config:
        from_attributes = True

#===================================== F E C H A S ========================================

class FechaBase(BaseModel):
    idFixture: int
    fechaPartido: date

class FechaCreate(FechaBase):
    pass

class FechaUpdate(FechaBase):
    pass

class Fecha(FechaBase):
    id: int
    fixture: Fixture
    class Config:
        from_attributes = True

#===================================== P A R T I D O S ========================================

class PartidoBase(BaseModel):
    idEquipoLocal: int
    idEquipoVisitante: int
    golLocal: Optional[int] = None
    golVisitante: Optional[int] = None

class PartidoCreate(PartidoBase):
    pass

class PartidoUpdate(PartidoBase):
    pass

class Partido(PartidoBase):
    id: int
    equipoLocal: Equipo
    equipoVisitante: Equipo
    class Config:
        from_attributes = True

#===================================== Á R B I T R O S ========================================

class ArbitroBase(BaseModel):
    apyn: str  # Apellido y nombre del árbitro
    idPartido: int

class ArbitroCreate(ArbitroBase):
    pass

class ArbitroUpdate(ArbitroBase):
    pass

class Arbitro(ArbitroBase):
    id: int
    partido: Partido
    class Config:
        from_attributes = True

#===================================== C A N C H A S ========================================

class CanchaBase(BaseModel):
    nombre: str
    ubicacion: Optional[str] = None
    tamaño: str  # F5, F6, F7, F8
    tipoSuperficie: str  # piso, pasto

class CanchaCreate(CanchaBase):
    pass

class CanchaUpdate(CanchaBase):
    pass

class Cancha(CanchaBase):
    id: int
    class Config:
        from_attributes = True
