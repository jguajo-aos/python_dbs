
#Importar librerias
from flask import Flask, jsonify # convertir un objeto a un json del navegador
from products import products

#Crear aplicacion del servidor
app = Flask(__name__)

#Entregar datos, datos de productos

# Sejecuta la funcion cada vez que se ejecuta esa ruta
@app.route("/ping")
def ping():
    return jsonify(
        {"message": "pong!"}
    )

if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)