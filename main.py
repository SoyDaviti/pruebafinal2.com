from flask import Flask, render_template, request
from buscardb import busquedamongo

app = Flask(__name__)


@app.route('/')
def carga():
    return render_template('index.html')

#@app.route('/procesar', methods=['POST'])
#def procesar():
 #   modelo_auto = request.form.get("modelo_auto")
  #  auto_detalle = request.form.get("anio_auto")

        #"modelo_auto": auto_name,
        #"anio_auto": auto_detalle,
        #"precio_auto:": auto_precio,
        #"auto_detalle:": auto_negociable

    #buscar=busquedamongo(modelo_auto=modelo_auto,anio_auto=auto_detalle,verbose=True)

    #return render_template("busqueda.html",datos=buscar)

if __name__ == "__main__":

    app.run(debug=True, port=4000)
