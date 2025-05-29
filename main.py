from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

from models import db, Usuario, Organizacion, Preferencia, UsuarioPreferencia, Discapacidad, UsuarioDiscapacidad, ActividadFacilidad, Actividad, \
                   ActividadDiscapacidad, AuditoriaActividad, Inscripcion, Notificacion, Feedback, Recomendacion, Tendencia, InteraccionChatbot, AnalisisParticipacion
from database.seed_data import seed_database

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', '968875239')    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///konectai.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)
    Migrate(app, db)
    
    with app.app_context():
        db.drop_all()  # Add this line
        db.create_all()
        try:
            seed_database()
        except Exception as e:
            print(f"Error al poblar la base de datos: {e}")
    return app

app = create_app()

# --- Rutas de Navegación Estándar ---
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route('/participar')
def participar():
    flash('¡Funcionalidad no disponible por el momento!<br>Estamos trabajando arduamente para brindarte la mejor experiencia.', 'info')
    return redirect(url_for('inicio'))

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

# --- Rutas de Registro ---
@app.route('/registro', methods=['POST'])
def registro():
    # Recuperar variables de formulario registro
    nombre = request.form.get('nombre') 
    dni = request.form.get('dni')
    perfil = 'voluntario'
    tiene_discapacidad_str = request.form.get('accs')
    discapacidad_ids = request.form.getlist('disc[]')
    preferencia_ids = request.form.getlist('pref[]')
    passw1 = request.form.get('passw1')
    passw2 = request.form.get('psw2')

    # Validación de contraseñas
    if passw1 != passw2:
        flash('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.', 'error')
        return redirect(url_for('inicio'))
    
    # Verificar existencia de DNI
    if Usuario.query.filter_by(DNI=dni).first():
        flash('El DNI ya está registrado. Por favor, inicie sesión o utilice otro DNI.', 'error')
        return redirect(url_for('inicio'))
    
    # Crear nuevo usuario
    hashed_password = generate_password_hash(passw1)
    nuevo_usuario = Usuario(
        DNI=dni,
        nombre=nombre,
        contrasena_hash=hashed_password,
        perfil=perfil,
        tiene_discapacidad=(tiene_discapacidad_str == 'si'),
        estado_usuario='activo'
    )
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    # Añadir discapacidades seleccionadas
    if nuevo_usuario.tiene_discapacidad and discapacidad_ids:
        for disc_name in discapacidad_ids:
            discapacidad = Discapacidad.query.filter_by(nombre=disc_name).first()
            if discapacidad:
                # Evitar duplicados
                if not UsuarioDiscapacidad.query.filter_by(id_usuario=nuevo_usuario.id_usuario, id_discapacidad=discapacidad.id_discapacidad).first():
                    usuario_discapacidad = UsuarioDiscapacidad(
                        id_usuario=nuevo_usuario.id_usuario,
                        id_discapacidad=discapacidad.id_discapacidad,
                        gravedad='moderada',
                        apoyo_requerido='otros'
                    )
                    db.session.add(usuario_discapacidad)

    # Añadir preferencias seleccionadas
    if preferencia_ids:
        for pref_name in preferencia_ids:
            preferencia = Preferencia.query.filter_by(nombre_corto=pref_name).first()
            if preferencia:
                # Evitar duplicados
                if not UsuarioPreferencia.query.filter_by(id_usuario=nuevo_usuario.id_usuario, id_preferencia=preferencia.id_preferencia).first():
                    usuario_preferencia = UsuarioPreferencia(
                        id_usuario=nuevo_usuario.id_usuario,
                        id_preferencia=preferencia.id_preferencia
                    )
                    db.session.add(usuario_preferencia)
    
    try:
        db.session.commit()
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('inicio'))
    except Exception as e:
        db.session.rollback()
        flash(f'Ocurrió un error al registrar: {e}. Por favor, inténtelo de nuevo.', 'error')
        print(f"Error al registrar usuario: {e}")
        return redirect(url_for('inicio'))

