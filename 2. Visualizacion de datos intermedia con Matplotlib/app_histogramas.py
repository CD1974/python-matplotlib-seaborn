import os

import pandas as pd
import matplotlib.pyplot as plt

# Ruta absoluta al archivo temperaturas.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'temperaturas.csv')

df_temperaturas = pd.read_csv("temperaturas.csv", delimiter=";")

fig, ax = plt.subplots()

ax.hist(df_temperaturas["tMaxima"], bins=20, color="blue", edgecolor="black")

ax.set_xlabel("Temperatura (°C)")
ax.set_ylabel("Frecuencia")
ax.set_title("Temperaturas Máximas Diarias \n (Agosto - Septiembre 2023)", color="blue", fontweight='bold', pad=5)
plt.show()