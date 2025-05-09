CREATE TABLE `usuarios` (
  `id_usuario` INT PRIMARY KEY AUTO_INCREMENT,
  `DNI` VARCHAR(8) UNIQUE,
  `nombre` VARCHAR(100),
  `apellido` VARCHAR(100),
  `email` VARCHAR(150) UNIQUE,
  `contrasena_hash` VARCHAR(255),
  `celular` VARCHAR(9),
  `direccion` TEXT,
  `fecha_nacimiento` DATE,
  `genero` ENUM(masculino,femenino,prefiero_no_decir),
  `perfil` ENUM(voluntario,organizador,administrador),
  `tiene_discapacidad` BOOLEAN,
  `estado_usuario` ENUM(activo,inactivo,pendiente),
  `fecha_registro` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `preferencias_voluntario` (
  `id_voluntario` INT PRIMARY KEY,
  `d_preferencias` TEXT,
  `ultimo_update` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `notas_adicionales` TEXT
);

CREATE TABLE `usuario_discapacidad` (
  `id_usuario` INT,
  `id_discapacidad` INT,
  `gravedad` ENUM(leve,moderada,grave),
  `apoyo_requerido` ENUM(interprete,otros),
  `primary` key(id_usuario,id_discapacidad)
);

CREATE TABLE `discapacidades` (
  `id_discapacidad` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) UNIQUE,
  `descripcion` TEXT
);

CREATE TABLE `actividades` (
  `id_actividad` INT PRIMARY KEY AUTO_INCREMENT,
  `titulo` VARCHAR(255),
  `descripcion` TEXT,
  `fecha_actividad` TIMESTAMP,
  `ubicacion` TEXT,
  `tipo` ENUM(presencial,virtual),
  `habilidades_requeridas` TEXT,
  `es_inclusiva` BOOLEAN DEFAULT false,
  `cupo_maximo` INT,
  `estado` ENUM(abierto,cerrado),
  `id_usuario` INT,
  `id_facilidad` INT
);

CREATE TABLE `log_user_actividad` (
  `id_log` INT PRIMARY KEY AUTO_INCREMENT,
  `id_actividad` INT,
  `id_usuario` INT,
  `IP_usuario` VARCHAR(45),
  `fecha_registro` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `actividad_discapacidad` (
  `id_actividad` INT,
  `id_discapacidad` INT,
  `valida_experto` BOOLEAN DEFAULT false,
  `primary` key(id_actividad,id_discapacidad)
);

CREATE TABLE `actividad_facilidad` (
  `id_facilidad` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre_facilidad` VARCHAR(255) UNIQUE,
  `descripcion` VARCHAR(255) UNIQUE
);

CREATE TABLE `inscripciones` (
  `id_inscripcion` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `id_actividad` INT,
  `fecha_inscripcion` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `notificaciones` (
  `id_notificacion` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `mensaje` TEXT,
  `fecha_envio` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `leida` BOOLEAN DEFAULT (FALSE),
  `prioridad` ENUM(alta,media,baja)
);

CREATE TABLE `feedback` (
  `id_feedback` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `id_actividad` INT,
  `puntuacion` INT,
  `comentario` TEXT,
  `fecha` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `recomendaciones` (
  `id_recomendacion` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `id_actividad` INT,
  `tipo_recomendacion` ENUM(P,G,BP),
  `descripcion` TEXT,
  `fecha` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `tendencias` (
  `id_tendencia` INT PRIMARY KEY AUTO_INCREMENT,
  `id_actividad` INT,
  `cantidad_participantes` INT,
  `puntuacion_promedio` DECIMAL(3,2),
  `fecha` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `interacciones_chatbot` (
  `id_interaccion` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `mensaje_usuario` TEXT,
  `respuesta_chatbot` TEXT,
  `fecha` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `analisis_participacion` (
  `id_analisis` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `cant_actividades` INT,
  `porcentaje_particip` DECIMAL(5,2),
  `fecha` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

ALTER TABLE `preferencias_voluntario` ADD FOREIGN KEY (`id_voluntario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `usuario_discapacidad` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `usuario_discapacidad` ADD FOREIGN KEY (`id_discapacidad`) REFERENCES `discapacidades` (`id_discapacidad`);

ALTER TABLE `actividades` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `actividades` ADD FOREIGN KEY (`id_facilidad`) REFERENCES `actividad_facilidad` (`id_facilidad`);

ALTER TABLE `log_user_actividad` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `log_user_actividad` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `actividad_discapacidad` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `actividad_discapacidad` ADD FOREIGN KEY (`id_discapacidad`) REFERENCES `discapacidades` (`id_discapacidad`);

ALTER TABLE `inscripciones` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `inscripciones` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `notificaciones` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `feedback` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `feedback` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `recomendaciones` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `recomendaciones` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `tendencias` ADD FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`);

ALTER TABLE `interacciones_chatbot` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `analisis_participacion` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);
