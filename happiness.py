import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In search for Happiness.")

col1 = st.selectbox('Select data for X-axis',["GDP","Happiness","Generosity"])

col2 = st.selectbox('Select data for Y-axis',["GDP","Happiness","Generosity"])

df = pd.read_csv("happy.csv")

data1 = df[col1.lower()]
data2 = df[col2.lower()]



st.header(f"{col1} vs {col2}")


figure = px.line(x=data1, y=data2, labels={"x" : "Days", "y" : "Temperature"})

st.plotly_chart(figure)