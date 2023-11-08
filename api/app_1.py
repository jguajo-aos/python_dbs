
#Importar librerias
from flask import Flask
from products import products

#Crear aplicacion del servidor
app = Flask(__name__)

#Entregar datos, datos de productos

# Sejecuta la funcion cada vez que se ejecuta esa ruta
@app.route("/ping")
def ping():
    return "Pong Claudio"

@app.route("/saludo")
def saludo():
    return "Hello world Claudio Augusto"



# inicio de la ejecuion
if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)