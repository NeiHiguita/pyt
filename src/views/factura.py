# views/factura.py
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from controllers.factura import obtener_facturas, crear_factura, actualizar_factura, eliminar_factura

factura_bp = Blueprint('factura', __name__)

def login_requerido(func):
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# vista para listar facturas 
@factura_bp.route('/facturas/html', methods=['GET'])
@login_requerido
def listar_facturas_html():
    try:
        # Renombrar la sesión de SQLAlchemy para evitar conflictos
        from models.usuario import Usuario, session as db_session
        usuario = db_session.query(Usuario).filter_by(id=session['usuario_id']).first()

        # Obtener las facturas ordenadas por fecha
        facturas = obtener_facturas()

        # Pasar el usuario y las facturas a la plantilla
        return render_template('factura/facturas.html', facturas=facturas, usuario=usuario)
    except Exception as e:
        return f"Error: {str(e)}", 500

# vista para crear una nueva factura    
@factura_bp.route('/facturas/nueva', methods=['GET'])
@login_requerido
def formulario_nueva_factura():
    return render_template('factura/nueva_factura.html')

# vista para crear una nueva factura desde el formulario
@factura_bp.route('/facturas/nueva', methods=['POST'])
@login_requerido
def crear_factura_formulario():
    try:
        from models.usuario import Usuario, session as db_session
        usuario = db_session.query(Usuario).filter_by(id=session['usuario_id']).first()

        # Obtener los datos del formulario
        fecha = request.form['fecha']
        tipo_proceso = request.form['tipo_proceso']
        subtotal = float(request.form['subtotal'])
        descripcion = request.form.get('descripcion', None)

        # Crear la factura usando el controlador
        nueva_factura = crear_factura(fecha, tipo_proceso, subtotal, descripcion)
        return redirect(url_for('factura.listar_facturas_html', usuario = usuario))  # Redirigir al listado de facturas
    except Exception as e:
        return f"Error al crear la factura: {str(e)}", 500
