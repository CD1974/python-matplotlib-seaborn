import os
import matplotlib.pyplot as plt
import pandas as pd

# Ruta absoluta al archivo empleados.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'empleados.csv')

df_empleados = pd.read_csv(csv_path, delimiter=",")

fig, ax = plt.subplots()

ax.scatter(df_empleados['Experiencia'], df_empleados['Salario'], color='gray')
ax.set_xlabel('Experiencia Laboral (años)')
ax.set_ylabel('Salario (Dólares)')
ax.set_title('Experiencia Laboral vs Salario', fontsize=16, color='olivedrab', fontweight='bold', pad=20)
plt.show()