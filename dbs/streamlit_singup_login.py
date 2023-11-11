"""
Proceso de registro de usuarios y login usando mysql y streamlit
"""

# pip install mysql-connector-python
# pip install streamlit

import mysql.connector
import streamlit as st
from datetime import datetime  # dates en python
from connection_data import data, tables
from queries.queries import query_insert, query_val_user


# establecer conexion
connection = mysql.connector.connect(
    host=data["host"],
    user=data["user"],
    password=data["password"],
    database=data["database"],
    port=data["port"]
)

table_name = tables["tb_customers"]


def val_user_exist(id_customer):
    """
    Valida si un usuario existe en la base de datos.

    Args:
        id_customer (int): ID del cliente a validar.

    Returns:
        bool: True si el usuario existe, False si no existe.
    """
    query = query_val_user.format(table_name=table_name, id_customer=id_customer)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado is None:
        return False  # Indica que no existe el id del usuario en la base de datos
    return True  # Indica que existe el usuario en la base de datos


def insert_user(id_customer, name_customer, lastname_customer, email_customer, password_customer, register_date):
    """
    Inserta un nuevo usuario en la base de datos.

    Args:
        id_customer (int): ID del cliente.
        name_customer (str): Nombre del cliente.
        lastname_customer (str): Apellido del cliente.
        email_customer (str): Correo electrónico del cliente.
        password_customer (str): Contraseña del cliente.
        register_date (datetime): Fecha de registro del cliente.
    """
    query = query_insert.format(
        table_name=table_name, id_customer=id_customer, name_customer=name_customer,
        lastname_customer=lastname_customer, email_customer=email_customer, password_customer=password_customer,
        register_date=register_date
    )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def val_login(id_customer, password_customer):
    """
    Valida el inicio de sesión de un usuario.

    Args:
        id_customer (int): ID del cliente.
        password_customer (str): Contraseña del cliente.

    Returns:
        bool: True si el inicio de sesión es exitoso, False si no es exitoso.
    """
    query = """
        SELECT * 
        FROM {table_name}
        WHERE id_customer = {id_customer} and password_customer = {password_customer}
    """.format(table_name=table_name, id_customer=id_customer, password_customer=password_customer)

    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado is None:
        return False  # Indica que el usuario o contraseña es incorrecto
    return True  # Indica que los datos son correctos


def login():
    """
    Sección de inicio de sesión.
    """
    st.subheader("Login Section")
    id_customer = st.sidebar.text_input("Id")
    password_customer = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        flag_login = val_login(id_customer, password_customer)
        if flag_login:
            st.success('Inicio de sesión exitoso')
            task = st.selectbox("Actividad", options=["Agregar Tareas", "Eliminar Tareas"])
        else:
            st.warning('Usuario/Contraseña incorrectos')


def signup():
    """
    Sección de registro de nuevos usuarios.
    """
    st.subheader("Create Account")
    id_customer = st.sidebar.text_input("Numero identificacion")
    name_customer = st.sidebar.text_input("Nombres")
    lastname_customer = st.sidebar.text_input("Apellidos")
    email_customer = st.sidebar.text_input("Email")
    password_customer = st.sidebar.text_input("Contrasena", type="password")
    register_date = datetime.now()

    if st.sidebar.button("Create"):
        flag_exists = val_user_exist(id_customer)
        if flag_exists:
            st.info("Usuario ya registrado")
        else:
            insert_user(id_customer, name_customer, lastname_customer, email_customer, password_customer, register_date)
            st.success("Welcome {}".format(name_customer))


def main():
    """Funcion principal que define la interfaz y maneja la navegacion.
    """
    st.title("Simple login")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        login()
    elif choice == "SignUp":
        signup()


if __name__ == "__main__":
    main()
