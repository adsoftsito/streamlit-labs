#Roberto

import pandas as pd 
import streamlit as st 

st.title("Reto de aplicación web")
st.header("Dashboard")
st.write("Texto")




names_data = pd.read_csv('Employees.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_emp(emp):
    filtered_data_emp = data[data['Employee_ID'].str.upper().str.contains(emp)]
    return filtered_data_emp

def filter_data_by_emp(employee):
    filtered_data_emp = data[data['Employee_ID'] == employee]
    return filtered_data_employee


import codecs

data_load_state = st.text('Loading cicle nyc data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Mostrar a todos los empleados'):
    st.subheader('Todos los filmes')
    st.write(data)



buscador = st.sidebar.text_input('Employee_ID, Hometown o Unit :')
btnBuscar = st.sidebar.button('Buscar')

if (btnBuscar):
   data_emp = filter_data_by_emp(buscador.upper())
   count_row = data_emp.shape[0]  # Gives number of rows
   st.write(f"Resulltado : {count_row}")
   st.write(data_emp)

selected_buscador = st.sidebar.selectbox("Seleccionar Empleado", data['Employee_ID'].unique())
btnFilterbyEmpleado = st.sidebar.button('Filtrar empleado ')

if (btnFilterbyEmpleado):
   filterbyempl = filter_data_by_employee(selected_employee)
   count_row = filterbyempl.shape[0]  # Gives number of rows
   st.write(f"Total employees : {count_row}")



st.dataframe(names_data)
