import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/employees.csv')

# Título de la aplicación
st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Mostrar la tabla
st.dataframe(df)

# Barra de separación
st.write("___")

# Crear columnas para alinear los widgets horizontalmente
col1, col2, col3 = st.columns(3)

with col1:
    bar_color = st.color_picker("Color", "#1f77b4")

with col2:
    display_names = st.toggle("Mostrar el nombre", value=True)

with col3:
    display_salaries = st.toggle("Mostrar sueldo en la barra", value=False)

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["full name"], df["salary"], color=bar_color)
ax.set_xlabel("Salario")
ax.set_ylabel("Empleado")
ax.set_title("Salarios de los empleados")

if display_salaries:
    for index, value in enumerate(df["salary"]):
        ax.text(value, index, f"{value}", va='center')

if display_names:
    plt.yticks(range(len(df)), df["full name"])
else:
    plt.yticks(range(len(df)), [''] * len(df))

st.pyplot(fig)

st.write("© Jesús Ruiz Toledo - CPIFP Alan Turing")