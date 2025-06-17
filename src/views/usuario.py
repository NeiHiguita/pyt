from flask import Blueprint, request, render_template, redirect, url_for, session
from controllers.usuario import registrar_usuario, autenticar_usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        usuario = autenticar_usuario(correo, password)
        if usuario:
            session['usuario_id'] = usuario.id  # Guardar el ID del usuario en la sesión
            return redirect(url_for('home'))  # Redirigir al index
        else:
            return render_template('usuario/login.html', error="Credenciales incorrectas")
    return render_template('usuario/login.html')

@usuario_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        registrar_usuario(nombre, correo, password)
        return render_template('usuario/registro.html', success=True)  # Pasar indicador de éxito
    return render_template('usuario/registro.html')

@usuario_bp.route('/logout', methods=['GET'])
def logout():
    try:
        # Eliminar la sesión del usuario
        session.pop('usuario_id', None)  # Remover el usuario de la sesión
        return redirect(url_for('usuario.login'))  # Redirigir al login
    except Exception as e:
        return f"Error al cerrar sesión: {str(e)}", 500