Script SQL para referencia | No es ejecutable
-- TABLA: usuarios
-- Contiene los datos personales y de acceso de los usuarios (voluntarios, organizadores, administradores)
Table usuarios (
    id_usuario INT [PK, auto-increment]
    DNI VARCHAR(8) [UNIQUE]
    nombre VARCHAR(100)
    apellido VARCHAR(100)
    email VARCHAR(150) [UNIQUE]
    contrasena_hash VARCHAR(255)
    celular VARCHAR(9)
    direccion TEXT
    fecha_nacimiento DATE
    genero ENUM('masculino', 'femenino', 'prefiero_no_decir')
    perfil ENUM('voluntario', 'organizador', 'administrador')
    tiene_discapacidad BOOLEAN
    estado_usuario ENUM('activo', 'inactivo', 'pendiente')
    fecha_registro TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
    fk_organizacion INT [NULL, FK → organizaciones.id_organizacion]
)

-- TABLA: preferencias
-- Catálogo de preferencias que los usuarios pueden seleccionar
Table preferencias (
    id_preferencia INT [PK, auto-increment]
    nombre_corto VARCHAR(50)
    descripcion_detallada TEXT
)

-- TABLA: usuarios_preferencia
-- Relación muchos a muchos entre usuarios y preferencias
Table usuarios_preferencia (
    id_usuario INT [PK, FK → usuarios.id_usuario]
    id_preferencia INT [PK, FK → preferencias.id_preferencia]
)

-- TABLA: discapacidades
-- Catálogo de discapacidades registradas
Table discapacidades (
    id_discapacidad INT [PK, auto-increment]
    nombre VARCHAR(100) [UNIQUE]
    descripcion TEXT
)

-- TABLA: usuario_discapacidad
-- Relación entre usuario y discapacidad, incluyendo nivel y tipo de apoyo requerido
Table usuario_discapacidad (
    id_usuario INT [FK → usuarios.id_usuario]
    id_discapacidad INT [FK → discapacidades.id_discapacidad]
    gravedad ENUM('leve', 'moderada', 'grave')
    apoyo_requerido ENUM('interprete', 'otros')
    PRIMARY KEY (id_usuario, id_discapacidad)
)

-- TABLA: organizaciones
-- Información de las organizaciones que crean actividades
Table organizaciones (
    id_organizacion INT [PK, auto-increment]
    nombre_org VARCHAR(255)
    descripcion_org TEXT
    direccion_fisica VARCHAR(255)
    logo TEXT
    fecha_registro TIMESTAMP
)

-- TABLA: actividad_facilidad
-- Catálogo de ayudas específicas que pueden ofrecerse en actividades inclusivas
Table actividad_facilidad (
    id_facilidad INT [PK, auto-increment]
    nombre_facilidad VARCHAR(255) [UNIQUE]
    descripcion VARCHAR(255)
)

-- TABLA: actividades
-- Actividades de voluntariado disponibles
Table actividades (
    id_actividad INT [PK, auto-increment]
    nombre VARCHAR(255)
    descripcion TEXT
    fecha_actividad TIMESTAMP
    ubicacion VARCHAR(255)
    tipo ENUM('presencial', 'virtual')
    habilidades_requeridas TEXT
    es_inclusiva BOOLEAN [DEFAULT FALSE]
    cupo_maximo INT
    estado ENUM('abierto', 'cerrado')
    imagen VARCHAR(255)
    compatibilidad VARCHAR(5)
    etiqueta VARCHAR(100) -- ejemplo: 'educacion', 'TIC'
    fk_organizacion INT [FK → organizaciones.id_organizacion]
    id_facilidad INT [FK → actividad_facilidad.id_facilidad]
)

-- TABLA: actividad_discapacidad
-- Actividades diseñadas para tipos específicos de discapacidad
Table actividad_discapacidad (
    id_actividad INT [FK → actividades.id_actividad]
    id_discapacidad INT [FK → discapacidades.id_discapacidad]
    PRIMARY KEY (id_actividad, id_discapacidad)
)

-- TABLA: auditoria_actividad
-- Registro de modificaciones a actividades (auditoría)
Table auditoria_actividad (
    id_auditoria INT [PK, auto-increment]
    id_actividad INT [FK → actividades.id_actividad]
    id_usuario INT [FK → usuarios.id_usuario]
    IP_usuario VARCHAR(45)
    fecha_registro TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: inscripciones
-- Registro de usuarios inscritos en actividades
Table inscripciones (
    id_inscripcion INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    id_actividad INT [FK → actividades.id_actividad]
    fecha_inscripcion TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: notificaciones
-- Mensajes enviados a usuarios desde la plataforma
Table notificaciones (
    id_notificacion INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    mensaje TEXT
    fecha_envio TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
    leida BOOLEAN [DEFAULT FALSE]
    prioridad ENUM('alta', 'media', 'baja')
)

-- TABLA: feedback
-- Evaluaciones realizadas por los usuarios sobre las actividades
Table feedback (
    id_feedback INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    id_actividad INT [FK → actividades.id_actividad]
    puntuacion INT
    comentario TEXT
    fecha TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: recomendaciones
-- Recomendaciones de actividades personalizadas o generales
Table recomendaciones (
    id_recomendacion INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    id_actividad INT [FK → actividades.id_actividad]
    tipo_recomendacion ENUM('P', 'G', 'BP') -- Personalizado, General, Basado en Preferencias
    descripcion TEXT
    fecha TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: tendencias
-- Análisis de popularidad de actividades
Table tendencias (
    id_tendencia INT [PK, auto-increment]
    id_actividad INT [FK → actividades.id_actividad]
    cantidad_participantes INT
    puntuacion_promedio DECIMAL(3,2)
    fecha TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: interacciones_chatbot
-- Registro de interacción entre usuarios y chatbot
Table interacciones_chatbot (
    id_interaccion INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    mensaje_usuario TEXT
    respuesta_chatbot TEXT
    fecha TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)

-- TABLA: analisis_participacion
-- Estadísticas de participación por usuario
Table analisis_participacion (
    id_analisis INT [PK, auto-increment]
    id_usuario INT [FK → usuarios.id_usuario]
    cant_actividades INT
    porcentaje_particip DECIMAL(5,2)
    fecha TIMESTAMP [DEFAULT CURRENT_TIMESTAMP]
)
