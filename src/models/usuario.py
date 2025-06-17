from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True)
    permiso = Column(String(50), nullable=False, default="empleado")

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost/gst"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()