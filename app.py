import streamlit as st
import numpy as np
import pandas as pd

st.title("Хистограма на случайни числа (0 - 69)")

# Плъзгач за броя стойности
num_values = st.slider("Брой стойности:", 10, 1000, 100)

# Генериране на данни
data = np.random.randint(0, 70, size=num_values)

# Преобразуване в pandas серия и броене на честоти
hist_data = pd.Series(data).value_counts().sort_index()

# Показване като хистограма (бар чарт)
st.bar_chart(hist_data)

