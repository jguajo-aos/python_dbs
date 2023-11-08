
#Importar librerias
from flask import Flask, jsonify # convertir un objeto a un json del navegador
from products import products

#Crear aplicacion del servidor
app = Flask(__name__)
#Entregar datos, datos de productos

@app.route("/products/<string:product_name>", methods=["GET"])
def get_esp_product(product_name):
    for prod in products:
        if prod["name"] == product_name:
            return jsonify({"product": prod})
    return  jsonify({"message": "producto no encontrado"})

if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)