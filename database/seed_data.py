from models import db, Discapacidad, Preferencia, Actividad
from datetime import datetime, timedelta

def seed_database():
    """Poblar la base de datos con datos iniciales"""
    
    # Crear discapacidades si no existen
    if Discapacidad.query.count() == 0:
        discapacidades = [
            Discapacidad(nombre='visual', descripcion='Limitación en percepción óptica'),
            Discapacidad(nombre='auditiva', descripcion='Dificultad en la comprensión de sonido'),
            Discapacidad(nombre='motriz', descripcion='Dificultad en la movilidad física'),
            Discapacidad(nombre='cognitiva', descripcion='Limitación en proceso de aprendizaje')
        ]
        db.session.add_all(discapacidades)
    
    # Crear preferencias si no existen
    if Preferencia.query.count() == 0:
        preferencias = [
            Preferencia(nombre='a_comunitario', descripcion='Apoyo comunitario'),
            Preferencia(nombre='tecnologia', descripcion='Tecnología'),
            Preferencia(nombre='deporte', descripcion='Eventos deportivos'),
            Preferencia(nombre='m_ambiente', descripcion='Medio ambiente'),
            Preferencia(nombre='educacion', descripcion='Educación')
        ]
        db.session.add_all(preferencias)
    
    # Crear algunas actividades de ejemplo si no existen
    if Actividad.query.count() == 0:
        fecha_base = datetime.now() + timedelta(days=7)
        actividades = [
            Actividad(
                nombre='Taller de Inclusión Digital',
                descripcion='Aprende a utilizar herramientas digitales para personas con diversas discapacidades',
                fecha=fecha_base + timedelta(days=1),
                ubicacion='Centro Cultural de Huancayo',
                cupo_maximo=25,
                estado='activa'
            ),
            Actividad(
                nombre='Reforestación en el Parque Nacional',
                descripcion='Ayuda a plantar árboles nativos en zonas deforestadas',
                fecha=fecha_base + timedelta(days=6),
                ubicacion='Parque Nacional Huaytapallana',
                cupo_maximo=40,
                estado='activa'
            ),
            Actividad(
                nombre='Visita a Residencia de Adultos Mayores',
                descripcion='Comparte tiempo de calidad con adultos mayores',
                fecha=fecha_base + timedelta(days=11),
                ubicacion='Residencia San Vicente, Huancayo',
                cupo_maximo=15,
                estado='activa'
            )
        ]
        db.session.add_all(actividades)
    
    db.session.commit()
