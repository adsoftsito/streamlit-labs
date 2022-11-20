# Maria Y
import streamlit as st
import pandas as pd
import codecs
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    if nrows == 0:
        data = pd.read_csv(doc)
    else: 
        data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

@st.cache
def load_data_byName(valor,bandera):
    doc = codecs.open('Employees.csv','rU','UTF-8')
    data = pd.read_csv(doc)
    #lowercase = lambda x: str(x).lower()
    if bandera == 1:
        filtered_data_byname = data[data['Employee_ID'].str.contains(valor)]
    elif bandera == 2: 
        filtered_data_byname = data[data['Hometown'].str.contains(valor)]
    elif bandera == 3: 
        filtered_data_byname = data[data['Unit'].str.contains(valor)]
    elif bandera == 4: 
        filtered_data_byname = data[data['Education_Level'].astype(str).str.contains(str(valor))]   

    return filtered_data_byname

#6. Crear título de la aplicación, encabezados y descripción del proyecto
st.title("Reto | Análisis de deserción de empleados ")
st.write(f"El aplicativo permite acceder a la información del Hackathon HackerEarth 2020. Específicamente ala información de empleados, para analizar las causas de deserción.")

# 7. Crear un sidebar en la aplicación
sidebar = st.sidebar
sidebar.subheader("Puedes revisar la información o ver gráficas")
opciones = sidebar.radio(
  'Elige opción',
  ['Filtros','Gráficas'])


if opciones == 'Filtros':
    sidebar.title("Filtros de búsqueda")
    st.write(f"Tablas de datos")

    # 8. En sidebar crear un control checkbox que permita mostrar u ocultar el dataframe completo
    if sidebar.checkbox('Mostrar a todos los empleados'):
        sidebar.subheader('Todos los empleados')
        empleados = load_data(500) # cambiar a 500
        st.write(f"Todos los empleados")
        st.dataframe(empleados)

    # 9. Crear un buscador de empleados con cajas de texto y botones de comando
    # que permita buscar por Employee_ID, Hometown o Unit, mostrar dataframe con resultados
    # encontrados  y total de empleados
    sidebar.subheader("Búsqueda por palabra")
    opcBuscar = sidebar.radio(
      'Búsqueda',
      ['Employee_ID','Hometown','Unit'])
    buscar = sidebar.text_input('Ingresa el identificador de búsqueda:')
    btnBuscar = sidebar.button('Buscar')
    
    if(btnBuscar):
        if(opcBuscar == 'Employee_ID'):
            st.write(f"Filtro por empleado")
            filterbyname = load_data_byName(buscar,1)
            st.dataframe(filterbyname)
            count_row = filterbyname.shape[0]
            st.write(f"Total empleados : {count_row}")
        elif(opcBuscar == 'Hometown'):
            st.write(f"Filtro por ciudad")
            filterbyname = load_data_byName(buscar,2)
            st.dataframe(filterbyname)
            count_row = filterbyname.shape[0]
            st.write(f"Total ciudad natal : {count_row}")
        elif(opcBuscar == 'Unit'):
            st.write(f"Filtro por unidad")
            filterbyname = load_data_byName(buscar,3)
            st.dataframe(filterbyname)
            count_row = filterbyname.shape[0]
            st.write(f"Total unidades : {count_row}")

    sidebar.subheader("Búsqueda por selección")
    datos = load_data(0) #carga los datos para los selectbox

    # 10. En el sidebar incuir un control selectbox que permita filtrar a los empleados por su nivel educativo
    # mostrar el frame filtrado y totao de empleados

    educacion = sidebar.selectbox("Selecciona el nivel educativo", datos['Education_Level'].unique()) 
    btnEducacion = sidebar.button('Busca por nivel educativo: ')
    if(btnEducacion):
        st.write(f"Filtro por nivel educativo seleccionado")
        filterbyname = load_data_byName(educacion,4)
        st.dataframe(filterbyname)
        count_row = filterbyname.shape[0]
        st.write(f"Total por nivel educativo : {count_row}")

    # 11. En el sidebar incuir un control selectbox con las ciudades que participaron en el estudio
    # mostrar los empleados por ciudad en un dataframe filtrado y total de empleados

    ciudad = sidebar.selectbox("Selecciona la ciudad", datos['Hometown'].unique())
    btnCiudad = sidebar.button('Busca por ciudad: ')
    if(btnCiudad):
        st.write(f"Filtro por ciudad seleccionada")
        filterbyname = load_data_byName(ciudad,2)
        st.dataframe(filterbyname)
        count_row = filterbyname.shape[0]
        st.write(f"Total ciudades : {count_row}")

     #12. Crear un selectedbox para filtrar por la unidad funcional (Unit) a la que pertenece.

    funcional = sidebar.selectbox("Selecciona la unidad funcional", datos['Unit'].unique())
    btnFuncional = sidebar.button('Busca por unidad funcional: ')
    if(btnFuncional):
        st.write(f"Filtro por unidad seleccionada")
        filterbyname = load_data_byName(funcional,3)
        st.dataframe(filterbyname)
        count_row = filterbyname.shape[0]
        st.write(f"Total unidades funcionales : {count_row}")

