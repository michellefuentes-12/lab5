import streamlit as st

st.title("Diagnóstico de conexión")

st.write("¿Secrets cargados?:", bool(st.secrets))

st.write("¿Existe mysql?:", "mysql" in st.secrets)

if "mysql" in st.secrets:
    st.success("La sección mysql fue reconocida")

    st.write(
        "Claves encontradas:",
        list(st.secrets["mysql"].keys())
    )
else:
    st.error("No se encuentra la sección mysql")
