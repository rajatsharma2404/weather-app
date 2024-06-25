import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place")

days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 help="Select number of days for forecast")


option = st.selectbox('Select data to view', ["Temperature","Sky"])




if place:
    try:

        filtered_data = get_data(place=place, forecast_days=days)
        st.header(f"{option.capitalize()} for the next {days} days in {place}")
        if option == "Temperature":
            temperature = [dict['main']["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Days", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear" : "images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            images = [images[weather] for weather in sky]
            dates = [dict["dt_txt"] for dict in filtered_data]
            st.image(image=images, width=150)
    except KeyError:
        st.text("Enter correct city")












