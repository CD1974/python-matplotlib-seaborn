import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_edad =  pd.DataFrame({
    'grupo_1': np.random.normal(18, 45, 1000),
    'grupo_2': np.random.normal(18, 45, 1000)
})

fig, ax = plt.subplots()
bins = np.arange(18, 45, 2)

ax.hist(
        [df_edad['grupo_1'],df_edad['grupo_2']],
        label=['Grupo 1','Grupo 2'],
        histtype='stepfilled',
        bins=bins,
        alpha=0.3,
        ec="k"
)
ax.legend(loc='upper right')
ax.set_xlabel('Edad')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de edades de grupos de estudio', fontsize=16, color='olivedrab', fontweight='bold', pad=20)
plt.show()