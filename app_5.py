
#Importar librerias
from flask import request, Flask, jsonify # convertir un objeto a un json del navegador
from products import products
import json

#Crear aplicacion del servidor
app = Flask(__name__)
#Entregar datos, datos de productos

# Sejecuta la funcion cada vez que se ejecuta esa ruta
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "Pong!"})


@app.route("/products", methods=["GET"])
def get_esp_product():
    dato = request.get_json()
    print(dato["name"])
    for prod in products:
        if prod["name"] == dato["product"]:
            return jsonify({"product": prod})
    return  jsonify({"message": "producto no encontrado"})

if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)