# --- Rutas de Autenticación ---
@app.route('/login', methods=['POST'])
def login():
    dni_o_email = request.form.get('usuario')
    contraseña = request.form.get('contraseña')
    
    usuario = Usuario.query.filter_by(DNI=dni_o_email).first()
    if usuario and check_password_hash(usuario.contrasena_hash, contraseña):
        # Guardar información en la sesión
        session['usuario_id'] = usuario.id_usuario
        session['usuario_dni'] = usuario.DNI
        session['usuario_nombre_completo'] = f"{usuario.nombre} {usuario.apellido}"
        session['usuario_perfil'] = usuario.perfil
        
        flash(f'¡Bienvenido, {usuario.nombre}!', 'success')
        
        # Redirigir según el perfil
        if usuario.perfil == 'voluntario':
            return redirect(url_for('voluntario'))
        elif usuario.perfil == 'organizador':
            return redirect(url_for('dashboard_organizador'))
        elif usuario.perfil == 'administrador':
            return redirect(url_for('dashboard_administrador'))
        else:
            return redirect(url_for('dashboard'))
    else:
        flash('DNI o contraseña incorrectos. Por favor, inténtelo de nuevo.', 'error')
        return redirect(url_for('inicio'))
      
@app.route('/logout')
def logout():
    session.clear()
    flash('¡Sesión cerrada correctamente!', 'success')
    return redirect(url_for('inicio'))

# fallback si no se especifica el perfil
@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        flash('Debe iniciar sesión para acceder.', 'error')
        return redirect(url_for('inicio'))
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        flash('Usuario no encontrado. Por favor, inicie sesión de nuevo.', 'error')
        session.clear()
        return redirect(url_for('inicio'))
    # Si el perfil está en la sesión
    if 'usuario_perfil' in session:
        perfil = session['usuario_perfil']
        if perfil == 'voluntario':
            return redirect(url_for('voluntario'))
        elif perfil == 'organizador':
            return redirect(url_for('dashboard_organizador'))
        elif perfil == 'administrador':
            return redirect(url_for('dashboard_administrador'))
    flash('Su perfil no tiene un dashboard asignado.', 'warning')
    return redirect(url_for('inicio'))

@app.route('/dashboard/voluntario')
def voluntario():
    if 'usuario_id' not in session or session.get('usuario_perfil') != 'voluntario':
        flash('Acceso denegado. Debe iniciar sesión como voluntario.', 'error')
        return redirect(url_for('inicio'))
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    # Obtener actividades en las que el usuario está inscrito
    inscripciones = Inscripcion.query.filter_by(id_usuario=usuario_id).all()
    actividades_inscritas = [inscripcion.actividad for inscripcion in inscripciones if hasattr(inscripcion, 'actividad') and inscripcion.actividad]
    
    # Obtener discapacidades del usuario
    discapacidades_usuario = UsuarioDiscapacidad.query.filter_by(id_usuario=usuario_id).all()
    discapacidades = [Discapacidad.query.get(du.id_discapacidad) for du in discapacidades_usuario]
    
    # Obtener preferencias del usuario
    preferencias_usuario = UsuarioPreferencia.query.filter_by(id_usuario=usuario_id).all()
    preferencias = [Preferencia.query.get(pu.id_preferencia) for pu in preferencias_usuario]
    
    # Obtener actividades disponibles (estado 'abierto', limit 10, order by fecha_actividad desc)
    actividades_disponibles = Actividad.query.filter_by(estado='abierto').order_by(Actividad.fecha_actividad.desc()).limit(10).all()
    
    return render_template(
        'dashboard/voluntario.html',
        usuario=usuario,
        actividades_inscritas=actividades_inscritas,
        discapacidades=discapacidades,
        preferencias=preferencias,
        actividades_disponibles=actividades_disponibles
    )

@app.route('/dashboard/organizador')
def dashboard_organizador():
    if 'usuario_id' not in session or session.get('usuario_perfil') != 'organizador':
        flash('Acceso denegado. Debe iniciar sesión como organizador.', 'error')
        return redirect(url_for('inicio'))
    
    usuario = Usuario.query.get(session['usuario_id'])
    if usuario and usuario.fk_organizacion:
        organizacion = Organizacion.query.get(usuario.fk_organizacion)
        actividades_organizacion = Actividad.query.filter_by(fk_organizacion=organizacion.id_organizacion).all()
        return render_template('dashboard/organizador.html', organizacion=organizacion, actividades=actividades_organizacion)
    else:
        flash('No estás asociado a ninguna organización.', 'warning')
        return render_template('dashboard/organizador.html', organizacion=None, actividades=[])

