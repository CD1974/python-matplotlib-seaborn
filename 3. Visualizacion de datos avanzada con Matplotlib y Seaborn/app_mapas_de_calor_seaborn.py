import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102'],
    'trimestre': ['T1', 'T1',  'T2', 'T2',  'T3', 'T3', 'T4', 'T4'],
    'ventas': [100, 150, 200, 123, 258, 156, 369, 212]
  })

pivot_table_ventas = df_ventas.pivot_table(values='ventas', index='cromos', columns='trimestre', aggfunc='sum')
fig, ax = plt.subplots()

sns.heatmap(pivot_table_ventas, cmap='BuPu', cbar_kws={'label': 'Total de Ventas'})
ax.set_xlabel('Trimestre')
ax.set_ylabel('Cromo')
ax.set_title('Venta en dólares de cromos en el 2023', color='green', fontweight='bold', ha='center', pad=20)

plt.show()