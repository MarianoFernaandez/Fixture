from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base, Session
from database import Base

#---Torneos---

class Torneo(Base):
    __tablename__ = 'torneos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    fechaInicio = Column(DateTime)
    fechaFin = Column(DateTime)
    cantidadEquipos = Column(Integer, CheckConstraint('cantidadEquipos IN (8, 10, 12, 14, 16)'))
    
    # Relación 1 a 1 con Fixture
    fixture = relationship("Fixture", back_populates="torneo", uselist=False)

     # Métodos CRUD
    @classmethod
    def create(cls, session: Session, **kwargs):
        new_torneo = cls(**kwargs)
        session.add(new_torneo)
        session.commit()
        session.refresh(new_torneo)
        return new_torneo

    @classmethod
    def read(cls, session: Session, torneo_id: int):
        return session.query(cls).filter(cls.id == torneo_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit() 

#---Equipos---

class Equipo(Base):
    __tablename__ = 'equipos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    escudo = Column(String(255))  # Puede ser una URL o imagen
    ciudad = Column(String(100))
    fechaFundacion = Column(DateTime)
    
    # Relación 1 a muchos con Jugadores
    jugadores = relationship("Jugador", back_populates="equipo")

    # Métodos CRUD
    @classmethod
    def create(cls, session: Session, **kwargs):
        new_equipo = cls(**kwargs)
        session.add(new_equipo)
        session.commit()
        session.refresh(new_equipo)
        return new_equipo

    @classmethod
    def read(cls, session: Session, equipo_id: int):
        return session.query(cls).filter(cls.id == equipo_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit() 

#---Jugadores---

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apellido = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    fechaNacimiento = Column(DateTime)
    posicion = Column(Enum('arquero', 'defensor', 'central', 'delantero', name='posicion_enum'))
    numeroDeCamiseta = Column(Integer)
    equipo_id = Column(Integer, ForeignKey('equipos.id'))
    
    # Relación con Equipos
    equipo = relationship("Equipo", back_populates="jugadores")
    
    # Asegurar que el número de camiseta sea único por equipo
    __table_args__ = (UniqueConstraint('numeroDeCamiseta', 'equipo_id', name='uq_numero_camiseta_equipo'),)

    # Métodos CRUD
    @classmethod
    def create(cls, session: Session, **kwargs):
        new_jugador = cls(**kwargs)
        session.add(new_jugador)
        session.commit()
        session.refresh(new_jugador)
        return new_jugador

    @classmethod
    def read(cls, session: Session, jugador_id: int):
        return session.query(cls).filter(cls.id == jugador_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit() 

#---Roles---

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(Enum('titular/capitan', 'titular', 'suplente', name='rol_enum'))

    # Métodos CRUD
    @classmethod
    def create(cls, session: Session, **kwargs):
        new_rol = cls(**kwargs)
        session.add(new_rol)
        session.commit()
        session.refresh(new_rol)
        return new_rol

    @classmethod
    def read(cls, session: Session, rol_id: int):
        return session.query(cls).filter(cls.id == rol_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit() 

#---Fixture---

class Fixture(Base):
    __tablename__ = 'fixture'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTorneo = Column(Integer, ForeignKey('torneos.id'))
    
    # Relación 1 a 1 con Torneos
    torneo = relationship("Torneo", back_populates="fixture")
    
    # Relación 1 a muchos con Fechas
    fechas = relationship("Fecha", back_populates="fixture")

#---Fechas---

class Fecha(Base):
    __tablename__ = 'fechas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idFixture = Column(Integer, ForeignKey('fixture.id'))
    fechaPartido = Column(DateTime, nullable=False)
    
    # Relación con Fixture
    fixture = relationship("Fixture", back_populates="fechas")
    
    # Relación 1 a muchos con Partidos
    partidos = relationship("Partido", back_populates="fecha")

#---Partidos---

class Partido(Base):
    __tablename__ = 'partidos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEquipoLocal = Column(Integer, ForeignKey('equipos.id'))
    idEquipoVisitante = Column(Integer, ForeignKey('equipos.id'))
    golLocal = Column(Integer)
    golVisitante = Column(Integer)
    
    # Relación con Fechas
    fecha_id = Column(Integer, ForeignKey('fechas.id'))
    fecha = relationship("Fecha", back_populates="partidos")
    
    # Relación con Equipos
    equipoLocal = relationship("Equipo", foreign_keys=[idEquipoLocal])
    equipoVisitante = relationship("Equipo", foreign_keys=[idEquipoVisitante])

    # Relación con Árbitro
    arbitro = relationship("Arbitro", back_populates="partido", uselist=False)

#---Arbitros---

class Arbitro(Base):
    __tablename__ = 'arbitros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apyn = Column(String(200))
    idPartido = Column(Integer, ForeignKey('partidos.id'))
    
    # Relación con Partidos
    partido = relationship("Partido", back_populates="arbitro", uselist=False)

#---Canchas---

class Cancha(Base):
    __tablename__ = 'canchas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(255))
    tamaño = Column(Enum('F5', 'F6', 'F7', 'F8', name='tamano_enum'))
    tipoSuperficie = Column(Enum('piso', 'pasto', name='tipo_superficie_enum'))
