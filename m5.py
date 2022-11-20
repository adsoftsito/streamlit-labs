#Erick

import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecs


# LECTURA DE ARCHIVO
@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data



# BARRA LATERAL
sidebar = st.sidebar
sidebar.write("BUSQUEDA.")


# TITULO INTERNOS
st.title("DESERCIÓN LABORAL")
st.write(""" El fenómeno que actualmente impacta a las empresas y organizaciones.
 Múltiples estudios realizados por empresas y consultoras indican que en México aproximadamente 7 de cada 10 empleados 
cambiará de trabajo en el corto o mediano plazo por diversas razones""")

# HISTROGRAMA
data = load_data(7001)
fig,ax =plt.subplots()
ax.hist(data.Age, bins=[10,20,30,40,50,60,70])
st.header(' Histograma Employees - Age')
ax.set_xlabel('Age')
ax.set_ylabel('Num.Employees')
st.pyplot(fig)

# FRECUENCIAS - UNIT PARA SABER CUANTOS EMPLEADOS HAY EN CADA UNA UNIDAD

st.title("EMPLEADOS POR UNIT")
data = load_data(7000)
df_hometown = data.groupby('Unit').sum()
fig3, axes = plt.subplots(figsize=(16,6))
axes.plot(df_hometown['Attrition_rate'],'g')
axes.set_title('Deserción por Ciudad')
plt.xticks(rotation=40)
st.pyplot(fig3)

#GRAFICA - CIUDADES CON MAYOR INDICE DE DESERCION
st.title("DESERCIÓN LABORAL - GRAFICAS")
data = load_data(7001)
df_hometown = data.groupby('Hometown').mean()
fig2, axes = plt.subplots(nrows=3, ncols=1, figsize=(10,13))
axes[0].plot(df_hometown['Attrition_rate'],'g')
axes[0].set_title('Deserción por Ciudad')

axes[1].plot(df_hometown['Age'],'b')
axes[1].set_title('Deserción por Edad')

axes[2].plot(df_hometown['Time_of_service'],'r')
axes[2].set_title('Deserción por tiempo de servicio')
st.pyplot(fig2)



# CHECKBOX - CON TODOS LA VISUALIZACION DE TODO EL DATA FRAME
data = load_data(7001)
agree = sidebar.checkbox('mostar toda la información')
if agree:
    count_row = data.shape[0]
    st.write(f'Todos los elementos: {count_row}')
    st.dataframe(data)



# FUNCION BUSQUEDA DE EMPLEADO
@st.cache
def load_data_byname(name):
    data = load_data(7001) 
    filtered_data_byname = data[(data['Unit'].str.contains(name) | (data['Employee_ID'].str.contains(name))| (data['Hometown'].str.contains(name)))]
    return filtered_data_byname

name = sidebar.text_input('Buscar Empleado (ID, Hometown o Unit) :')
if (name):
    filterbyname = load_data_byname(name)
    count_row = filterbyname.shape[0]
    st.write('Informacion por nivel educativo')
    st.write(f"Total names : {count_row}")
    st.dataframe(filterbyname)


# FUNCION NIVEL EDUCATIVO
@st.cache
def load_data_bynivel(select_): 
    data = load_data(7000)
    filter =  data.Education_Level == select_
    filter_data_by_nivel =  data[filter] 
    return filter_data_by_nivel


# SELECT BOX -NIVEL EDUCACION
select_ =sidebar.selectbox('Seleccionar Nivel Educativo :' , data['Education_Level'].unique())
botton = sidebar.button('Filtrar')

if (botton):
    filterbynivel = load_data_bynivel(select_) 
    count_row = filterbynivel.shape[0] 
    st.dataframe(filterbynivel)
    st.write(f"Total : {count_row}")


# FUNCION CIUDAD-EMPLEADOS
@st.cache
def load_data_by_c_e(select_c): # revisar que parametro
    data = load_data(7000)
    filter =  data.Hometown == select_c
    filter_data_by_c_e =  data[filter]
    filter_data_by_c_e = filter_data_by_c_e[['Hometown','Employee_ID']]
    return filter_data_by_c_e

# SELECT BOX CIUDADES-EMPLEADOS
select_c =sidebar.selectbox('Selecciona la Ciudad :' , data['Hometown'].unique())
botton_h = sidebar.button('Filtro')

if (botton_h):
    filterbynivel = load_data_by_c_e(select_c) #tiene que leer las peliculas por director la funsion
    count_row = filterbynivel.shape[0] # da el numero de filas 3
    st.dataframe(filterbynivel)
    st.write(f"Total : {count_row}")

# FUNCION UNIDAD
@st.cache
def load_data_by_unit(select_u): # revisar que parametro
    data = load_data(7000)
    filter =  data.Unit == select_u
    filter_data_by_unit =  data[filter]
    return filter_data_by_unit

select_u =sidebar.selectbox('Selecciona Unidad :' , data['Unit'].unique())
botton_u = sidebar.button('Filtrar.')

if (botton_u):
    filterbyunit = load_data_by_unit (select_u) #tiene que leer las peliculas por director la funsion
    count_row = filterbyunit.shape[0] # da el numero de filas 3
    st.dataframe(filterbyunit)
    st.write(f"Total : {count_row}")


