from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload
from fastapi import HTTPException


username = 'root'
password = '454848'
host = '127.0.0.1'
port = '3307' 
# Importante poner el puerto para que SQLalchemy sepa escuchar el servidor
database = 'fixture'

connection_string = (
    f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
)

engine = create_engine(connection_string)

Base = declarative_base()

"""
try:
    with engine.connect() as connection:
        print("Conexión exitosa!")
        # Realiza tus operaciones de base de datos aquí
except Exception as e:
    print(f"Error al conectar: {e}")
"""