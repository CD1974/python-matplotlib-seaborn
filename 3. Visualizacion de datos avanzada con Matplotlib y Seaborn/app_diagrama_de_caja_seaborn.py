import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame(
    {
        "cromos": ["Cromo 101", "Cromo 102"] * 6,
        "ventas": [100, 150, 200, 123,258, 156,369, 212,567, 234,123, 890],
    }
)

fig, ax = plt.subplots(figsize=(6,7)) 
sns.boxplot(x='cromos', y='ventas', data=df_ventas, palette='deep')

ax.set_xlabel('Producto')
ax.set_ylabel('Venta Semestre (Dólares)')
ax.set_title('Venta en dólares de cromos \n Primer semestre de 2023', 
             fontsize=16, 
             color='green', 
             fontweight='bold',
            ha='center', 
            pad=20)

plt.show()