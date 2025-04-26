from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola!"

@app.route('/api/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"mensaje": f"Hola, {nombre}!"})

if __name__ == '__main__':
    app.run(debug=True)
