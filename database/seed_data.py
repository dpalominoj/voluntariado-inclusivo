from models import db, Discapacidad, Preferencia, Actividad
from datetime import datetime, timedelta

peru_tz = timezone(timedelta(hours=-5))

def seed_database():
    """Poblar la base de datos con registros iniciales"""

# Crea organizaciones
if Organizacion.query.count() == 0: #si no existe, crea
    org1 = Organizacion(
        nombre_org="Fundación Inclusión Perú",
        descripcion_org="Organización dedicada a promover la inclusión social de personas con discapacidad",
        direccion_fisica="Av. Arequipa 123, Lima"
    )
    org2 = Organizacion(
        nombre_org="Voluntarios Unidos",
        descripcion_org="Red de voluntarios para causas sociales",
        direccion_fisica="Jr. Huancavelica 456, Lima"
    )
    org3 = Organizacion(
        nombre_org="Manos Solidarias",
        descripcion_org="Ayuda a comunidades vulnerables",
        direccion_fisica="Calle Los Olivos 789, Lima"
    )
db.session.add_all([org1, org2, org3])
db.session.commit()

# Crea discapacidades
if Discapacidad.query.count() == 0:
    disc1 = Discapacidad(nombre="Auditiva", descripcion="Dificultad o imposibilidad de usar el sentido del oído")
    disc2 = Discapacidad(nombre="Visual", descripcion="Dificultad o imposibilidad de usar el sentido de la vista")
    disc3 = Discapacidad(nombre="Motriz", descripcion="Dificultad o imposibilidad de moverse o desplazarse")
db.session.add_all([disc1, disc2, disc3])
db.session.commit()
    
# Crea preferencias
if Preferencia.query.count() == 0:
    pref1 = Preferencia(nombre_corto="Niños", descripcion_detallada="Trabajar con niños")
    pref2 = Preferencia(nombre_corto="Adultos mayores", descripcion_detallada="Trabajar con adultos mayores")
    pref3 = Preferencia(nombre_corto="Animales", descripcion_detallada="Trabajar con animales")
    pref4 = Preferencia(nombre_corto="Educación", descripcion_detallada="Actividades educativas")
    pref5 = Preferencia(nombre_corto="Medio ambiente", descripcion_detallada="Actividades ambientales")
db.session.add_all([pref1, pref2, pref3, pref4, pref5])
db.session.commit()

# Crea facilidades para actividades
if ActividadFacilidad.query.count() == 0:
    facilidad1 = ActividadFacilidad(nombre_facilidad="Rampas", descripcion="Acceso con rampas para sillas de ruedas")
    facilidad2 = ActividadFacilidad(nombre_facilidad="Intérpretes", descripcion="Intérpretes de lengua de señas disponibles")
    facilidad3 = ActividadFacilidad(nombre_facilidad="Material braille", descripcion="Material disponible en sistema braille")
db.session.add_all([facilidad1, facilidad2, facilidad3])
db.session.commit()

