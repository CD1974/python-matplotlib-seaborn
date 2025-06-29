import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
    'annio': [2019, 2020, 2021, 2022, 2023, 2024],
    'precio_cromo': [150, 210, 250, 320, 350, 400],
    'unidades': [12, 23, 20, 52, 45, 10]
   })

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(
    df_ventas['annio'], 
    df_ventas['precio_cromo'], 
    df_ventas['unidades'], color='darkmagenta', marker='o')

ax.set_xlabel('Año')
ax.set_ylabel('Precio del Cromo (Dólares)')
ax.set_zlabel('Unidades Vendidas')
ax.set_title('Venta en función del año y el  precio unitario \n Del 2019 al 2024', 
             fontsize=16, color='cadetblue', fontweight='bold', ha='center')
plt.show()