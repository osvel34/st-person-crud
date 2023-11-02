import streamlit as st
import sqlite3
import pandas as pd

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('personasdb.db')
c = conn.cursor() 

# Crear la tabla si no existe
#c.execute('''
#    CREATE TABLE IF NOT EXISTS personas (
#        id INTEGER PRIMARY KEY,
#        nombre TEXT,
#        edad INTEGER
#    )
#''')
#conn.commit()

# Función para insertar una persona en la base de datos
def insertar_persona(nombre, edad):
    c.execute("INSERT INTO personas (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()

# Función para obtener todas las personas de la base de datos
def obtener_personas():
    c.execute("SELECT nombre, edad FROM personas")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['Nombre', 'Edad'])
    return df

# Aplicación Streamlit
st.title("Registro de Personas en la ciudad")

# Formulario para agregar una nueva persona
nuevo_nombre = st.text_input("Nombre")
nueva_edad = st.number_input("Edad", min_value=0, max_value=150, step=1)
if st.button("Agregar"):
    if nuevo_nombre and nueva_edad:
        insertar_persona(nuevo_nombre, nueva_edad)
        st.success(f"Se ha agregado a {nuevo_nombre} de {nueva_edad} años.")

# Mostrar la lista de personas
st.header("Lista de Personas")
personas_df = obtener_personas()
if not personas_df.empty:
    #st.write(personas_df)
    st.table(personas_df)
else:
    st.info("No hay personas registradas en la base de datos.")

# Cerrar la conexión a la base de datos al finalizar
conn.close()
