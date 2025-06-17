# views/mercancia.py
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from controllers.mercancia import obtener_merca

mercancia_bp = Blueprint('mercancia', __name__)

def login_requerido(func):
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@mercancia_bp.route('/mercancia/html', methods=['GET'])
@login_requerido
def listar_mercancia_html():
    try:
        mercancia = obtener_merca()
        return render_template('mercancia/mercancia.html', mercancia=mercancia)
    except Exception as e:
        return f"Error: {str(e)}", 500