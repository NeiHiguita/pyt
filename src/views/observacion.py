# views/mercancia.py
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from controllers.observacion import obtener_ob

observacion_bp = Blueprint('observacion', __name__)

def login_requerido(func):
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@observacion_bp.route('/observacion/html', methods=['GET'])
@login_requerido
def listar_observacion_html():
    try:
        observacion = obtener_ob()
        return render_template('observacion/observacion.html', observacion=observacion)
    except Exception as e:
        return f"Error: {str(e)}", 500