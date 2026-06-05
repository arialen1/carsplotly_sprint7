import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# --- Encabezado ---
st.title('Análisis de Anuncios de Venta de Coches en EE.UU.')
st.write('Explora la distribución del odómetro y la relación entre precio y kilometraje en el mercado de vehículos usados.')

# --- Histograma ---
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de dispersión ---
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el odómetro y el precio de los vehículos')
    fig2 = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(size=4, opacity=0.4, color='steelblue')
    )])
    fig2.update_layout(
        title_text='Precio vs. Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig2, use_container_width=True)
