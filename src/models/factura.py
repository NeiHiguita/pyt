# models/factura.py
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Factura(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    tipo_proceso = Column(String(50), nullable=False)
    subtotal = Column(Float, nullable=False)
    descripcion = Column(String(255), nullable=True)
    estado = Column(String(50), nullable=False)

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost/gst"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()