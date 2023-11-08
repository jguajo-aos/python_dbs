
#Importar librerias
from flask import request, Flask, jsonify # convertir un objeto a un json del navegador
from products import products
import json

#Crear aplicacion del servidor
app = Flask(__name__)
#Entregar datos, datos de productos

@app.route("/valpassword", methods=["GET"])
def val_password():
    dato = request.get_json()
    contrasena = dato["pass"]
    user = dato["name"]
    print(user)
    print(contrasena)
    longitud_minima = 8
    debe_tener_mayuscula = False
    debe_tener_minuscula = False
    debe_tener_numero = False

    # Verificar la longitud mínima
    if len(contrasena) >= longitud_minima:
        # Verificar otros requisitos
        for caracter in contrasena:
            if caracter.isupper():
                debe_tener_mayuscula = True
            elif caracter.islower():
                debe_tener_minuscula = True
            elif caracter.isdigit():
                debe_tener_numero = True

    # Comprobar si la contraseña cumple con todos los requisitos
    if (debe_tener_mayuscula and debe_tener_minuscula and debe_tener_numero):
        print("valido")
        return jsonify({"message": "contrasena valida"})
    else:
        print("invalido")
        return jsonify({"message": "contrasena invalida"})






if __name__ == "__main__":
    #ejecucion del servidor, si se hacde un cambio el script va a reiniciar
    app.run(debug=True, port=4000)