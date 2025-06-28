import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
        "annio": [2019, 2020, 2021, 2022, 2023, 2024],
        "venta_cromos_101": [119.25, 141.28, 132.06, 205.33, 216.59, 157.51],
        "venta_cromos_102": [51.15, 90.39, 43.09, 178.21, 211.79, 450.28]
    })

print(df_ventas)

fig, ax = plt.subplots()

ax.plot(df_ventas['annio'], df_ventas['venta_cromos_101'], label='Cromos 101')
ax.plot(df_ventas['annio'], df_ventas['venta_cromos_102'], label='Cromos 102')
ax.legend(loc='upper left', fontsize=10, title='Leyenda', title_fontsize='13', shadow=True, frameon=True, facecolor='lightgray', edgecolor='black')

ax.set_xlabel('Años', fontsize=10, fontweight='bold', color='green')
ax.set_ylabel('Ventas (Dólares)', fontsize=10, fontweight='bold', color='green')
ax.set_title('Ventas en dólares de cromos del 2019 al 2024', fontsize=14, fontweight='bold', color='blue', ha='center', pad=20)

plt.show()