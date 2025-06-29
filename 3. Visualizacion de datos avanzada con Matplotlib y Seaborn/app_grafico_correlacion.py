import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import os

# Ruta absoluta al archivo empleados.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'empleados.csv')

df_empleados = pd.read_csv(csv_path, delimiter=",")


df_correlacion = df_empleados[["Edad", "Experiencia", "Salario"]].corr()
f, ax = plt.subplots()

mask = np.triu(np.ones_like(df_correlacion, dtype=bool))

sns.heatmap(df_correlacion, 
            mask=mask, 
            annot=True, 
            center=0, 
            fmt=".2f",
            linewidths=.5, 
            cbar_kws={"shrink": .5}
        )

ax.set_title('Correlación entre edad, salario y experiencia', color='olivedrab', ha='center', fontweight='bold', pad=20)
plt.show()