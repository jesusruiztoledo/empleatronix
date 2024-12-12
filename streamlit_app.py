import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

df = pd.read_csv('./data/employees.csv')

st.title('Employee Data')

st.write(df)
st_echarts(options={
    'xAxis': {
        'type': 'category',
        'data': df['salary'].tolist()
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [{
        'data': df['salary'].tolist(),
        'type': 'bar'
    }],
    'title': {'text': 'Employee Salary'}
})