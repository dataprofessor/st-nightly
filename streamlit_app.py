import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.header('🎈 `st.line_chart` demo')

plot_height = st.slider("Select the plot's height", 100, 500, 250)
df = pd.read_csv('seattle-weather.csv', parse_dates=['date'])

st.line_chart(df, x='date', y='temp_max', height = plot_height) # plot one line
st.line_chart(df, x='date', y=['temp_max', 'temp_min', 'wind', 'precipitation']) # plot multiple lines
