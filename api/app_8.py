
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


@app.route("/products", methods=["DELETE"])
def delete_products():
    dato = request.get_json()

    prod = dato["name"]

    proc_found = False
    for index, producto in enumerate(products):
        if producto["name"] == prod:
            del products[index]
            proc_found = True
    if proc_found:
        return jsonify({"message": "producto eliminado ok", "products": products})
    else:
        return jsonify({"message": "product no found"})




if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)