Script SQL para referencia | No es ejecutable
Tabla: usuarios
- id (PK, AUTO_INCREMENT)
- dni (UNIQUE)
- nombres
- apellidos 
- password_hash
- fecha_registro
- ultimo_acceso
- estado (activo/inactivo)

Tabla: discapacidades
- id (PK, AUTO_INCREMENT)
- nombre
- descripcion

Tabla: usuario_discapacidad
- id (PK, AUTO_INCREMENT)
- usuario_id (FK)
- discapacidad_id (FK)
- otra_descripcion (para tipos no listados)

Tabla: preferencias
- id (PK, AUTO_INCREMENT)
- nombre
- descripcion

Tabla: usuario_preferencia
- id (PK, AUTO_INCREMENT)
- usuario_id (FK)
- preferencia_id (FK)

Tabla: actividades
- id (PK, AUTO_INCREMENT)
- nombre
- descripcion
- fecha
- ubicacion
- cupo_maximo
- estado (activa/cancelada/completa)
- organizacion
- imagen  # Ruta de imagen
- compatibilidad # Valor entre 0 y 100
- nivel_accesibilidad

Tabla: participaciones
- id (PK, AUTO_INCREMENT)
- usuario_id (FK)
- actividad_id (FK)
- estado (registrado/confirmado/asistió/no asistió)
- fecha_registro
