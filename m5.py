# manuel.py
# Jorge
# Carlos Gtz
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#6. Crear título de la aplicación, encabezados y texto de descripción del proyecto. 
st.title('Employees app')

DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')

import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_employees(empleados):
    filtered_data_employees = data[data['Employee_ID'].str.upper().str.contains(empleados)]
    return filtered_data_employees

def filter_data_by_education(Education_Level):
    filtered_data_education= data[data['Education_Level'] == Education_Level]
    return filtered_data_education

def filter_data_by_hometown(Hometown):
    filtered_data_hometown= data[data['Hometown'] == Hometown]
    return filtered_data_hometown

def filter_data_by_unit(Unit):
    filtered_data_unit= data[data['Unit'] == Unit]
    return filtered_data_unit


data_load_state = st.text('Loading Employees data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

# 7. Crear un sidebar en la aplicación 
# 8. En sidebar crear un control checkbox que permita mostrar u ocultar el dataframe 

if st.sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los empleados')
    st.write(data)

### 9. Crear un buscador de empleados con cajas de texto y botones de comando, que 
permitan buscar por Employee_ID, Hometown o Unit, mostrar dataframe con resultados 
encontrados y total de empleados. Nota:  Usar funciones con cache. 
idemployee = st.sidebar.text_input('ID de Empleado, Lugar de residencia o de Unidad :')
btnBuscar = st.sidebar.button('Buscar empleado')###

if (btnBuscar):
   data_employees = filter_data_by_employees(idemployee.upper())
   count_row = data_employees.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_employees)

### 10. En el sidebar incluir un control selectedbox que permita filtrar los empleados por su nivel 
educativo, mostrar el dataframe filtrado y total de empleados. Nota:  Usar funciones con 
cache. ###
selected_nivelEducativo = st.sidebar.selectbox("Seleccionar Nivel educativo", data['Education_Level'].unique())
btnFilterbyEducation = st.sidebar.button('Nivel educativo ')

if (btnFilterbyEducation):
   filterbyedu = filter_data_by_education(selected_nivelEducativo)
   count_row = filterbyedu.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyedu)

### 11. En el sidebar crear un control selectedbox con las ciudades que participaron en el 
estudio, mostrar los empleados por ciudad en un dataframe filtrado y total de 
empleados. Nota:  Usar funciones con cache. ###

selected_hometown = st.sidebar.selectbox("Seleccionar lugar de Residencia", data['Hometown'].unique())
btnFilterbyhometown = st.sidebar.button('Lugar de Residencia ')

if (btnFilterbyhometown):
   filterbyhome = filter_data_by_hometown(selected_hometown)
   count_row = filterbyhome.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyhome)
### 12. Crear un selectedbox para filtrar por la unidad funcional (Unit) a la que pertenece. Nota:  
Usar funciones con cache. ###

selected_unit = st.sidebar.selectbox("Seleccionar unidad", data['Unit'].unique())
btnFilterbyunit = st.sidebar.button('Unidad ')

if (btnFilterbyunit):
   filterbyunit = filter_data_by_unit(selected_unit)
   count_row = filterbyunit.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyunit)
   
# 13. Crear un histograma de los empleados agrupados por edad. 
if st.sidebar.checkbox('Edades'):
    st.subheader('Edad')

    hist_values = np.histogram(data['Age'], bins=8, range=(0,50))[0]
    st.bar_chart(hist_values)

### 14. Crear una gráfica de frecuencias para las unidades funcionales (Unit) para conocer 
cuántos empleados hay en cada Unidad ###

st.title("Empleados por unidad")
data = load_data(7000)
df_hometown = data.groupby('Unit').sum()
fig3, axes = plt.subplots(figsize=(16,6))
axes.plot(df_hometown['Attrition_rate'],'g')
axes.set_title('Deserción por Ciudad')
plt.xticks(rotation=40)
st.pyplot(fig3)

###15. Analizar los datos con una gráfica que nos permita visualizar las ciudades (Hometown) 
que tienen el mayor índice de deserción ###

st.title("Deserción Laboral")
data = load_data(7001)
df_hometown = data.groupby('Hometown').mean()
fig2, axes = plt.subplots(nrows=3, ncols=1, figsize=(10,13))
axes[0].plot(df_hometown['Attrition_rate'],'g')
axes[0].set_title('Deserción por Ciudad')

### 16. Analizar la información con una gráfica que permita visualizar la edad y la tasa de 
deserción ###
axes[1].plot(df_hometown['Age'],'b')
axes[1].set_title('Deserción por Edad')

### 17. Analizar con una gráfica que determine la relación entre el tiempo de servicio y la tasa 
de deserción ###

axes[2].plot(df_hometown['Time_of_service'],'r')
axes[2].set_title('Deserción en el tiempo de servicio')
st.pyplot(fig2)
