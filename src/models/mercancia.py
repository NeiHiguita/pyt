# models/mercancia.py
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Mercancia(Base):
    __tablename__ = 'mercancia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    proveedor = Column(String(50), nullable=False)
    producto = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    estado = Column(String(50), nullable=False)

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost/gst"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# # Configuración de la base de datos
# DATABASE_URL = "mysql+pymysql://root:DQxQHzllsrnFCoOrcOpHgUVSHUJaPLHb@maglev.proxy.rlwy.net:27277/railway"
# engine = create_engine(DATABASE_URL)
# Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()

try:
    connection = engine.connect()
    print("✅ ¡Conexión exitosa!")
except Exception as e:
    print("❌ Error al conectar:", e)