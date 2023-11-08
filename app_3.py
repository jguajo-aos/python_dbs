
#Importar librerias
from flask import Flask, jsonify # convertir un objeto a un json del navegador
from products import products

#Crear aplicacion del servidor
app = Flask(__name__)
#Entregar datos, datos de productos

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products_list": products, "message": "Lista de productos"})

if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)