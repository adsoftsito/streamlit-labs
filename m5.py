# lucia moreno
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import codecs

st.title('Attrition rate')
st.write("En el presente proyecto se podrán visualizar datos referentes a la tasa deserción de un universo de empleados de manera interactiva ")

DATE_COLUMN = 'started_at'
DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return employees

def filter_data_by_ID(ID):
    filter_data_by_ID = employees[employees['Employee_ID'].str.upper().str.contains(ID)]
    return filter_data_by_ID

def filter_data_by_Hometown(Hometown):
    filter_data_by_Hometown = employees[employees['Hometown'].str.upper().str.contains(Hometown)]
    return filter_data_by_Hometown

def filter_data_by_Unit(Unit):
    filter_data_by_Unit = employees[employees['Unit'].str.upper().str.contains(Unit)]
    return filter_data_by_Unit

def filter_data_by_educ(education):
    filter_data_by_educ = employees[employees['Education_Level'] == education]
    return filter_data_by_educ

def filter_data_by_Ciudad(Ciudad):
    filter_data_by_Ciudad = employees[employees['Hometown'] == Ciudad]
    return filter_data_by_Ciudad

def filter_data_by_U_(Unit):
    filter_data_by_U_ = employees[employees['Unit'] == Unit]
    return filter_data_by_U_

employees = load_data(7000)

if st.sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los empleados')
    count_row = employees.shape[0]  # Gives number of rows
    st.write(f"Total empleados mostrados : {count_row}")
    st.write(employees)

ID_filter = st.sidebar.text_input('ID empleado')
btnBuscarID = st.sidebar.button('Buscar ID')

if (btnBuscarID):
   data_id = filter_data_by_ID(ID_filter.upper())
   count_row = data_id.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_id)

HT_filter = st.sidebar.text_input('Ciudad de origen del empleado')
btnBuscarHT = st.sidebar.button('Buscar Hometown')

if (btnBuscarHT):
   data_ht = filter_data_by_Hometown(HT_filter.upper())
   count_row = data_ht.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_ht)

Unit_filter = st.sidebar.text_input('Unidad del empleado')
btnBuscarUnit = st.sidebar.button('Buscar Unidad')

if (btnBuscarUnit):
   data_Unit = filter_data_by_Unit(Unit_filter.upper())
   count_row = data_Unit.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_Unit)

selected_educ = st.sidebar.selectbox("Seleccionar Nivel Educativo", employees['Education_Level'].unique())
btnFilterbyNE = st.sidebar.button('Filtrar NE ')

if (btnFilterbyNE):
   filterbyNE = filter_data_by_educ(selected_educ)
   count_row = filterbyNE.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbyNE)

selected_city = st.sidebar.selectbox("Seleccionar Ciudad", employees['Hometown'].unique())
btnFilterbycity = st.sidebar.button('Filtrar Ciudad')

if (btnFilterbycity):
   filterbycity = filter_data_by_Ciudad(selected_city)
   count_row = filterbycity.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbycity)

selected_unit = st.sidebar.selectbox("Seleccionar Unit", employees['Unit'].unique())
btnFilterbyunit = st.sidebar.button('Filtrar Unit')

if (btnFilterbyunit):
   btnFilterbyunit = filter_data_by_U_(selected_unit)
   count_row = btnFilterbyunit.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(btnFilterbyunit)

st.markdown("___")
fig1, ax = plt.subplots()
ax.hist(employees.Age)
st.header("Empleados por edad")
st.write("Existe una mayor proporción de la distribución en el rango de 20 a 30 años")
st.pyplot(fig1)

st.markdown("___")

fig2, ax2 = plt.subplots()
sns.countplot(employees['Unit'], ax = ax2)
plt.xticks(rotation=90)
st.header("Empleados por Unidad funcional")
st.write("La unidad que tiene más empleados es IT")
st.pyplot(fig2)

st.markdown("___")

employees_by_hometown = employees.groupby('Hometown').mean()
fig3, ax3 = plt.subplots()
employees_by_hometown['Attrition_rate'].plot(title='Attrition_rate',ax=ax3)
st.header("Deserción promedio por ciudad")
st.write("La ciudad que tiene mayor deserción promedio es Springfield")
st.pyplot(fig3)

st.markdown("___")

fig4, ax4 = plt.subplots()
sns.scatterplot(x=employees['Age'],y=employees['Attrition_rate'], ax = ax4)
st.header("Tasa de deserción por edad")
st.write("La deserción es mayor en empleados menores de los 30 años de edad")
st.pyplot(fig4)

st.markdown("___")

fig5, ax5 = plt.subplots()
sns.scatterplot(x=employees['Time_of_service'],y=employees['Attrition_rate'])
st.header("Tasa de deserción por tiempo de servicio")
st.write("La tasa de deserción tiene una tendencia decreciente en años de servicio mayores a los 10 años")
st.pyplot(fig5)
