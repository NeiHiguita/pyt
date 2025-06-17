# models/mercancia.py
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Observacion(Base):
    __tablename__ = 'observacion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    observaciont = Column(String(255), nullable=True)
    fecha = Column(Date, nullable=False)

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost/gst"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()