import streamlit as st

st.title("Conexión con base de datos MySQL")

try:
    st.write("Secciones:", list(st.secrets.keys()))

    st.write(
        "Variables MySQL:",
        list(st.secrets["mysql"].keys())
    )

    st.success("Secrets reconocidos correctamente")

except KeyError as e:
    st.error(f"No se encontró la clave: {e}")
