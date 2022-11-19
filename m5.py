# manuel.py
# Jorge
#Importando librerias necesarias
import streamlit as st
import pandas as pd
import numpy as np
import codecs

st.title('Análisis de datos de deserción')
st.text('Aplicación para el análisis de la deserción en empresas de las ciudades del país.')

sidebar = st.sidebar
sidebar.title("Jorge - Filtros de búsqueda")


# DATE_COLUMN = 'started_at'
DATA_URL = ('Employees.csv')

#Funcion para obtener todos los datos
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    # data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Funcion para obtener datos filtrados
@st.cache
def load_data_byVar(name,valor):
    doc = codecs.open(DATA_URL,'rU','latin1')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    if valor == 1:
        filtered_data_byVar = data[data['Employee_ID'].str.contains(name)]
    elif valor == 2:
        filtered_data_byVar = data[data['Hometown'].str.contains(name)]
    elif valor == 3:
        filtered_data_byVar = data[data['Unit'].str.contains(name)]
    else: 
        filtered_data_byVar = data[data['Education_Level'] == int(name)]
    return filtered_data_byVar



#Muestra todos los datos
data = load_data(500)
mcheckbox = False
mcheckbox = st.sidebar.checkbox('Mostrar dataframe completo')
if mcheckbox:
    st.header('Conjuntos de datos')
    st.subheader('Todos los datos')
    st.write(data)


### ---------Text inputs y Botones
id_empleado = sidebar.text_input('Id de Empleado:')
btnIdEmpleado = sidebar.button('Buscar')
if(btnIdEmpleado):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Empleado')
    filterbyId = load_data_byVar(id_empleado,1)
    st.dataframe(filterbyId)
    count_row = filterbyId.shape[0]
    st.write(f"Total Empleados : {count_row}")

hometown = sidebar.text_input('Ciudad de Origen:')
btnhometown = sidebar.button('Buscar por Ciudad')
if(btnhometown):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Ciudad')
    filterbyhometown = load_data_byVar(hometown,2)
    st.dataframe(filterbyhometown)
    count_row = filterbyhometown.shape[0]
    st.write(f"Total Empleados : {count_row}")

unidad = sidebar.text_input('Unidad :')
btnunidad = sidebar.button('Buscar por Unidad')
if(btnunidad):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Unidad')
    filterbyunidad = load_data_byVar(unidad,3)
    st.dataframe(filterbyunidad)
    count_row = filterbyunidad.shape[0]
    st.write(f"Total Empleados : {count_row}")


###---------Selectboxs y botones
doc = codecs.open(DATA_URL,'rU','latin1')
data = pd.read_csv(doc)
education_level = sidebar.selectbox("Selecciona el Nivel Educativo", data['Education_Level'].sort_values().unique())
btnEducation = sidebar.button('Busca por nivel educativo: ')
if(btnEducation):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Nivel Educativo')
    filterbyEdu = load_data_byVar(education_level,4)
    st.dataframe(filterbyEdu)
    count_row = filterbyEdu.shape[0]
    st.write(f"Total Empleados : {count_row}")



#doc = codecs.open(DATA_URL,'rU','latin1')
#data = pd.read_csv(doc)
ciudad = sidebar.selectbox("Selecciona la ciudad", data['Hometown'].unique())
btnciudad = sidebar.button('Busca por ciudad: ')
if(btnciudad):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Ciudad')
    filterbyTown = load_data_byVar(ciudad,2)
    st.dataframe(filterbyTown)
    count_row = filterbyTown.shape[0]
    st.write(f"Total Empleados : {count_row}")


# doc = codecs.open(DATA_URL,'rU','latin1')
# data = pd.read_csv(doc)
unidadS = sidebar.selectbox("Selecciona la Unidad", data['Unit'].sort_values().unique())
btnUnidadS = sidebar.button('Busca Unidad: ')
if(btnUnidadS):
    st.header('Conjuntos de datos')
    mcheckbox = False
    st.subheader('Filtro por Unidad')
    filterbyUnit = load_data_byVar(unidadS,3)
    st.dataframe(filterbyUnit)
    count_row = filterbyUnit.shape[0]
    st.write(f"Total Empleados : {count_row}")



###---------Gráficos
st.header('Gráficos')
# Histograma
st.subheader('Histograma por edades')
hist_values = np.histogram(data['Age'],bins=20, range=(0,24))[0]
st.bar_chart(hist_values)

# Empleados por Unidad
st.subheader('Empleados por Unidad')
bar_values = data.loc[:,['Unit','Employee_ID']].groupby('Unit').count()
bar_values.rename(columns= {'Employee_ID':'Empleados'}, inplace = True)
st.bar_chart (bar_values)


# Deserción por ciudad
st.subheader('Deserción por Ciudad de Origen')
bar_values = data.loc[:,['Hometown','Attrition_rate']].groupby('Hometown').mean()
st.bar_chart (bar_values)


# Deserción por edades
st.subheader('Deserción por Edad')
bar_values = data.loc[:,['Age','Attrition_rate']].groupby('Age').mean()
st.bar_chart (bar_values)

# Deserción por Tiempo de servicio
st.subheader('Deserción por Tiempo de servicio')
bar_values = data.loc[:,['Time_of_service','Attrition_rate']].groupby('Time_of_service').mean()
st.bar_chart (bar_values)


