from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voluntariado.db' #voluntariado.db = name_database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

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
