import requests
import streamlit as st
import matplotlib.pyplot as plt

API_KEY = "19fdff6d73005aac85b9d921cd7b0131"

st.title("🌦 Weather Dashboard")

city = st.text_input("Enter City Name", "Dhanbad")

if st.button("Get Weather Data"):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    data = response.json()

    dates = []
    temps = []
    humidity = []

    for item in data["list"][:10]:
        dates.append(item["dt_txt"])
        temps.append(item["main"]["temp"])
        humidity.append(item["main"]["humidity"])

    # Temperature graph
    fig1, ax1 = plt.subplots()
    ax1.plot(dates, temps, marker='o')
    ax1.set_title("Temperature Trend")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("°C")
    plt.xticks(rotation=45)

    st.pyplot(fig1)

    # Humidity graph
    fig2, ax2 = plt.subplots()
    ax2.plot(dates, humidity, marker='o')
    ax2.set_title("Humidity Trend")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("%")
    plt.xticks(rotation=45)

    st.pyplot(fig2)

    st.success("Data Loaded Successfully!")
