import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
        "annio": [2019, 2020, 2021, 2022, 2023, 2024],
        "venta_cromos_101": [119.25, 141.28, 132.06, 205.33, 216.59, 157.51],
        "venta_cromos_102": [51.15, 90.39, 43.09, 178.21, 211.79, 450.28]

    })

fig = plt.figure(figsize=(8,7))
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.75])
ax2 = fig.add_axes([0.17, 0.55, 0.3, 0.2]) 
ax1.plot(df_ventas['annio'], df_ventas['venta_cromos_101'], color='#ff7f0e')
ax2.plot (df_ventas['annio'], df_ventas['venta_cromos_102'], color='#bcbd22')
ax1.set_xlabel('Años')
ax1.set_ylabel('Venta (Dólares)')
ax1.set_title('Cromos 101', color='gray', fontweight='bold', ha='center')
ax2.set_title('Cromos 102', color='gray', fontweight='bold', ha='center')
fig.suptitle('Venta en dólares de cromos \nDel 2019 al 2024', fontsize=16, color='green', fontweight='bold', ha='center')
plt.show()