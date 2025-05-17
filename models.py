from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

# Tabla asociativa para usuario_discapacidad
usuario_discapacidad = db.Table('usuario_discapacidad',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True),
    db.Column('discapacidad_id', db.Integer, db.ForeignKey('discapacidades.id'), primary_key=True)
)

# Tabla asociativa para usuario_preferencia
usuario_preferencia = db.Table('usuario_preferencia',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True),
    db.Column('preferencia_id', db.Integer, db.ForeignKey('preferencias.id'), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    ultimo_acceso = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(20), default='activo')
    
    # Relaciones
    discapacidades = db.relationship('Discapacidad', secondary=usuario_discapacidad, 
                                     backref=db.backref('usuarios', lazy='dynamic'))
    preferencias = db.relationship('Preferencia', secondary=usuario_preferencia, 
                                   backref=db.backref('usuarios', lazy='dynamic'))
    participaciones = db.relationship('Participacion', backref='usuario', lazy=True)

    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Usuario {self.nombres} {self.apellidos}>'

class Discapacidad(db.Model):
    __tablename__ = 'discapacidades'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Discapacidad {self.nombre}>'

class Preferencia(db.Model):
    __tablename__ = 'preferencias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Preferencia {self.nombre}>'

class Actividad(db.Model):
    __tablename__ = 'actividades'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    organizacion = db.Column(db.String(100), nullable=True)
    imagen = db.Column(db.String(255), nullable=True)  # Ruta de imagen
    compatibilidad = db.Column(db.Integer, nullable=True)  # Porcentaje
    nivel_accesibilidad = db.Column(db.Integer, nullable=True)
    fecha = db.Column(db.DateTime, nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    cupo_maximo = db.Column(db.Integer, nullable=True)
    estado = db.Column(db.String(20), default='activa')
    
    
    # Relaciones
    participaciones = db.relationship('Participacion', backref='actividad', lazy=True)
    
    def __repr__(self):
        return f'<Actividad {self.nombre}>'

class Participacion(db.Model):
    __tablename__ = 'participaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividades.id'), nullable=False)
    estado = db.Column(db.String(20), default='registrado')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Participacion {self.usuario_id} en {self.actividad_id}>'
