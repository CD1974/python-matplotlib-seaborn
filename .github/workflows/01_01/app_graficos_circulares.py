import matplotlib.pyplot as plt
import pandas as pd

df_gastos = pd.DataFrame({
        "categorías": ["Comida", "Vivienda", "Transporte", "Ropa", "Ahorro", "Otros"],
        "gastos": [170, 280, 120, 100, 110, 220],
    })

fig, ax = plt.subplots()
ax.pie(
    x=df_gastos['gastos'],
    labels=df_gastos['categorías'],
    autopct="%1.1f%%",
    startangle=90,)

ax.set_title("Gastos mensuales", fontsize=16, color='blue', fontweight='bold')
plt.show()