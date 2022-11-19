# Juan Pablo
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Nu - Kaizen')
st.header('Data')
st.write("""

"Improving quality requires a culture change, not just a new diet" - Philip B. Crosby

""")

DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data 
data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text('Juan Pablo Alvarez Heredia')
#----------------------------------------------
@st.cache

def load_data_byemployee(Employee_ID):    
    data = pd.read_csv(DATA_URL)
    filtered_data_byemployee = data[data['Employee_ID'].str.contains(Employee_ID)]
    return filtered_data_byemployee   

def load_data_byhometown(Hometown):    
    data = pd.read_csv(DATA_URL)
    filtered_data_byhometown = data[data['Hometown'].str.contains(Hometown)]
    return filtered_data_byhometown  

def load_data_byunit(Unit):    
    data = pd.read_csv(DATA_URL)
    filtered_data_byunit = data[data['Unit'].str.contains(Unit)]
    return filtered_data_byunit  

def filter_data_by_level(Education_Level):
    filtered_data_level = data[data['Education_Level'] == Education_Level]
    return filtered_data_level

def filter_data_by_hometown(Hometown):
    filtered_data_hometown = data[data['Hometown'] == Hometown]
    return filtered_data_hometown

def filter_data_by_unit(Unit):
    filtered_data_unit = data[data['Unit'] == Unit]
    return filtered_data_unit
#----------------------------------------------
if st.sidebar.checkbox('Mostrar Data'): #checkbox
    st.subheader('BDX')
    st.write(data)

#----------------------------------------------
selected_level = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbylevel = st.sidebar.button('Filtrar N')

if (btnFilterbylevel):
   filterbylevel = filter_data_by_level(selected_level)
   count_row = filterbylevel.shape[0]  # Gives number of rows
   st.write(f"Total names : {count_row}")

   st.dataframe(filterbylevel)

selected_hometown = st.sidebar.selectbox("Seleccionar Ciudad", data['Hometown'].unique())
btnFilterbyhometown = st.sidebar.button('Filtrar C')

if (btnFilterbyhometown):
   filterbyhometown = filter_data_by_hometown(selected_hometown)
   count_row = filterbyhometown.shape[0]  # Gives number of rows
   st.write(f"Total names : {count_row}")

   st.dataframe(filterbyhometown)

selected_unit = st.sidebar.selectbox("Seleccionar Área", data['Unit'].unique())
btnFilterbyunit = st.sidebar.button('Filtrar A')

if (btnFilterbyunit):
   filterbyunit = filter_data_by_unit(selected_unit)
   count_row = filterbyunit.shape[0]  # Gives number of rows
   st.write(f"Total names : {count_row}")

   st.dataframe(filterbyunit)
#-----------------------------------------------------
busqueda = st.sidebar.text_input('Buscar:') #sidebar
btnBuscar = st.sidebar.button('Buscar')

myname = busqueda
if (myname):
    filterbyemployee = load_data_byemployee(myname)
    count_row = filterbyemployee.shape[0]  #Gives number of rows
    st.write(f'Total names :{count_row}')
    st.dataframe(filterbyemployee)
if (myname):
    filterbyhometown = load_data_byhometown(myname)
    count_row = filterbyhometown.shape[0]  #Gives number of rows
    st.write(f'Total names :{count_row}')
    st.dataframe(filterbyhometown)
if (myname):
    filterbyunit = load_data_byunit(myname)
    count_row = filterbyunit.shape[0]  #Gives number of rows
    st.write(f'Total names :{count_row}')
    st.dataframe(filterbyunit)

#Gráficas----------------------------------------------
sns.histplot(x=data['Age'])
# sns.countplot(data['Unit'])
plt.xticks(rotation=90)
