import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset

daily_sales = pd.read_csv("daily_sales.csv")
forecast_df = pd.read_csv("sales_forecast.csv")

daily_sales['Date'] = pd.to_datetime(daily_sales['Date'])
forecast_df['Date'] = pd.to_datetime(forecast_df['Date'])

st.title("Sales Forecast Dashboard")

# KPI

st.subheader("Buisness Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Average Sales",f"{daily_sales["Sales"].mean():,.0f}")

col2.metric("Maximum Sales",f"{daily_sales["Sales"].max():,.0f}")

col3.metric("Forecast Average",f"{forecast_df["Forecasted_Sales"].mean():,.0f}")

# Historical Sales

st.subheader("Historical Sales")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(daily_sales['Date'],daily_sales['Sales'])

ax.set_title("Historical Sales")

st.pyplot(fig)

# Forecast

st.subheader("30 days Forecasted Sales")

fig, ax = plt.subplots(figsize = (10,5))

ax.plot(forecast_df["Date"],forecast_df["Forecasted_Sales"],marker = "o")

ax.set_title("Forecasted Sales")

st.pyplot(fig)

# Combined Graph

st.subheader("Historical vs Forecast")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(daily_sales['Date'],daily_sales['Sales'],label='Historical')

ax.plot(forecast_df['Date'],forecast_df['Forecasted_Sales'],label='Forecast')

ax.legend()

st.pyplot(fig)

# Forecast Table

st.subheader("Forecast Table")

st.dataframe(forecast_df)