from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import db, Usuario, Discapacidad, Preferencia, Actividad, Participacion
from database.seed_data import seed_database

def create_app():
    app = Flask(__name__)
    app.secret_key = '852456'    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///konectai.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)
    Migrate(app, db)
    
    with app.app_context():
        db.create_all()
        try:
            seed_database()
        except Exception as e:
            print(f"Error al poblar la base de datos: {e}")
    
    # Eliminar si no usas routes.py
    # from routes import register_routes
    # register_routes(app)

    return app

app = create_app()

# Ruta principal
@app.route("/")
def inicio():
    return render_template("inicio.html")
    
#Ruta participar (mensaje inhabilitado)    
@app.route('/participar')
def participar():
    flash('No disponible por el momento<br>ya que me encuentro<br>programando a full', 'error')
    return redirect(url_for('inicio'))

# Ruta de registro
@app.route('/registro', methods=['POST'])
def registro():
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    dni = request.form.get('dni')
    passw1 = request.form.get('passw1')
    passw2 = request.form.get('psw2')
    acceso_discapacidad = request.form.get('accs')     # Checkbox valor del radio
    discapacidad_ids = request.form.getlist('disc[]')  # Si marcó alguna discapacidad
    otras_discap = request.form.get('otra_discap')     # Si escribe otra discapacidad
    preferencia_ids = request.form.getlist('pref[]')   # Preferencias marcadas
    
    # Validación de contraseñas
    if passw1 != passw2:
        flash('Las contraseñas no coinciden <br> intente nuevamente', 'error')
        return redirect(url_for('inicio'))
    
    # Verificar si el DNI ya existe
    usuario_existente = Usuario.query.filter_by(dni=dni).first()
    if usuario_existente:
        flash('El DNI ya está registrado <br> intente con otro o inicie sesión', 'error')
        return redirect(url_for('inicio'))
    
    # Crear nuevo usuario
    nuevo_usuario = Usuario(
        dni=dni,
        nombres=nombres,
        apellidos=apellidos
    )
    nuevo_usuario.set_password(passw1)
    
    # Agregar discapacidades seleccionadas
    if acceso_discapacidad == 'si' and discapacidad_ids:
        for disc_id in discapacidad_ids:
            discapacidad = Discapacidad.query.filter_by(nombre=disc_id).first()
            if discapacidad:
                nuevo_usuario.discapacidades.append(discapacidad)
    
    # Agregar preferencias seleccionadas
    if preferencia_ids:
        for pref_id in preferencia_ids:
            preferencia = Preferencia.query.filter_by(nombre=pref_id).first()
            if preferencia:
                nuevo_usuario.preferencias.append(preferencia)
    
    # Guardar en la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    flash('Registro guardado correctamente. Ya puede iniciar sesión.', 'success')
    return redirect(url_for('inicio'))

# Ruta de login
@app.route('/login', methods=['POST'])
def login():
    dni = request.form.get('usuario')
    contraseña = request.form.get('contraseña')
    
    # Buscar usuario por DNI
    usuario = Usuario.query.filter_by(dni=dni).first()
    
    if usuario and usuario.check_password(contraseña):
        # Actualizar último acceso
        usuario.ultimo_acceso = datetime.utcnow()
        db.session.commit()
        
        # Guardar información en la sesión
        session['usuario_id'] = usuario.id
        session['usuario_dni'] = usuario.dni
        session['usuario_nombre'] = f"{usuario.nombres} {usuario.apellidos}"
        
        flash(f'Bienvenido {usuario.nombres}', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Usuario o contraseña incorrecta <br> intente nuevamente', 'error')
        return redirect(url_for('inicio'))

# Ruta de cierre de sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('inicio'))

# Ruta de panel de control
@app.route('/dashboard')
def dashboard():
    # Verificar si el usuario está logueado
    if 'usuario_id' not in session:
        flash('Debe iniciar sesión para acceder', 'error')
        return redirect(url_for('inicio'))
    
    # Obtener información del usuario
    usuario = Usuario.query.get(session['usuario_id'])
    
    # Obtener actividades disponibles
    actividades = Actividad.query.filter_by(estado='activa').all()
    
    # Obtener participaciones del usuario
    participaciones = Participacion.query.filter_by(usuario_id=session['usuario_id']).all()
    
    return render_template('dashboard.html', 
                          usuario=usuario, 
                          actividades=actividades,
                          participaciones=participaciones)

@app.route('/voluntario')
def voluntario():
    return render_template('dashboard/voluntario.html')

@app.route('/organizador')
def organizador():
    return render_template('dashboard/organizador.html')

@app.route('/administrador')
def administrador():
    return render_template('dashboard/administrador.html')
    
@app.route('/actividades')
def actividades():
    # Obtener todas las actividades
    todas_actividades = Actividad.query.all()
    return render_template('actividades.html', actividades=todas_actividades)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

# Ruta para inscribirse a una actividad
@app.route('/inscribir/<int:actividad_id>', methods=['POST'])
def inscribir_actividad(actividad_id):
    # Verificar si el usuario está logueado
    if 'usuario_id' not in session:
        flash('Debe iniciar sesión para inscribirse', 'error')
        return redirect(url_for('inicio'))
    
    # Verificar si la actividad existe
    actividad = Actividad.query.get(actividad_id)
    if not actividad:
        flash('La actividad no existe', 'error')
        return redirect(url_for('dashboard'))
    
    # Verificar si ya está inscrito
    participacion_existente = Participacion.query.filter_by(
        usuario_id=session['usuario_id'],
        actividad_id=actividad_id
    ).first()
    
    if participacion_existente:
        flash('Ya estás inscrito en esta actividad', 'info')
        return redirect(url_for('dashboard'))
    
    # Crear nueva participación
    nueva_participacion = Participacion(
        usuario_id=session['usuario_id'],
        actividad_id=actividad_id,
        estado='registrado'
    )
    
    db.session.add(nueva_participacion)
    db.session.commit()
    
    flash(f'Te has inscrito correctamente a la actividad: {actividad.nombre}', 'success')
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
