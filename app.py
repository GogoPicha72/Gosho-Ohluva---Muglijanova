import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Заглавие
st.title("Хистограма на случайни числа (0 - 69)")

# Генериране на случайни числа
num_values = st.slider("Брой случайни стойности:", min_value=10, max_value=1000, value=100)
data = np.random.randint(0, 70, size=num_values)

# Показване на генерираните данни
st.write("Генерирани числа:", data)

# Създаване на хистограма
fig, ax = plt.subplots()
ax.hist(data, bins=range(0, 71, 5), edgecolor='black')  # стъпка през 5
ax.set_title("Хистограма на случайни цели числа")
ax.set_xlabel("Стойности")
ax.set_ylabel("Честота")

# Показване в Streamlit
st.pyplot(fig)
