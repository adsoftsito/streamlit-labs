# Arely

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.title('APLICACIÓN WEB DE CIENCIA DE DATOS')
st.header("Análisis del archivo --Employees.csv--")
st.write("""Este es el 5o reto de aplicación del diplomado --Data Science and AI: 
Del Concepto a Desarrollo de Aplicaciones - Live--, analizaremos a través de Streamlit 
el archivo --Employees.csv--.""")

data_url = ('employees.csv')

@st.cache
def emp_data():
    employees = pd.read_csv(data_url)
    return employees

employees_state = st.text('Loading data ...')
employees = emp_data()
employees_state.text("File upload completed, we're using st.cache!")


if st.sidebar.checkbox('Show complete file --Employees.csv--'):
    st.subheader('Employees.csv')
    count_row = employees.shape[0]  
    st.write(f"Total de registros: {count_row}")
    st.write(employees)

@st.cache
def filter_by_employeeid(employeeid):
    filtered_employeeid = employees[employees['Employee_ID'].str.upper().str.contains(employeeid)]
    return filtered_employeeid

@st.cache
def filter_by_hometown(hometown):
    filtered_hometown = employees[employees['Hometown'].str.upper().str.contains(hometown)]
    return filtered_hometown

@st.cache
def filter_by_unit(unit):
    filtered_unit = employees[employees['Unit'].str.upper().str.contains(unit)]
    return filtered_unit

@st.cache
def filter_by_edlevel(edlevel):
    filtered_level= employees[employees['Education_Level'] == edlevel]
    return filtered_level

@st.cache
def filter_by_ht(ht):
    filtered_level= employees[employees['Hometown'] == ht]
    return filtered_level

@st.cache
def filter_by_ut(ut):
    filtered_unit = employees[employees['Unit'] == ut]
    return filtered_unit

browser_emp = st.sidebar.text_input('Employee_ID :')
btnsearch_emp = st.sidebar.button('Buscar empleado')

if (btnsearch_emp):
   data_emp = filter_by_employeeid(browser_emp.upper())
   count_row = data_emp.shape[0]  
   st.write(f"Total de empleados : {count_row}")
   st.write(data_emp)

browser_ht = st.sidebar.text_input('Hometown :')
btnsearch_ht = st.sidebar.button('Buscar lugar de procedencia')

if (btnsearch_ht):
   data_ht = filter_by_hometown(browser_ht.upper())
   count_row = data_ht.shape[0]  
   st.write(f"Total de empleados : {count_row}")
   st.write(data_ht)

browser_unit = st.sidebar.text_input('Unit :')
btnsearch_unit = st.sidebar.button('Buscar unidad funcional')

if (btnsearch_unit):
   data_unit = filter_by_unit(browser_unit.upper())
   count_row = data_unit.shape[0]  
   st.write(f"Total de empleados : {count_row}")
   st.write(data_unit)

selected_edlevel = st.sidebar.selectbox("Seleccionar Nivel Edicativo", employees['Education_Level'].unique())
btnedlevel = st.sidebar.button('Filtrar nivel educativo')

if (btnedlevel):
   filterbyedlevel = filter_by_edlevel(selected_edlevel)
   count_row = filterbyedlevel.shape[0] 
   st.write(f"Total de empleados : {count_row}")
   st.dataframe(filterbyedlevel)

selected_ht = st.sidebar.selectbox("Seleccionar Nivel Edicativo", employees['Hometown'].unique()) 
btn_ht = st.sidebar.button('Filtrar lugar de procedencia')

if (btn_ht):
   data_ht = filter_by_ht(selected_ht)
   count_row = data_ht.shape[0]  
   st.write(f"Total de empleados : {count_row}")
   st.write(data_ht)

selected_ut = st.sidebar.selectbox("Seleccionar Unidad Funcional", employees['Unit'].unique()) 
btn_ut = st.sidebar.button('Filtrar unidad funcional')

if (btn_ut):
   data_ut = filter_by_ut(selected_ut)
   count_row = data_ut.shape[0]  
   st.write(f"Total de empleados : {count_row}")
   st.write(data_ut)

st.write("*Histograma de edades de los empleados*")
hist_ages =  employees[['Age','Employee_ID']].groupby('Age').count()
st.bar_chart(hist_ages) 

st.write("*Gráfica de frecuencias de las unidades funcionales*")
bar_unit = employees[['Unit','Employee_ID']].groupby('Unit').count()
st.bar_chart(bar_unit) 

st.write("*Índice de diserción por ciudad*")
att_index = employees[['Attrition_rate','Hometown']].groupby('Hometown').mean()
st.bar_chart(att_index) 

st.write("*Gráfica de edades y tasa de deserción*")
fig_age_att = px.scatter(employees, x = "Age", y = "Attrition_rate")
st.plotly_chart(fig_age_att)

st.write("*Gráfica de tiempo de servicio y tasa de deserción*")
fig_ts_att = px.scatter(employees, x = "Time_of_service", y = "Attrition_rate")
st.plotly_chart(fig_ts_att)
