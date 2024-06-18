import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place")

days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 help="Select number of days for forecast")


data = st.selectbox('Select data to view', ["Temperature","Sky"])

st.header(f"{data} for the next {days} days in {place}")