# Crea usuarios
if Usuario.query.count() == 0:
    # Administrador
    admin = Usuario(
        DNI="12345678",
        nombre="Juan",
        apellido="Pérez",
        email="admin@inclusivo.com",
        contrasena_hash="hashed_password_123",
        celular="987654321",
        direccion="Av. Principal 123",
        fecha_nacimiento=date(1980, 5, 15),
        genero="masculino",
        perfil="administrador",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
    # Organizadores
    org1 = Usuario(
        DNI="23456789",
        nombre="María",
        apellido="Gómez",
        email="maria@fundacion.org",
        contrasena_hash="hashed_password_234",
        celular="987654322",
        direccion="Av. Libertad 456",
        fecha_nacimiento=date(1985, 7, 20),
        genero="femenino",
        perfil="organizador",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz),
        fk_organizacion=1
    )
    org2 = Usuario(
        DNI="34567890",
        nombre="Carlos",
        apellido="Rodríguez",
        email="carlos@voluntarios.org",
        contrasena_hash="hashed_password_345",
        celular="987654323",
        direccion="Jr. Unión 789",
        fecha_nacimiento=date(1978, 3, 10),
        genero="masculino",
        perfil="organizador",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz),
        fk_organizacion=2
    )
    org3 = Usuario(
        DNI="45678901",
        nombre="Lucía",
        apellido="Fernández",
        email="lucia@manos.org",
        contrasena_hash="hashed_password_456",
        celular="987654324",
        direccion="Av. Sol 1011",
        fecha_nacimiento=date(1990, 11, 25),
        genero="femenino",
        perfil="organizador",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz),
        fk_organizacion=3
    )
    # Voluntarios
    vol1 = Usuario(
        DNI="56789012",
        nombre="Pedro",
        apellido="López",
        email="pedro@email.com",
        contrasena_hash="hashed_password_567",
        celular="987654325",
        direccion="Calle Lima 1213",
        fecha_nacimiento=date(1995, 2, 14),
        genero="masculino",
        perfil="voluntario",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
    vol2 = Usuario(
        DNI="67890123",
        nombre="Ana",
        apellido="Martínez",
        email="ana@email.com",
        contrasena_hash="hashed_password_678",
        celular="987654326",
        direccion="Av. Brasil 1415",
        fecha_nacimiento=date(1992, 8, 30),
        genero="femenino",
        perfil="voluntario",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )    
    vol3 = Usuario(
        DNI="78901234",
        nombre="Jorge",
        apellido="Silva",
        email="jorge@email.com",
        contrasena_hash="hashed_password_789",
        celular="987654327",
        direccion="Jr. Ayacucho 1617",
        fecha_nacimiento=date(1998, 4, 5),
        genero="masculino",
        perfil="voluntario",
        tiene_discapacidad=False,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
    vol4 = Usuario(
        DNI="89012345",
        nombre="Rosa",
        apellido="Quispe",
        email="rosa@email.com",
        contrasena_hash="hashed_password_890",
        celular="987654328",
        direccion="Av. Argentina 1819",
        fecha_nacimiento=date(1993, 6, 12),
        genero="femenino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )    
    vol5 = Usuario(
        DNI="90123456",
        nombre="Luis",
        apellido="Vargas",
        email="luis@email.com",
        contrasena_hash="hashed_password_901",
        celular="987654329",
        direccion="Calle Tacna 2021",
        fecha_nacimiento=date(1987, 9, 18),
        genero="masculino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )    
    vol6 = Usuario(
        DNI="01234567",
        nombre="Carmen",
        apellido="Díaz",
        email="carmen@email.com",
        contrasena_hash="hashed_password_012",
        celular="987654330",
        direccion="Jr. Ica 2223",
        fecha_nacimiento=date(1996, 1, 22),
        genero="femenino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
    vol7 = Usuario(
        DNI="11223344",
        nombre="Miguel",
        apellido="Torres",
        email="miguel@email.com",
        contrasena_hash="hashed_password_112",
        celular="987654331",
        direccion="Av. Bolivia 2425",
        fecha_nacimiento=date(1989, 12, 8),
        genero="masculino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )    
    vol8 = Usuario(
        DNI="22334455",
        nombre="Sofía",
        apellido="Castro",
        email="sofia@email.com",
        contrasena_hash="hashed_password_223",
        celular="987654332",
        direccion="Calle Junín 2627",
        fecha_nacimiento=date(1994, 7, 3),
        genero="femenino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
    vol9 = Usuario(
        DNI="33445566",
        nombre="Roberto",
        apellido="Mendoza",
        email="roberto@email.com",
        contrasena_hash="hashed_password_334",
        celular="987654333",
        direccion="Av. Venezuela 2829",
        fecha_nacimiento=date(1991, 10, 15),
        genero="masculino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )    
    vol10 = Usuario(
        DNI="44556677",
        nombre="Elena",
        apellido="Rojas",
        email="elena@email.com",
        contrasena_hash="hashed_password_445",
        celular="987654334",
        direccion="Jr. Cusco 3031",
        fecha_nacimiento=date(1988, 4, 27),
        genero="femenino",
        perfil="voluntario",
        tiene_discapacidad=True,
        estado_usuario="activo",
        fecha_registro=datetime.now(peru_tz)
    )
db.session.add_all([admin, org1, org2, org3, vol1, vol2, vol3, vol4, vol5, vol6, vol7, vol8, vol9, vol10])
db.session.commit()

# Asignar discapacidades a los voluntarios
    # Discapacidad auditiva
    db.session.add(UsuarioDiscapacidad(id_usuario=4, id_discapacidad=1, gravedad="moderada", apoyo_requerido="interprete"))
    db.session.add(UsuarioDiscapacidad(id_usuario=5, id_discapacidad=1, gravedad="leve", apoyo_requerido="otros"))
    db.session.add(UsuarioDiscapacidad(id_usuario=6, id_discapacidad=1, gravedad="grave", apoyo_requerido="interprete"))
    # Discapacidad visual
    db.session.add(UsuarioDiscapacidad(id_usuario=7, id_discapacidad=2, gravedad="moderada", apoyo_requerido="otros"))
    db.session.add(UsuarioDiscapacidad(id_usuario=8, id_discapacidad=2, gravedad="leve", apoyo_requerido="otros"))
    # Discapacidad motriz
    db.session.add(UsuarioDiscapacidad(id_usuario=9, id_discapacidad=3, gravedad="grave", apoyo_requerido="otros"))
    db.session.add(UsuarioDiscapacidad(id_usuario=10, id_discapacidad=3, gravedad="moderada", apoyo_requerido="otros"))

# Asignar preferencias a usuarios
    #  organizadores
    db.session.add(UsuarioPreferencia(id_usuario=2, id_preferencia=1))
    db.session.add(UsuarioPreferencia(id_usuario=2, id_preferencia=2))
    db.session.add(UsuarioPreferencia(id_usuario=3, id_preferencia=3))
    db.session.add(UsuarioPreferencia(id_usuario=3, id_preferencia=5))
    db.session.add(UsuarioPreferencia(id_usuario=4, id_preferencia=1))
    db.session.add(UsuarioPreferencia(id_usuario=4, id_preferencia=4))
    # voluntarios
    db.session.add(UsuarioPreferencia(id_usuario=5, id_preferencia=2))
    db.session.add(UsuarioPreferencia(id_usuario=6, id_preferencia=3))
    db.session.add(UsuarioPreferencia(id_usuario=7, id_preferencia=1))
    db.session.add(UsuarioPreferencia(id_usuario=8, id_preferencia=4))
    db.session.add(UsuarioPreferencia(id_usuario=9, id_preferencia=5))
    db.session.add(UsuarioPreferencia(id_usuario=10, id_preferencia=2))

# Crear actividades
if Actividad.query.count() == 0:
    actividad1 = Actividad(
        nombre="Taller de lectura inclusiva",
        descripcion="Taller de lectura para personas con discapacidad visual",
        fecha_actividad=datetime(2023, 12, 15, 10, 0),
        ubicacion="Biblioteca Nacional, Lima",
        tipo="presencial",
        habilidades_requeridas="Paciencia, conocimiento básico de braille",
        es_inclusiva=True,
        cupo_maximo=20,
        estado="abierto",
        compatibilidad="A1",
        etiqueta="educación",
        fk_organizacion=1,
        id_facilidad=3  # Material braille
    )    
    actividad2 = Actividad(
        nombre="Charla sobre derechos de personas con discapacidad",
        descripcion="Charla informativa sobre derechos y leyes",
        fecha_actividad=datetime(2023, 12, 20, 15, 0),
        ubicacion="Zoom",
        tipo="virtual",
        habilidades_requeridas="Conocimiento básico de leyes",
        es_inclusiva=True,
        cupo_maximo=50,
        estado="abierto",
        compatibilidad="A2",
        etiqueta="derechos",
        fk_organizacion=2,
        id_facilidad=2  # Intérpretes
    )    
    actividad3 = Actividad(
        nombre="Jornada de limpieza de playas accesible",
        descripcion="Limpieza de playas con accesibilidad para personas con movilidad reducida",
        fecha_actividad=datetime(2024, 1, 10, 8, 0),
        ubicacion="Playa Agua Dulce, Chorrillos",
        tipo="presencial",
        habilidades_requeridas="Conciencia ambiental",
        es_inclusiva=True,
        cupo_maximo=30,
        estado="abierto",
        compatibilidad="A3",
        etiqueta="medio ambiente",
        fk_organizacion=3,
        id_facilidad=1  # Rampas
    )
    ''' actividad4 = Actividad(
                nombre='Taller de Lectura Inclusiva',
                descripcion='Sesiones semanales de lectura accesible con voluntarios oyentes y personas con discapacidad auditiva.',
                fecha_actividad=datetime(2025, 1, 10, 8, 0),
                ubicacion='Lima, Perú',
                cupo_maximo=20,
                estado='activa',
                organizacion='Biblioteca Nacional del Perú',
                imagen='lectura_inclusiva.jpg',
                compatibilidad=85,
                nivel_accesibilidad=5
            ) 
    actividad5 = Actividad(
                nombre='Jornada de Reforestación Accesible',
                descripcion='Actividad ambiental con caminos adaptados para voluntarios con movilidad reducida. Incluye interpretación en lengua de señas.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Cusco, Perú',
                cupo_maximo=30,
                estado='activa',
                organizacion='ONG Verde Esperanza',
                imagen='reforestacion_accesible.jpg',
                compatibilidad=92,
                nivel_accesibilidad=4
            )
    actividad6 = Actividad(
                nombre='Voluntariado en Centro de Rehabilitación Infantil',
                descripcion='Apoyo en juegos y dinámicas inclusivas para niños con discapacidad motriz y cognitiva.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Arequipa, Perú',
                cupo_maximo=15,
                estado='activa',
                organizacion='Fundación Somos Uno',
                imagen='voluntariado_rehabilitacion.jpg',
                compatibilidad=78,
                nivel_accesibilidad=3
            )
    actividad7 = Actividad(
                nombre='Capacitación en Tecnología Asistiva',
                descripcion='Capacitación para el uso de software de accesibilidad, orientado a voluntarios que apoyan a personas con discapacidad visual.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Trujillo, Perú',
                cupo_maximo=25,
                estado='activa',
                organizacion='TecnoInclusión Perú',
                imagen='tecnologia_asistiva.jpg',
                compatibilidad=88,
                nivel_accesibilidad=5
            )
    actividad8 = Actividad(
                nombre='Voluntariado en Comedor Popular',
                descripcion='Apoyo logístico en la preparación y distribución de alimentos en zonas vulnerables. No se requieren adaptaciones especiales.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Callao, Perú',
                cupo_maximo=40,
                estado='activa',
                organizacion='Red de Apoyo Solidario',
                imagen='comedor_popular.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            )
    actividad9 = Actividad(
                nombre='Campaña de Limpieza Costera',
                descripcion='Recojo de residuos sólidos en playas del litoral para proteger el ecosistema marino. Requiere desplazamiento prolongado.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Chorrillos, Lima, Perú',
                cupo_maximo=35,
                estado='activa',
                organizacion='EcoMar Perú',
                imagen='limpieza_costera.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            )
    actividad10 = Actividad(
                nombre='Tutorías Escolares en Zonas Rurales',
                descripcion='Voluntariado presencial para reforzamiento escolar en comunidades rurales. Implica caminatas y acceso limitado a servicios.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Huancavelica, Perú',
                cupo_maximo=10,
                estado='activa',
                organizacion='Educa Rural',
                imagen='tutorias_rurales.jpg',
                compatibilidad=98,
                nivel_accesibilidad=1
            )
    actividad11 = Actividad(
                nombre='Festival Juvenil de Arte Urbano',
                descripcion='Organización y montaje de espacios artísticos para jóvenes. Incluye armado de estructuras y coordinación en campo.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Barranco, Lima, Perú',
                cupo_maximo=20,
                estado='activa',
                organizacion='Colectivo Cultura Viva',
                imagen='arte_urbano.jpg',
                compatibilidad=97,
                nivel_accesibilidad=2
            )
    activida12 = Actividad(
                nombre='Brigada de Emergencia Comunitaria',
                descripcion='Simulacros y talleres sobre primeros auxilios y evacuación ante desastres. Participación física activa requerida.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Chiclayo, Perú',
                cupo_maximo=25,
                estado='activa',
                organizacion='Defensa Civil Joven',
                imagen='brigada_emergencia.jpg',
                compatibilidad=99,
                nivel_accesibilidad=1
            )
    activida13 = Actividad(
                nombre='Pintado de Escuelas en Renovación',
                descripcion='Apoyo en mejora de infraestructura escolar mediante tareas de pintado, limpieza y reparaciones básicas.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Ayacucho, Perú',
                cupo_maximo=30,
                estado='activa',
                organizacion='Manos que Suman',
                imagen='pintado_escuelas.jpg',
                compatibilidad=100,
                nivel_accesibilidad=1
            )
    activida14 = Actividad(
                nombre='Festival Deportivo Inclusivo',
                descripcion='Evento deportivo con actividades adaptadas para voluntarios y participantes con distintas habilidades.',
                fecha_actividad=datetime(2025, 1, 12, 8, 0),
                ubicacion='Piura, Perú',
                cupo_maximo=50,
                estado='activa',
                organizacion='Red Peruana de Deporte Inclusivo',
                imagen='festival_deportivo.jpg',
                compatibilidad=95,
                nivel_accesibilidad=4
            )
    activida15 = Actividad(
                nombre='Apoyo psicológico con señas a adolescentes',
                descripcion='Apoyo emocional a adolescentes en riesgo',
                fecha_actividad=datetime(2025, 3, 12, 8, 0),
                ubicacion='Piura, Perú',
                cupo_maximo=50,
                estado='activa',
                organizacion='Red Peruana de Deporte Inclusivo',
                imagen='festival_deportivo.jpg',
                compatibilidad=95,
                nivel_accesibilidad=4
            ) '''
db.session.add_all([actividad1, actividad2, actividad3])
db.session.commit()

# Asignar discapacidades compatibles con las actividades
    # Taller de lectura (visual)
    db.session.add(ActividadDiscapacidad(id_actividad=1, id_discapacidad=2))    
    # Charla sobre derechos (auditiva)
    db.session.add(ActividadDiscapacidad(id_actividad=2, id_discapacidad=1))    
    # Limpieza de playas (motriz)
    db.session.add(ActividadDiscapacidad(id_actividad=3, id_discapacidad=3))

# Crea inscripciones
    # Voluntarios con discapacidad visual inscritos en taller de lectura
    db.session.add(Inscripcion(id_usuario=7, id_actividad=1, fecha_inscripcion=datetime.now(peru_tz)))
    db.session.add(Inscripcion(id_usuario=8, id_actividad=1, fecha_inscripcion=datetime.now(peru_tz)))    
    # Voluntarios con discapacidad auditiva inscritos en charla
    db.session.add(Inscripcion(id_usuario=4, id_actividad=2, fecha_inscripcion=datetime.now(peru_tz)))
    db.session.add(Inscripcion(id_usuario=5, id_actividad=2, fecha_inscripcion=datetime.now(peru_tz)))
    db.session.add(Inscripcion(id_usuario=6, id_actividad=2, fecha_inscripcion=datetime.now(peru_tz)))    
    # Voluntarios con discapacidad motriz y otros en limpieza de playas
    db.session.add(Inscripcion(id_usuario=9, id_actividad=3, fecha_inscripcion=datetime.now(peru_tz)))
    db.session.add(Inscripcion(id_usuario=10, id_actividad=3, fecha_inscripcion=datetime.now(peru_tz)))
db.session.commit()

