# pruebafinal2.com
Proyecto final de Tratamiento de datos con Selenium - Autos usados Patiotuerca - Servicio WEB

## Descripción
Se define extraer datos de una fuente de datos online, en este caso se realiza
la extracción de datos de una empresa de Ecuador que se dedica a la venta
de automóviles de segunda mano, con la finalidad de realizar el tratamiento de datos,
como los modelos de autos, sus precios, su año de fabricación. La información
extraída se almacena en una base de datos MongoDB. Como segunda parte de la prueba
se crea un servicio web para manejar esta data extraída.
Se escoge la página online de la empresa Ecuador - Patiotuercas

https://ecuador.patiotuerca.com/usados/-/autos

## PASO 1. Configuración de librería
Crear un archivo `requirements.txt`

Contenido de archivo `requirements.txt`:
```
selenium
flask
pymongo
python-dotenv
certifi
```

Instalar las librerías ejecutando desde el terminal:
```
pip install -r requirements.txt
```
## PASO 2. Creación Base de datos MongoDB 
Se realiza la conexión a la base de datos en MongoDB, la misma que almacenará
la información extraída.

Para generar la base de datos es necesario ingresar a la siguiente URL:
https://cloud.mongodb.com/

Se recomienda generar una base de datos en la nube ubicada en Azure y que sea Free.

Se define las credenciales de la BDD:
Usuario: `soydaviti96`
Contraseña: `Password.1234`

## PASO 3. Configuración archivo .env
Se genera el archivo `.env` donde se presenta la configuración de la base de datos.

El archivo cuenta con el siguiente contenido:
```
MONGO_USER=soydaviti96
MONGO_PASSWORD=Password.1234
MONGO_HOST=cluster0.fhjhjzu.mongodb.net
```

## PASO 4. Configuración archivo mongo.py
Se genera el archivo `mongodb.py` el mismo que permite la conexión
de la base de datos con el proyecto ejecutado pycharm, específicamente
con el archivo `main.py`.

El archivo `mongo.py` cuenta con el siguiente contenido:

```
from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
db_hostname = os.getenv("MONGO_HOST")
uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client["autos"]
    except ConnectionError:
        print('Error de conexion BD')
    return db
```
## PASO 5. Creación archivo buscardb.py
Se genera el archivo buscardb.py que funciona como tipo clase y sirve para presentar las variables de Python
a las variables de la base de datos de MongoDB.

El archivo contiene lo siguiente:
```
class Autos:
    def __init__(self, modelo_auto, anio_auto, precio_auto, auto_detalle):
        self.modelo_auto = modelo_auto
        self.anio_auto = anio_auto
        self.precio_auto = precio_auto
        self.auto_detalle = auto_detalle

    def toDBCollection(self):
        return{
            'modelo_auto':self.modelo,
            'anio_auto': self.anio_auto,
            'precio_auto': self.precio_auto,
            'auto_detalle': self.auto_detalle
        }

```


## PASO 6. Configuración archivo main.py
Este es el archivo principal que permite ejecutar y desplegar la API Web con
el listado de la información extraída de la página de PatioTuercas. 

El archivo `main.py` cuenta con lo siguiente:

```
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

@app.route('/buscar/<string:listado_name>', methods=['POST'])
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

```

## Paso 7. Generación de archivo .html
Se genera el archivo `index.html` el mismo que despliega la API Web
con el listado de la información extraída en MongoDB.

El archivo contiene lo siguiente:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TRATAMIENTO DE DATOS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1 class="text-center mt-5 mb-5 "> Prueba Final </h1>
    </div>

    <div class="container">
        <div class="row row-col-1 rowcols-sm-1 row-cols-md-2 row-cols-lg-2">
           <div class="col-md-6 mb-3">
               <div class="card">
                   <div class="card-header">
                       <h5 class="text-center"> Productos PatioTuerca </h5>
                   </div>
                   <div class="card-body">
                        <form action="/buscar" method="POST">
                            <label>Buscar:</label>
                            <input type="text" class="form-control mb-3" name="modelo_auto">
                        </form>
                   </div>
               </div>
           </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">
                        <h5 class="text-center">Listado de autos PatioTuerca</h5>
                    </div>
                    <div class="card-body">
                        <ul class="list-group">
                            <div class="row row-col-2 rowcols-sm-2 row-cols-md-2 row-cols-lg-2">
                                {% for buscardb in listadoproductos %}

                                    <div class="col">
                                        <li class="list-group-item mb-2">
                                            <form action="/buscar/{{buscardb.modelo_auto}}" method="POST">
                                                <input type="text" class="form-control" value="{{buscardb.modelo_auto}}" name="modelo_auto">
                                                <small>Anio auto:</small>
                                                <input type="text" class="form-control" value="{{buscardb.anio_auto}}" name="anio_auto">
                                                <small>Precio:</small>
                                                <input type="text" class="form-control" value="{{buscardb.precio_auto}}" name="precio_auto">
                                                <small>Detalle:</small>
                                                <input type="text" class="form-control" value="{{buscardb.auto_detalle}}" name="auto_detalle">
                                            </form>
                                        </li>
                                    </div>

                                {% endfor %}
                            </div>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```
