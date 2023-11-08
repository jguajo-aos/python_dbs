
import streamlit as st

# Escribir un titutlo
st.title("Hello World")

# Escribir un header
st.header("Header")

# Escribir un subheader
st.subheader("Subheader")

# Escribir un texto
st.text("Text")

# Escribir un markdown https://www.markdownguide.org/cheat-sheet/
st.markdown("# Markdown *Jose Joaquin Ey*")

# Agregar un caption
st.caption("Caption")

# Agregar latex https://katex.org/docs/supported.html
st.latex(r"\begin{equation} \frac{1}{2} \end{equation}")

# Escribir un json en la pagina web
json = {
    "name": "Maria",
    "age": 30,
    "city": "Bogota"
}

st.json(json) # Escribir un json en la pagina web

# Mostrar codigo en la web
code = """
print("hello world")
"""
st.code(code, language="python")

# Funcion write, permite hacer lo anterior
st.write("## H2")

# Escribir una metrica
st.metric(label="Temparature", value="35C", delta="5")