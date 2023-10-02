from flask import Flask, render_template, request
from Buscardb import busquedamongo

app=Flask(__name__, template_folder='web')


@app.route('/')
def carga():
    return render_template("paginaprincipal.html")
@app.route('/procesar', methods=['POST'])
def procesar():
    modelo_auto = request.form.get("modelo_auto")
    auto_detalle = request.form.get("anio_auto")

        #"modelo_auto": auto_name,
        #"anio_auto": auto_detalle,
        #"precio_auto:": auto_precio,
        #"auto_detalle:": auto_negociable

    buscar=busquedamongo(modelo_auto=modelo_auto,anio_auto=auto_detalle,verbose=True)

    return render_template("busqueda.html",datos=buscar)

if __name__ == "_main_":

    app.run(host='0.0.0.0', port=8000,debug=True)
