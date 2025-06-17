# controllers/factura.py
from models.factura import Factura, session

def obtener_facturas():
    try:
        # Ordenar las facturas por fecha en orden descendente
        return session.query(Factura).order_by(Factura.fecha.desc()).all()
    except Exception as e:
        raise Exception(f"Error al obtener facturas: {str(e)}")

def crear_factura(fecha, tipo_proceso, subtotal, descripcion):
    nueva_factura = Factura(
        fecha=fecha,
        tipo_proceso=tipo_proceso,
        subtotal=subtotal,
        descripcion=descripcion,
        estado=1
    )
    session.add(nueva_factura)
    session.commit()
    return nueva_factura

def actualizar_factura(id, **kwargs):
    factura = session.query(Factura).filter_by(id=id).first()
    if factura:
        for key, value in kwargs.items():
            setattr(factura, key, value)
        session.commit()
    return factura

def eliminar_factura(id):
    factura = session.query(Factura).filter_by(id=id).first()
    if factura:
        session.delete(factura)
        session.commit()
    return factura