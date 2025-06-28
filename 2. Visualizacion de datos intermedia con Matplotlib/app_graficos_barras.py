import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102'],
    'trimestre': ['T1', 'T1',  'T2', 'T2',  'T3', 'T3', 'T4', 'T4'],
    'ventas': [100, 150, 200, 123, 258, 156, 369, 212]
})

fig, ax = plt.subplots()
df_trimestre_cromos = df_ventas.groupby(['trimestre', 'cromos']).sum()['ventas'].unstack()

df_trimestre_cromos.plot(kind='bar', ax=ax, color=['rosybrown', 'gray'])
ax.set_xlabel('Trimestre')
ax.set_ylabel('Ventas (Dólares)')
ax.legend(title='Cromos', loc='upper left')

# Cambia la rotación de las etiquetas del eje X a horizontal
ax.set_xticklabels(df_trimestre_cromos.index, rotation=0)

ax.set_title('Ventas de cromos por trimestre 2023', fontsize=16, color='blue', fontweight='bold', pad=20)
plt.show()