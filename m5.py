#Roney
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title("RETO MÓDULO 5")
st.header("Análisis df Employees")

st.write("""
Este es el proyecto para el Reto del módulo 5. 
Se estará poniendo en práctica el uso de Streamlit
así como todo el conocimiento adquirido en módulos anteriores.
""")

# Definición de todas las funciones a utilizar.

@st.cache
def load_data(nrows):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

@st.cache
def filtro_datos_x_employeeID(employeeID):
    filtro_datos_x_employeeID = data[data['Employee_ID'].str.upper().str.contains(employeeID)]
    return filtro_datos_x_employeeID

@st.cache
def filtro_datos_x_hometown(hometown):
    filtro_datos_x_hometown = data[data['Hometown'].str.upper().str.contains(hometown)]
    return filtro_datos_x_hometown

@st.cache
def filtro_datos_x_unit(unit):
    filtro_datos_x_unit = data[data['Unit'].str.upper().str.match(unit)]
    return filtro_datos_x_unit

@st.cache
def filtro_datos_x_nivel(education_level):
    filtro_datos_x_nivel = data[data['Education_Level'] == education_level]
    return filtro_datos_x_nivel

@st.cache
def filtro_datos_x_hometown2(hometown2):
    filtro_datos_x_hometown2 = data[data['Hometown'] == hometown2]
    return filtro_datos_x_hometown2

@st.cache
def filtro_datos_x_unit2(unit2):
    filtro_datos_x_unit2 = data[data['Unit'] == unit2]
    return filtro_datos_x_unit2   

# Creación de elementos del sidebar (Checkbox, buttons, selectbox, text_input)

data_load_state = st.text("Cargando datos.")
data = load_data(500)
data_load_state.text("Listo!")

if st.sidebar.checkbox("Mostrar datos"):
    st.subheader("Datos completos")
    st.write(data)

ID_empleado = st.sidebar.text_input('ID de empleado :')
btn_ID_empleado = st.sidebar.button('Buscar ID')

if (btn_ID_empleado):
   data_ID_empleado = filtro_datos_x_employeeID(ID_empleado.upper())
   count_row = data_ID_empleado.shape[0] 
   st.write(f"Total de empleados encontrados : {count_row}")
   st.write(data_ID_empleado)

ciudad = st.sidebar.text_input('Ciudad de origen :')
btn_ciudad = st.sidebar.button('Buscar x ciudad')

if (btn_ciudad):
   data_ciudad = filtro_datos_x_hometown(ciudad.upper())
   count_row = data_ciudad.shape[0] 
   st.write(f"Total de empleados encontrados : {count_row}")
   st.write(data_ciudad)

unidad = st.sidebar.text_input('Unidad funcional :')
btn_unidad = st.sidebar.button('Buscar Unidad')

if (btn_unidad):
   data_unidad = filtro_datos_x_unit(unidad.upper())
   count_row = data_unidad.shape[0] 
   st.write(f"Total de empleados encontrados : {count_row}")
   st.write(data_unidad)

nivel_educativo = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btn_nivel_educativo = st.sidebar.button('Filtrar x Nivel ')

if (btn_nivel_educativo):
   filter_Education = filtro_datos_x_nivel(nivel_educativo)
   count_row = filter_Education.shape[0]  
   st.write(f"Total de empleados encontrados : {count_row}")

   st.dataframe(filter_Education)

ciudad2 = st.sidebar.selectbox("Seleccionar ciudad", data['Hometown'].unique())
btn_ciudad2 = st.sidebar.button('Filtrar x Ciudad ')

if (btn_ciudad2):
   filter_ciudad2= filtro_datos_x_hometown2(ciudad2)
   count_row = filter_ciudad2.shape[0]  
   st.write(f"Total de empleados encontrados : {count_row}")

   st.dataframe(filter_ciudad2)

unidad2 = st.sidebar.selectbox("Seleccionar unidad funcional", data['Unit'].unique())
btn_unidad2 = st.sidebar.button('Filtrar x Unidad ')

if (btn_unidad2):
   filter_unit2 = filtro_datos_x_unit2(unidad2)
   count_row = filter_unit2.shape[0]  
   st.write(f"Total de empleados encontrados : {count_row}")

   st.dataframe(filter_unit2)

# Creación de gráficos

data.dropna(inplace=True)

if st.sidebar.checkbox('Histograma Edad'):
    st.subheader('Agrupamiento por edad')
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    hist_edad = pd.DataFrame(data, columns = ["Age"])
    hist_edad.hist()
    plt.show()
    st.pyplot()

if st.sidebar.checkbox('Frecuencia Unidad'):
    st.subheader('Empleados x Unidad')
    
    val_count = data["Unit"].value_counts()
    fig = plt.figure(figsize=(10,5))
    sns.barplot(val_count.index, val_count.values, alpha=0.8)
    plt.xticks(rotation = 45)
    st.pyplot(fig)

if st.sidebar.checkbox('Deserción x Ciudad'):
    st.subheader('Deserción x Ciudad')

    att_hometown = data.groupby("Hometown")["Attrition_rate"].max()
    fig = plt.figure(figsize=(10,5))
    sns.barplot(att_hometown.index, att_hometown.values)
    plt.xticks(rotation = 45)
    st.pyplot(fig)

if st.sidebar.checkbox('Deserción x Edad'):
    st.subheader('Deserción x Edad')

    att_age = data.groupby("Age")["Attrition_rate"].mean()
    fig = plt.figure(figsize=(10,5))
    sns.barplot(att_age.index, att_age.values, alpha=0.8)
    plt.xticks(rotation = 90)
    st.pyplot(fig)

if st.sidebar.checkbox('Relación ToS/Deserción'):
    st.subheader('Relación Tiempo de Servicio Vs. Deserción')

    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(data.corr(), annot=True)
    st.pyplot()
    
