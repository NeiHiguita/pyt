from models.usuario import Usuario, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
import bcrypt

def registrar_usuario(nombre, correo, password):
    try:
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, password=hashed_password, permiso ="empleado")
        session.add(nuevo_usuario)
        session.commit()
        return nuevo_usuario
    except IntegrityError:
        session.rollback()
        raise ValueError("El correo ya está registrado. Por favor, utiliza otro correo.")

def autenticar_usuario(correo, password):
    usuario = session.query(Usuario).filter_by(correo=correo).first()
    if usuario:
        if usuario.password.startswith("$2b$") or usuario.password.startswith("$2a$"):
            if bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
                return usuario
        else:
            if check_password_hash(usuario.password, password):
                return usuario
    return None