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

    # Crear actividades si no existen
    if Actividad.query.count() == 0:
        fecha_base = datetime.now() + timedelta(days=7)
        actividades = [
            Actividad(
                nombre='Taller de Lectura Inclusiva',
                descripcion='Sesiones semanales de lectura accesible con voluntarios oyentes y personas con discapacidad auditiva.',
                fecha=fecha_base,
                ubicacion='Lima, Perú',
                cupo_maximo=20,
                estado='activa',
                organizacion='Biblioteca Nacional del Perú',
                imagen='lectura_inclusiva.jpg',
                compatibilidad=85,
                nivel_accesibilidad=5
            ),
            Actividad(
                nombre='Jornada de Reforestación Accesible',
                descripcion='Actividad ambiental con caminos adaptados para voluntarios con movilidad reducida. Incluye interpretación en lengua de señas.',
                fecha=fecha_base + timedelta(days=3),
                ubicacion='Cusco, Perú',
                cupo_maximo=30,
                estado='activa',
                organizacion='ONG Verde Esperanza',
                imagen='reforestacion_accesible.jpg',
                compatibilidad=92,
                nivel_accesibilidad=4
            ),
            Actividad(
                nombre='Voluntariado en Centro de Rehabilitación Infantil',
                descripcion='Apoyo en juegos y dinámicas inclusivas para niños con discapacidad motriz y cognitiva.',
                fecha=fecha_base + timedelta(days=10),
                ubicacion='Arequipa, Perú',
                cupo_maximo=15,
                estado='activa',
                organizacion='Fundación Somos Uno',
                imagen='voluntariado_rehabilitacion.jpg',
                compatibilidad=78,
                nivel_accesibilidad=3
            ),
            Actividad(
                nombre='Capacitación en Tecnología Asistiva',
                descripcion='Capacitación para el uso de software de accesibilidad, orientado a voluntarios que apoyan a personas con discapacidad visual.',
                fecha=fecha_base + timedelta(days=14),
                ubicacion='Trujillo, Perú',
                cupo_maximo=25,
                estado='activa',
                organizacion='TecnoInclusión Perú',
                imagen='tecnologia_asistiva.jpg',
                compatibilidad=88,
                nivel_accesibilidad=5
            ),
            Actividad(
                nombre='Voluntariado en Comedor Popular',
                descripcion='Apoyo logístico en la preparación y distribución de alimentos en zonas vulnerables. No se requieren adaptaciones especiales.',
                fecha=fecha_base + timedelta(days=5),
                ubicacion='Callao, Perú',
                cupo_maximo=40,
                estado='activa',
                organizacion='Red de Apoyo Solidario',
                imagen='comedor_popular.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            ),
            Actividad(
                nombre='Campaña de Limpieza Costera',
                descripcion='Recojo de residuos sólidos en playas del litoral para proteger el ecosistema marino. Requiere desplazamiento prolongado.',
                fecha=fecha_base + timedelta(days=6),
                ubicacion='Chorrillos, Lima, Perú',
                cupo_maximo=35,
                estado='activa',
                organizacion='EcoMar Perú',
                imagen='limpieza_costera.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            ),
            Actividad(
                nombre='Tutorías Escolares en Zonas Rurales',
                descripcion='Voluntariado presencial para reforzamiento escolar en comunidades rurales. Implica caminatas y acceso limitado a servicios.',
                fecha=fecha_base + timedelta(days=9),
                ubicacion='Huancavelica, Perú',
                cupo_maximo=10,
                estado='activa',
                organizacion='Educa Rural',
                imagen='tutorias_rurales.jpg',
                compatibilidad=98,
                nivel_accesibilidad=1
            ),
            Actividad(
                nombre='Festival Juvenil de Arte Urbano',
                descripcion='Organización y montaje de espacios artísticos para jóvenes. Incluye armado de estructuras y coordinación en campo.',
                fecha=fecha_base + timedelta(days=13),
                ubicacion='Barranco, Lima, Perú',
                cupo_maximo=20,
                estado='activa',
                organizacion='Colectivo Cultura Viva',
                imagen='arte_urbano.jpg',
                compatibilidad=97,
                nivel_accesibilidad=2
            ),
            Actividad(
                nombre='Brigada de Emergencia Comunitaria',
                descripcion='Simulacros y talleres sobre primeros auxilios y evacuación ante desastres. Participación física activa requerida.',
                fecha=fecha_base + timedelta(days=15),
                ubicacion='Chiclayo, Perú',
                cupo_maximo=25,
                estado='activa',
                organizacion='Defensa Civil Joven',
                imagen='brigada_emergencia.jpg',
                compatibilidad=99,
                nivel_accesibilidad=1
            ),
            Actividad(
                nombre='Pintado de Escuelas en Renovación',
                descripcion='Apoyo en mejora de infraestructura escolar mediante tareas de pintado, limpieza y reparaciones básicas.',
                fecha=fecha_base + timedelta(days=17),
                ubicacion='Ayacucho, Perú',
                cupo_maximo=30,
                estado='activa',
                organizacion='Manos que Suman',
                imagen='pintado_escuelas.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            ),
            Actividad(
                nombre='Festival Deportivo Inclusivo',
                descripcion='Evento deportivo con actividades adaptadas para voluntarios y participantes con distintas habilidades.',
                fecha=fecha_base + timedelta(days=21),
                ubicacion='Piura, Perú',
                cupo_maximo=50,
                estado='activa',
                organizacion='Red Peruana de Deporte Inclusivo',
                imagen='festival_deportivo.jpg',
                compatibilidad=95,
                nivel_accesibilidad=4
            )
        ]
    db.session.add_all(actividades)
    db.session.commit()

