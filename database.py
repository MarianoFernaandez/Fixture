from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

username = 'root'
password = '454848'
host = '127.0.0.1'
port = '3307' 
# Importante poner el puerto para que SQLalchemy sepa escuchar el servidor (Heidi)
database = 'fixture'

connection_string = (
    f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
)

# Crear una instancia de motor para la base de datos
engine = create_engine(connection_string)
# Crear una clase de sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)
# Base para la creación de modelos de datos
Base = declarative_base()
# Base para la creación de modelos de datos
Base.metadata.create_all(bind=engine)

try:
    with engine.connect() as connection:
        print("Conexión exitosa!")
        # Realiza tus operaciones de base de datos aquí
except Exception as e:
    print(f"Error al conectar: {e}")
