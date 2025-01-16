import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Información de vehículos')

data = pd.read_csv('./vehicles_us.csv') # leer los datos

hist_checkbox = st.checkbox('Construir histograma para la columna de odómetro') # crear una casilla de verificación
        
if hist_checkbox: # al hacer click en la casilla
    # escribir un mensaje
    st.write('Histograma para la columna de odómetro')
            
    # crear un histograma
    fig_hist = px.histogram(data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)


disp_checkbox = st.checkbox('Construir diagrama de dispersión odómetro vs precio') # crear una casilla de verificación

if disp_checkbox: # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Diagrama de dispersión para las columnas de odómetro y precio')
       
    fig_cylinders = px.scatter(data, x="odometer", y="price", title='Precio vs cantidad de cilindros del vehículo') # crear un gráfico de dispersión
    
    st.plotly_chart(fig_cylinders, use_container_width=True)


year_checkbox = st.checkbox('Construir diagrama de dispersión precio vs año') # crear una casilla de verificación

if year_checkbox: # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Diagrama de dispersión para las columnas de precio y año')
       
    fig_year = px.scatter(data, x="model_year", y="price", title='Precio vs año del vehículo') # crear un gráfico de dispersión
    
    st.plotly_chart(fig_year, use_container_width=True)

fuel_checkbox=st.checkbox('Creación de un diagrama de caja para las columnas de precio y combustible')# crear una casilla de verificación

if fuel_checkbox:
    # escribir un mensaje
    st.write('Diagrama de dispersión para las columnas de precio y combustible')
       
    fig_fuel = px.box(data, x="fuel", y="price", title='Precio vs combustible del vehículo') # crear un gráfico de dispersión
    
    st.plotly_chart(fig_fuel, use_container_width=True)
    
