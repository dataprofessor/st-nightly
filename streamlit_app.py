import streamlit as st

st.header('🎈 App Name')

st.line_chart(df, x="column1", y="column2") # plot one line
st.line_chart(df, x="column1", y=["column2", "column3"]) # plot multiple lines
