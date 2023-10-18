

import streamlit as st

st.write("#  fisrt program")

# Eventos
state_checkbox = st.checkbox("Checkbox", value=False, key="checker1")

if state_checkbox:
    st.write("Checkbox seleccionado")


def change():
    print(st.session_state.checker2)
    if st.session_state.checker1:
        print("Checkbox seleccionado")
    else:
        print("Checkbox deseleccionado")

st.checkbox("Checkbox", value=False, on_change=change, key="checker2")

# Opciones

def option():
    print(f"Opcion {st.session_state.option}")

radio_button = st.radio("Radio", ["1", "2", "3"], on_change=option, key="option")

# botones

def boton():
    print("Boton presionado")
btn = st.button("Click aqui", on_click=boton)

# Multiples selecciones

def select():
    print(f"Seleccionado {st.session_state.select}")
    
select = st.selectbox("Cual no es una palabra reservada de python", 
                      ["lambda", "try", "except", "spam"], key="select",
                      on_change=select)



# Multiples selecciones

def mult_opt():
    print(st.session_state.m_select)

multi_select = st.multiselect(
    "Cual es tu color favorito",
    options=["Rojo", "Verde", "Azul", "Amarillo"],
    on_change=mult_opt,
    key="m_select"

)




def text_area():
    print(st.session_state.text_area)
    print("Texto cambiado")

st.text_area("oe", key="text_area", on_change=text_area)



