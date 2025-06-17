# controllers/observacion.py
from models.observacion import Observacion, session

def obtener_ob():
    try:
        return session.query(Observacion).all()
    except Exception as e:
        raise Exception(f"Error al obtener mercancia: {str(e)}")

def crear_merca(observaciont, fecha):
    nueva_observacion = Observacion(
        observacion = observaciont,
        fecha=fecha,
    )
    session.add(nueva_observacion)
    session.commit()
    return nueva_observacion