
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


@app.route("/products", methods=["POST"])
def add_products():
    dato = request.get_json()
    new_prodc = {
        "name": dato["name"],
        "price": dato["price"],
        "qunatity": dato["qunatity"]
    }

    products.append(new_prodc)

    return jsonify({"message": "producto agregado ok", "products": products})

if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)