@app.route('/dashboard/administrador')
def dashboard_administrador():
    if 'usuario_id' not in session:
        flash('Debe iniciar sesión para acceder.', 'error')
        return redirect(url_for('inicio'))
    
    if session.get('usuario_perfil') != 'administrador':
        flash('Acceso restringido: Solo para administradores.', 'error')
        return redirect(url_for('inicio'))
    
    try:
        total_usuarios = Usuario.query.count()
        total_organizaciones = Organizacion.query.count()
        total_actividades = Actividad.query.count()
        # Si no existe fecha_creacion, usa fecha_actividad para actividades recientes
        ultimas_actividades = Actividad.query.order_by(Actividad.fecha_actividad.desc()).limit(5).all()
        nuevos_usuarios = Usuario.query.order_by(Usuario.fecha_registro.desc()).limit(5).all()
        return render_template(
            'dashboard/administrador.html',
            total_usuarios=total_usuarios,
            total_organizaciones=total_organizaciones,
            total_actividades=total_actividades,
            ultimas_actividades=ultimas_actividades,
            nuevos_usuarios=nuevos_usuarios
        )
    except Exception as e:
        flash(f'Error al cargar el dashboard: {str(e)}', 'error')
        return redirect(url_for('inicio'))

# --- Rutas de Actividades ---
@app.route('/actividades_filtradas')
@app.route('/actividades')
def actividades_filtradas():
    tipo_filtro = request.args.get('tipo')
    accesibilidad_filtro = request.args.get('accesibilidad')
    busqueda_texto = request.args.get('busqueda')

    query = Actividad.query

    if tipo_filtro and tipo_filtro != '':
        query = query.filter_by(tipo=tipo_filtro)
    if accesibilidad_filtro and accesibilidad_filtro != '':
        if accesibilidad_filtro == 'inclusiva':
            query = query.filter_by(es_inclusiva=True)
        elif accesibilidad_filtro == 'no_inclusiva':
            query = query.filter_by(es_inclusiva=False)
    if busqueda_texto:
        query = query.filter(
            (Actividad.nombre.ilike(f'%{busqueda_texto}%')) |
            (Actividad.descripcion.ilike(f'%{busqueda_texto}%'))
        )
    # Si tienes relación con organización definida, puedes cargarla con joinedload
    # from sqlalchemy.orm import joinedload
    # todas_actividades = query.options(joinedload(Actividad.organizacion)).all()
    todas_actividades = query.all()

    return render_template('actividades.html',
                           actividades=todas_actividades,
                           current_tipo=tipo_filtro,
                           current_accesibilidad=accesibilidad_filtro,
                           current_busqueda=busqueda_texto)

# Ruta para inscribirse a una actividad
@app.route('/inscribir_actividad/<int:actividad_id>', methods=['POST'])
def inscribir_actividad(actividad_id):
    if 'usuario_id' not in session:
        flash('Debe iniciar sesión para inscribirse.', 'error')
        return redirect(url_for('inicio'))
    usuario_id = session['usuario_id']
    actividad = Actividad.query.get(actividad_id)
    if not actividad:
        flash('La actividad no existe.', 'error')
        return redirect(url_for('actividades_filtradas'))
    # Verificar si el usuario ya está inscrito 
    inscripcion_existente = Inscripcion.query.filter_by(
        id_usuario=usuario_id,
        id_actividad=actividad_id
    ).first()
    if inscripcion_existente:
        flash('¡Ya estás inscrito en esta actividad!', 'info')
        return redirect(url_for('voluntario'))
    current_inscripciones = Inscripcion.query.filter_by(id_actividad=actividad_id).count()
    if actividad.cupo_maximo and current_inscripciones >= actividad.cupo_maximo:
        flash('¡Lo sentimos! El cupo para esta actividad está completo.', 'error')
        return redirect(url_for('actividades_filtradas'))
    try:
        fecha_inscripcion = datetime.utcnow()
        nueva_inscripcion = Inscripcion(
            id_usuario=usuario_id,
            id_actividad=actividad_id,
            fecha_inscripcion=fecha_inscripcion
        )
        db.session.add(nueva_inscripcion)
        db.session.commit()
        flash(f'¡Te has inscrito correctamente a la actividad: {actividad.nombre}!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Ocurrió un error al inscribirte: {e}. Por favor, inténtelo de nuevo.', 'error')
        print(f"Error al inscribir usuario a actividad: {e}")
    return redirect(url_for('voluntario'))

if __name__ == "__main__":
    app.run(debug=True)
