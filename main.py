from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voluntariado.db' #voluntariado.db = name_database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def execute_sql_script(script_file):
    with app.app_context():
        try:
            with open(script_file, 'r') as f:
                sql_script = f.read()
            db.session.execute(sql_script)
            db.session.commit()
        except Exception as e:
            print(f"Error al ejecutar el script SQL: {e}")
            db.session.rollback()

@app.before_first_request
def create_tables():
    execute_sql_script('database/esquema.sql')

# Modelo de ejemplo
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
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Ruta principal
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')
    
# Manejando formularios
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'Iniciando sesión para {username}'

@app.route('/registro', methods=['POST'])
def registro():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    return f'Registrando a {username} con el correo {email}'

if __name__ == '__main__':
    db.create_all()  # Crea todas las tablas
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=3000)  # ¿accesible?
