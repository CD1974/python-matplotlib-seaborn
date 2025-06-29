import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# Ruta absoluta al archivo empleados.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'empleados.csv')

df_empleados = pd.read_csv(csv_path, delimiter=",")


sns.set_theme(style="whitegrid")
sns.pairplot(df_empleados, 
             plot_kws={'color': '#ff7f0e'},
             diag_kws={'color': '#bcbd22'})
plt.show()