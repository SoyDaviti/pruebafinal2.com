from flask import Flask, render_template, request, jsonify, redirect, url_for
import mongodb as basebd
from buscardb import Autos

db = basebd.dbConnection()
app = Flask(__name__)


@app.route('/')
def inicio():
    listadoproductos = db['buscar']
    productsReceived = listadoproductos.find()
    return render_template('index.html', listadoproductos = productsReceived)

@app.route('/buscar', methods=['POST'])
def buscar():
    modelo_auto = request.form.get("modelo_auto")
    anio_auto = request.form.get("anio_auto")
    precio_auto = request.form.get("precio_auto")
    auto_detalle = request.form.get("auto_detalle")

    if modelo_auto and anio_auto and precio_auto and auto_detalle:
        buscardb = Autos(modelo_auto, anio_auto, precio_auto, auto_detalle)
        response = jsonify({
            'modelo_auto': modelo_auto,
            'anio_auto': anio_auto,
            'precio_auto': precio_auto,
            'auto_detalle': auto_detalle
        })
        return redirect(url_for('inicio'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message={
        'message': 'No encontrado'+request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response







if __name__ == "__main__":
    app.run(debug=True, port=4000)
