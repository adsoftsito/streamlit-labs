# manuel.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

names_link = 'Employees.csv'
names_data = pd.read_csv(names_link,nrows=500)

sidebar = st.sidebar

st.title("Modulo 5 Streamlit")
st.header("Employees")
st.text("Analisando datos")

sidebar.title("Sidebar")
showHide = sidebar.checkbox("Mostrar DataFrame")

if showHide:
  st.dataframe(names_data)


def load_data_bytitle(title):
    print(title)
    print(names_data['Hometown'].head(1).str.upper())
    filtered_data_bytit = names_data[names_data['Hometown'].str.upper().str.contains(title) | names_data['Unit'].str.upper().str.contains(title) | names_data['Employee_ID'].str.upper().str.contains(title)]
    print(filtered_data_bytit)
    return filtered_data_bytit	


tit = sidebar.text_input("Buscar")

if (tit):
  print(tit)
  filterbytitle = load_data_bytitle(tit.upper())
  count_row = filterbytitle.shape[0]
  st.title('Coincidencias')
  st.write(f"Total Titles: {count_row}")
  st.dataframe(filterbytitle)

selected_sex = sidebar.selectbox("Nivel educativo", names_data['Education_Level'].unique())
selected_unit = sidebar.selectbox("Unit", names_data['Unit'].unique())
selected_city = sidebar.selectbox("Ciudad", names_data['Hometown'].unique())

@st.cache
def load_data_edl(dat):
  filtered_data_byDir = names_data[names_data["Education_Level"] == dat]
  return filtered_data_byDir

@st.cache
def load_data_unit(dat):
  filtered_data_byDir = names_data[names_data["Unit"] == dat]
  return filtered_data_byDir

@st.cache
def load_data_city(dat):
  filtered_data_byDir = names_data[names_data["Hometown"] == dat]
  return filtered_data_byDir

if selected_sex:
	filterbydir = load_data_edl(selected_sex)
	count_row = filterbydir.shape[0]
	st.write(f"Total Items: {count_row}")
	st.dataframe(filterbydir)
	st.markdown("___")

if selected_unit:
	filterbydir = load_data_unit(selected_unit)
	count_row = filterbydir.shape[0]
	st.write(f"Total Items: {count_row}")
	st.dataframe(filterbydir)
	st.markdown("___")

if selected_city:
	filterbydir = load_data_city(selected_city)
	count_row = filterbydir.shape[0]
	st.write(f"Total Items: {count_row}")
	st.dataframe(filterbydir)
	st.markdown("___")

#Edad
fig, ax = plt.subplots()
plt.title("Edad Histograma")
ax.hist(names_data["Age"], bins=20)
st.pyplot(fig)

#Unit
fig2, ax2 = plt.subplots()
plt.title("Unidad Histograma")
ax2.hist(names_data.groupby('Unit').size(), bins=20)
st.pyplot(fig2)

#Ciudad
ht = names_data[['Hometown','Attrition_rate']].groupby('Hometown').max()
fig3, ax3 = plt.subplots()
plt.title("Ciudad con tasa de desercion Histograma")
ax3.hist(ht['Attrition_rate'], bins=20)
st.pyplot(fig3)

#Edad
edad = names_data[['Age','Attrition_rate']].groupby('Age').max()
fig4, ax4 = plt.subplots()
plt.title("Edad con tasa de desercion Histograma")
ax4.hist(edad['Attrition_rate'], bins=20)
st.pyplot(fig4)

#Tiempo de servicio
tiempo = names_data[['Time_of_service','Attrition_rate']].groupby('Time_of_service').max()
fig5, ax5 = plt.subplots()
plt.title("Tiempo de servicio con tasa de desercion Histograma")
ax5.hist(tiempo['Attrition_rate'], bins=20)
st.pyplot(fig5)
