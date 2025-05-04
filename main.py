from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("inicio.html")

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
