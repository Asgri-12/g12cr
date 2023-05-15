# import module
import streamlit as st
import pandas as pd
import numpy as np

st.title("Statistics")
st.subheader("Male VS Female")
chart_data = pd.DataFrame({
    'index': ['Male', 'Female'], 'Total Count': [2250, 1873]}).set_index('index')

st.bar_chart(chart_data)

st.subheader("UAE VS Non-UAE")
data2 = {'UAE': 1105, 'Non-UAE': 3018}
chart_data2 = pd.DataFrame({
    'index': ['UAE', 'Non-UAE'], 'Total Count': [1105, 3018]}).set_index('index')
st.bar_chart(chart_data2)

st.subheader('Cancer Type Distribution')

chart_data3 = pd.DataFrame({
    'index': ['Leukemia', 'Colorectal','Prostate','Non-Hodgkins','Brain cancer','Breast', 'Thyroid'],
    'Total Count': [314, 422,155,172,76,834,412]}).set_index('index')

st.area_chart(chart_data3)
