import matplotlib.pyplot as plt
import pandas as pd

df_empleados = pd.read_csv('../../empleados.csv', delimiter=";")

fig, ax = plt.subplots()

ax.scatter(df_empleados['Experiencia'], df_empleados['Salario'], color='gray')

ax.set_xlabel('Experiencia Laboral (años)')
ax.set_ylabel('Salario (Dólares)')
ax.set_title('Experiencia Laboral vs Salario', fontsize=16, color='olivedrab', fontweight='bold', pad=20)
plt.show()