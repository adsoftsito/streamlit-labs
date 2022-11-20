#Raul

import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt  



st.title('Entrega de proyecto M5 Raúl Rodríguez Salomón')
st.header('Dashboard_Empleados 2020')
st.write(' En esta applicación podras analizar la información de empleados provistos en el Hackathon HackerEarth 2020,  tomando  como  hipótesis  que  esta  información  resultará  explicativa  del  fenómeno  de  deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones')


ruta =  'Employees..csv'

@st.cache
def load_data(nrows):
    employees = pd.read_csv(ruta, nrows=nrows)
    return employees 

def filter_data_by_id(Employee_ID):
    filtered_data_id = employees[employees['Employee_ID'].str.upper().str.contains(Employee_ID)]
    return filtered_data_id

def filter_data_by_Hometown(Hometown):
    filtered_data_Hometown = employees[employees['Hometown'].str.upper().str.contains(Hometown)]
    return filtered_data_Hometown

def filter_data_by_Unit(Unit):
    filtered_data_Unit = employees[employees['Unit'].str.upper().str.contains(Unit)]
    return filtered_data_Unit

def filter_data_by_Level(Education_Level):
    filtered_data_EL = employees[employees['Education_Level'] == Education_Level]
    return filtered_data_EL

def filter_data_by_Unit2(Unit):
    filtered_data_Unit2 = employees[employees['Unit'] == Unit]
    return filtered_data_Unit2



employees = load_data(500)

tituloid = st.sidebar.text_input('Busqueda por ID :')
btnBuscar_ID = st.sidebar.button('Buscar * Employee_ID')
tituloht = st.sidebar.text_input("Busqueda por residencia :")
btnBuscar_HT = st.sidebar.button('Buscar * Hometown')
tituloUnit = st.sidebar.text_input("Busqueda por Área del empleado :")
btnBuscar_Unit = st.sidebar.button('Buscar * Unit')

if (btnBuscar_ID):
   employees_id_f = filter_data_by_id(tituloid.upper())
   count_row = employees_id_f.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(employees_id_f)

if (btnBuscar_HT):
   data_ht = filter_data_by_Hometown(tituloht.upper())
   count_row = data_ht.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_ht)
if (btnBuscar_Unit):
   data_unit = filter_data_by_Unit(tituloUnit.upper())
   count_row = data_unit.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_unit)
  
selected_EL = st.sidebar.selectbox("Seleccionar Nivel Educativo", employees['Education_Level'].unique())
btnFilterbyEL = st.sidebar.button('Filtrar Nivel Educativo ')
selected_HT = st.sidebar.selectbox("Seleccionar lugar de residencia del empleado", employees['Hometown'].unique())
btnFilterbyHT = st.sidebar.button('Filtrar lugar de residencia del empleado ')
selected_Unit = st.sidebar.selectbox("Seleccionar Área laboral", employees['Unit'].unique())
btnFilterbyUnit = st.sidebar.button('Filtrar Área del empleado')


if (btnFilterbyEL):
   filterbyEL = filter_data_by_Level(selected_EL)
   count_row = filterbyEL.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyEL)

if (btnFilterbyHT):
   filterbyHT = filter_data_by_Hometown(selected_HT.upper())
   count_row = filterbyHT.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyHT)

if (btnFilterbyUnit):
   filterbyUnit = filter_data_by_Unit2(selected_Unit)
   count_row = filterbyUnit.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyUnit)

if st.sidebar.checkbox('Tabla completa de empleados'):
    st.subheader('Employees data')
    st.dataframe(employees)

# Histograma
   
fig, ax = plt.subplots()  
   
ax.hist(employees['Age'])    
   
st.header("Histograma Edad de los empleados")  
   
st.pyplot(fig)    
st.markdown("___")   


#FFrecuencia

fig2, ax2 = plt.subplots()  
   
ax2.plot(employees['Unit'].value_counts(),'bo')
plt.xticks(rotation=90)

st.header("# de empleados por área")  
   
st.pyplot(fig2)  
 
st.markdown("___")  

#Barras

fig3, ax3 = plt.subplots()  
   
ax3.bar(employees['Hometown'],employees['Attrition_rate'].mean())  
ax3.set_ylabel("Attrition_rate")  
ax3.set_xlabel("Hometown")
   

st.header("Deserción por ubicación")  
   
st.pyplot(fig3)  
  
st.markdown("___") 

fig4, ax4 = plt.subplots()  
   
ax4.bar(employees['Age'],employees['Attrition_rate'])
ax4.set_ylabel("Attrition_rate")  
ax4.set_xlabel("Age")
   
st.header("Relación edad-deserción")  
   
st.pyplot(fig4)  

st.markdown("___") 

fig5, ax5 = plt.subplots()  
   
ax5.scatter(employees['Time_of_service'],employees['Attrition_rate'])  
   
st.header("Relación Tiempo de servicio - deserción")  
   
st.pyplot(fig5)  

   
st.markdown("___") 
