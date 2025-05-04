from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '852456'

# Ruta principal
@app.route("/")
def inicio():
    return render_template("inicio.html")

# Ruta de registro
@app.route('/registro', methods=['POST'])
def registro():
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    dni = request.form.get('dni')
    passw1 = request.form.get('passw1')
    passw2 = request.form.get('psw2')
    acceso_discapacidad = request.form.get('accs')     # Checkbox valor del radio
    discapacidad = request.form.getlist('disc[]')      # Si marcó alguna discapacidad
    otras_discap = request.form.get('otra_discap')     # Si escribe otra discapacidad
    preferencias = request.form.getlist('pref[]')      # Preferencias marcadas

    if passw1 != passw2:
        flash('Las contraseñas no coinciden.')
        return redirect(url_for('inicio'))

    # Falta implementar para DB
    flash('Registro guardado')
    return redirect(url_for('inicio'))

# Ruta de login
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    contraseña = request.form.get('contraseña')

    # Aquí podrías validar con base de datos
    if usuario == "73992058" and contraseña == "palomino":  # Simulando
        flash('Bienvenido Dany')
    else:
        flash('Usuario o contraseña incorrecta.')
    return redirect(url_for('inicio'))

@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')
    
if __name__ == "__main__":
    app.run(debug=True)
