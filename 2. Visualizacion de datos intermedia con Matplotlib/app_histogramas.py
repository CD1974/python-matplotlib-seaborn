import matplotlib.pyplot as plt
import matplotlib.colors as mcolors  # <--- Agrega esta línea
import pandas as pd
import os

# Ruta absoluta al archivo temperaturas.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'temperaturas.csv')

df_temperaturas = pd.read_csv(csv_path, delimiter=",")

fig, ax = plt.subplots()

n, bins, patches = ax.hist(df_temperaturas["tmaxima"], bins=20, edgecolor="black")

# Normalizar los valores de temperatura para el colormap
norm = mcolors.Normalize(vmin=bins.min(), vmax=bins.max())  # <--- Usa mcolors aquí
cmap = plt.get_cmap('coolwarm')  # Puedes elegir otro colormap si prefieres

for bin_left, bin_right, patch in zip(bins[:-1], bins[1:], patches):
    color = cmap(norm((bin_left + bin_right) / 2))
    patch.set_facecolor(color)

ax.set_xlabel("Temperatura (°C)")
ax.set_ylabel("Frecuencia")
ax.set_title("Temperaturas Máximas Diarias \n (Agosto - Septiembre 2023)", color="blue", fontweight='bold', pad=5)
plt.show()