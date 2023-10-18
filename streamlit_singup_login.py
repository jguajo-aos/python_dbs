

import streamlit as st

def login():
    st.subheader("Login Section")

    user = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        print(st.session_state)
        if user in st.session_state and st.session_state[user] == password:
            st.success("Logged in as {}".format(user))
            st.write('Inicio de sesión exitoso')
            task = st.selectbox("Actividad", options=["Agregar Tareas", "Eliminar Tareas"])
        else:
            st.warning('User/Password incorrectos')

def signup():
    st.subheader("Create Account")

    new_user = st.sidebar.text_input("Username")
    new_password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Create"):
        st.success("Welcome {}".format(new_user))
        if new_user not in st.session_state:
            st.session_state[new_user] = new_password



def main():

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