from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta

peru_tz = timezone(timedelta(hours=-5))
fecha_peru = datetime.now(peru_tz)

db = SQLAlchemy()

class Organizacion(db.Model):
    __tablename__ = 'organizaciones'
    id_organizacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_org = db.Column(db.String(255))
    descripcion_org = db.Column(db.Text)
    direccion_fisica = db.Column(db.String(255))
    logo = db.Column(db.Text)
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(peru_tz))

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DNI = db.Column(db.String(8), unique=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    contrasena_hash = db.Column(db.String(255))
    celular = db.Column(db.String(9))
    direccion = db.Column(db.Text)
    fecha_nacimiento = db.Column(db.Date)
    genero = db.Column(db.Enum('masculino', 'femenino', 'prefiero_no_decir'))
    perfil = db.Column(db.Enum('voluntario', 'organizador', 'administrador'))
    tiene_discapacidad = db.Column(db.Boolean)
    estado_usuario = db.Column(db.Enum('activo', 'inactivo', 'pendiente'))
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(peru_tz))
    fk_organizacion = db.Column(db.Integer, db.ForeignKey('organizaciones.id_organizacion'))

class Preferencia(db.Model):
    __tablename__ = 'preferencias'
    id_preferencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_corto = db.Column(db.String(50))
    descripcion_detallada = db.Column(db.Text)

class UsuarioPreferencia(db.Model):
    __tablename__ = 'usuarios_preferencia'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_preferencia = db.Column(db.Integer, db.ForeignKey('preferencias.id_preferencia'), primary_key=True)

class Discapacidad(db.Model):
    __tablename__ = 'discapacidades'
    id_discapacidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), unique=True)
    descripcion = db.Column(db.Text)

class UsuarioDiscapacidad(db.Model):
    __tablename__ = 'usuario_discapacidad'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_discapacidad = db.Column(db.Integer, db.ForeignKey('discapacidades.id_discapacidad'), primary_key=True)
    gravedad = db.Column(db.Enum('leve', 'moderada', 'grave'))
    apoyo_requerido = db.Column(db.Enum('interprete', 'otros'))

class ActividadFacilidad(db.Model):
    __tablename__ = 'actividad_facilidad'
    id_facilidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_facilidad = db.Column(db.String(255), unique=True)
    descripcion = db.Column(db.String(255))

class Actividad(db.Model):
    __tablename__ = 'actividades'
    id_actividad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    fecha_actividad = db.Column(db.DateTime)
    ubicacion = db.Column(db.String(255))
    tipo = db.Column(db.Enum('presencial', 'virtual'))
    habilidades_requeridas = db.Column(db.Text)
    es_inclusiva = db.Column(db.Boolean, default=False)
    cupo_maximo = db.Column(db.Integer)
    estado = db.Column(db.Enum('abierto', 'cerrado'))
    imagen = db.Column(db.String(255))
    compatibilidad = db.Column(db.Integer)
    etiqueta = db.Column(db.String(100))
    fk_organizacion = db.Column(db.Integer, db.ForeignKey('organizaciones.id_organizacion'))
    organizacion = db.relationship('Organizacion', backref='actividades', lazy=True) #agregado
    id_facilidad = db.Column(db.Integer, db.ForeignKey('actividad_facilidad.id_facilidad'))

class ActividadDiscapacidad(db.Model):
    __tablename__ = 'actividad_discapacidad'
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'), primary_key=True)
    id_discapacidad = db.Column(db.Integer, db.ForeignKey('discapacidades.id_discapacidad'), primary_key=True)

class AuditoriaActividad(db.Model):
    __tablename__ = 'auditoria_actividad'
    id_auditoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    IP_usuario = db.Column(db.String(45))
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(peru_tz))

class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'
    id_inscripcion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'))
    usuario = db.relationship('Usuario', backref='inscripciones', lazy=True) #agregado
    actividad = db.relationship('Actividad', backref='inscripciones', lazy=True) #agregado
    fecha_inscripcion = db.Column(db.DateTime, default=datetime.utcnow)

class Notificacion(db.Model):
    __tablename__ = 'notificaciones'
    id_notificacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    mensaje = db.Column(db.Text)
    fecha_envio = db.Column(db.DateTime, default=datetime.utcnow)
    leida = db.Column(db.Boolean, default=False)
    prioridad = db.Column(db.Enum('alta', 'media', 'baja'))

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id_feedback = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'))
    puntuacion = db.Column(db.Integer)
    comentario = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class Recomendacion(db.Model):
    __tablename__ = 'recomendaciones'
    id_recomendacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'))
    tipo_recomendacion = db.Column(db.Enum('P', 'G', 'BP'))
    descripcion = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class Tendencia(db.Model):
    __tablename__ = 'tendencias'
    id_tendencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividades.id_actividad'))
    cantidad_participantes = db.Column(db.Integer)
    puntuacion_promedio = db.Column(db.Numeric(3,2))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class InteraccionChatbot(db.Model):
    __tablename__ = 'interacciones_chatbot'
    id_interaccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    mensaje_usuario = db.Column(db.Text)
    respuesta_chatbot = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class AnalisisParticipacion(db.Model):
    __tablename__ = 'analisis_participacion'
    id_analisis = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    cant_actividades = db.Column(db.Integer)
    porcentaje_particip = db.Column(db.Numeric(5,2))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
