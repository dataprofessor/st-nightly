import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('🎈 `st.line_chart` demo')

df = pd.read_csv('seattle-weather.csv', parse_dates=['date'])

st.line_chart(df, x='date', y='temp_max') # plot one line
st.line_chart(df, x='date', y=['temp_max', 'temp_min', 'wind', 'precipitation']) # plot multiple lines
