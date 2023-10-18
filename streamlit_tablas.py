

import pandas as pd
import streamlit as st

names = ["Jose", "Joaquin"]
last_name = ["Guajo", "Trujillo"]

table = pd.DataFrame({"Name": names, "Last Name": last_name})

# Estatico
st.table(table)

# Dinamico 
st.dataframe(table)