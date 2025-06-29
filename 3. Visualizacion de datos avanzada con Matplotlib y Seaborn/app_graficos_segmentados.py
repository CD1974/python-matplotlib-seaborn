import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102'],
    'trimestre': ['T1', 'T1',  'T2', 'T2',  'T3', 'T3', 'T4', 'T4'],
    'ventas': [100, 150, 200, 123, 258, 156, 369, 212]
  })

g = sns.FacetGrid(df_ventas, col="trimestre", col_wrap=2, height=4)
g.map(sns.barplot, "cromos", "ventas", order=['Cromo 101', 'Cromo 102'],palette="deep")
g.set_titles(col_template="Distribución de ventas en el trimestre {col_name}")
g.set_axis_labels("Cromo", "Venta (Dólares)")
plt.show()