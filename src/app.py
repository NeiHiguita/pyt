from flask import Flask, redirect, render_template, session, url_for
from views.factura import factura_bp
from views.usuario import usuario_bp
from views.mercancia import mercancia_bp
from views.observacion import observacion_bp
import webview
from threading import Thread
import os

app = Flask(__name__)

# Configurar la clave secreta para las sesiones
app.secret_key = '1015068806'

app.register_blueprint(factura_bp, url_prefix='/api')
app.register_blueprint(mercancia_bp, url_prefix='/api')
app.register_blueprint(observacion_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/usuario')

@app.route('/')
def home():
    if 'usuario_id' in session:  # Verificar si el usuario está autenticado (sesión de Flask)
        from models.usuario import Usuario, session as db_session  # Renombrar la sesión de SQLAlchemy
        usuario = db_session.query(Usuario).filter_by(id=session['usuario_id']).first()
        if usuario:
            return render_template('index.html', usuario=usuario)  # Pasar el usuario a la plantilla
    return redirect(url_for('usuario.login'))  # Redirigir al login si no está autenticado
def start_flask():
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto especificado por Render o 5000 por defecto
    app.run(host="0.0.0.0", port=port, debug=False)
    
if __name__ == '__main__':
    # Ejecutar Flask en un hilo separado
    flask_thread = Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Crear una ventana de escritorio con PyWebview
    webview.create_window("Gestor de Ventas", "http://127.0.0.1:5000")
    webview.start()
