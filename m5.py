# Joaquin

import streamlit as st
import pandas as pd
import numpy as np



st.title('Employees App')
st.header("Información sobre el conjunto de datos de empleados")
st.write("""
Este es un simple ejemplo de una app para ver los datos de un dataframe
""")

DATE_COLUMN = 'Employee_ID'
AGE_COLUMN = 'Age'
UNIT_COLUMN = 'Unit'
DATA_URL = ('Employees.csv')

import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_employee(employee):
    filtered_data_employee = data[data['Employee_ID'].str.upper().str.contains(employee)]
    return filtered_data_employee

def filter_data_by_unit(unit):
    filtered_data_unit = data[data['Unit'] == unit]
    return filtered_data_unit


def filter_data_by_hometown(hometown):
    filtered_data_hometown = data[data['Hometown'] == hometown]
    return filtered_data_hometown


data_load_state = st.text('Loading employee data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los empleados')
    st.write(data)


empleado = st.sidebar.text_input('Numero de empleado :')
btnBuscar = st.sidebar.button('Buscar empleado')

if (btnBuscar):
   data_employee = filter_data_by_employee(empleado.upper())
   count_row = data_employee.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_employee)



selected_hometown = st.sidebar.selectbox("Seleccionar hometown", data['Hometown'].unique())
btnFilterbyhome = st.sidebar.button('Filtrar hometown')

if (btnFilterbyhome):
   filterbyhom = filter_data_by_hometown(selected_hometown)
   count_row = filterbyhom.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyhom)


selected_unit = st.sidebar.selectbox("Seleccionar unidad", data['Unit'].unique())
btnFilterbyunit = st.sidebar.button('Filtrar Unidad')

if (btnFilterbyunit):
   filterbyuni = filter_data_by_unit(selected_unit)
   count_row = filterbyuni.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyuni)

st.write('Histograma de edades')
hist_values = np.histogram(data[AGE_COLUMN], bins=65, range=(0,65))[0]
st.bar_chart(hist_values)

st.write('Empleados por unidad')
barras_values = st.bar_chart(data[UNIT_COLUMN].value_counts())

HOMETOWN_COLUMN = 'Hometown'
employees_by_hometown = data.groupby('Hometown').mean()
Attrition_COLUMN = 'Attrition_rate'
st.write('Ciudades con mayor deserción')
lineas_values = st.line_chart(employees_by_hometown[Attrition_COLUMN])

