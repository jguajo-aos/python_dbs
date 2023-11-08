
import streamlit as st


# Agregar una imagen desde una url
st.image(
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", 
    width=300,
    caption="Python"
)

# Agregar una imagen desde local
st.image(
    "media_data/636ec9b036dfd.png", 
    width=300,
    caption="Restaurante"
)

# Agregar un audio
st.audio("media_data/titanium-170190.mp3")

# Agregar un video
st.video("https://www.youtube.com/watch?v=UWb5Qc-fBvk")
