import streamlit as st
import pandas as pd
import plotly.express as px

DataFrame = pd.read_csv("C:/Users/USUARIO/Desktop/ESCRITORIO/CURSO DE TRIPLETEN/Sprint7PJSL/vehicles_us.csv")

st.header("Proyecto Sprint 7")
Boton = st.button("Construir un Histograma")
Boton2 = st.checkbox("Construir grafico de dispersion")
if Boton:
    st.write("Creacion del histograma")
    hist = px.histogram(DataFrame,x = "odometer")
    st.plotly_chart(hist,use_container_width=True)

if Boton2:
    st.write("Construyendo el grafico de dispersion")
    hist2= px.scatter(DataFrame,x="odometer", y ="price")
    st.plotly_chart(hist2,use_container_width=True)