#btnGraficas = sidebar.button('Consulta las gráficas')
if opciones == 'Gráficas':
    sidebar.title("Filtros de gráficas")  
    st.write(f"Gráficas")
    datos = load_data(0) #carga los datos para los selectbox

    opcionesGrafica = sidebar.radio(
    'Opciones de gráficas',
    ['Histograma de empleados por edad','Gráfica de frecuencias para las unidades funcionales','Ciudades Vs Indices de deserción','Edad Vs Indices de deserción','Relación de tiempo de servicio Vs Indices de deserción'])
    
    if opcionesGrafica == 'Histograma de empleados por edad':
        #13. Crear un histograma de los empleados agrupado por edad 
        st.write(f"Histograma de empleados por edad")
        fig, ax = plt.subplots()
        ax.hist(datos['Age'])
        st.pyplot(fig)
    elif opcionesGrafica == 'Gráfica de frecuencias para las unidades funcionales':
        #14. Crear una gráfica de frecuencias para las unidades funcionales (Unit) para conocer cuantos empleados hay por unidades
        st.write(f"Gráfica de frecuencias para las unidades funcionales")
        frec_values = datos[['Employee_ID','Unit']].groupby('Unit').count()
        st.bar_chart(frec_values)
    elif opcionesGrafica == 'Ciudades Vs Indices de deserción':
        #15. Analizar los datos con una gráfica que permita visualizar las ciudades (hometown) que tienen el mayor índice de deserción
        st.write(f"Ciudades Vs Indices de deserción")
        fig3, ax3 = plt.subplots() 
        hometown_Max = datos[['Attrition_rate','Hometown']].groupby('Hometown').max()
        st.bar_chart(hometown_Max)
        #ax3.plot(datos['Hometown'],datos['Attrition_rate'])
        #ax3.scatter(x=datos['Hometown'],y=datos['Attrition_rate'])
        #st.pyplot(fig3)
    elif opcionesGrafica == 'Edad Vs Indices de deserción':
        #16. Analizar la información con una gráfica que permita visualizar la edad y la tasa de deserción
        st.write(f"Edad Vs Indices de deserción")
        fig1, ax1 = plt.subplots()
        ax1.scatter(x=datos['Age'],y=datos['Attrition_rate'])
        st.pyplot(fig1)
    elif opcionesGrafica == 'Relación de tiempo de servicio Vs Indices de deserción':
        #17. Analizar con una  gráfica que determine la relación entre el tiempo de servicio y la tasa de deserción
        st.write(f"Relación de tiempo de servicio Vs Indices de deserción")
        fig2, ax2 = plt.subplots()
        ax2.scatter(x=datos['Time_of_service'],y=datos['Attrition_rate'])
        st.pyplot(fig2)
