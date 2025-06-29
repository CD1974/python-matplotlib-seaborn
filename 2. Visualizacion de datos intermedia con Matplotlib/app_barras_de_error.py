import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta absoluta al archivo temperaturas.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'altura_peso.csv')

# Cargar el DataFrame desde el archivo CSV
df_altura_peso = pd.read_csv(csv_path, delimiter=";")

etiquetas = [i + 1 for i in range(len(df_altura_peso['altura']))]

fig, ax = plt.subplots()
ax.bar(etiquetas, df_altura_peso['altura'], yerr=0.05, capsize=5, color='olivedrab')

ax.set_xlabel('Persona')
ax.set_ylabel('Altura(m)')
ax.set_title('Altura de personas con barras de error', color='olivedrab', fontweight='bold', pad=20)
plt.show()