import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.header('🎈 `st.line_chart` demo')

st.subheader('Settings')
plot_height = st.sidebar.slider("Select the plot's height", 100, 500, 250)
plot_data = st.sidebar.multiselect(
     'Select data to plot',
     ['temp_min', 'temp_max', 'precipitation', 'wind'],
     ['temp_min', 'temp_max'])
df = pd.read_csv('seattle-weather.csv', parse_dates=['date'])

st.subheader('Plot')
st.line_chart(df, x = 'date', y = plot_data, height = plot_height)
