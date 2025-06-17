# controllers/mercancia.py
from models.mercancia import Mercancia, session

def obtener_merca():
    try:
        return session.query(Mercancia).all()
    except Exception as e:
        raise Exception(f"Error al obtener mercancia: {str(e)}")

def crear_merca(proveedor, producto, descripcion, precio, fecha):
    nueva_mercancia = Mercancia(
        proveedor=proveedor,
        producto=producto,
        descripcion=descripcion,
        precio=precio,
        fecha=fecha,
        estado=1
    )
    session.add(nueva_mercancia)
    session.commit()
    return nueva_mercancia