import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ruta absoluta al archivo empleados.csv, esté donde esté el script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'empleados.csv')

df_empleados = pd.read_csv(csv_path, delimiter=",")


sns.set_theme(style="whitegrid")
g =  sns.jointplot(x="Experiencia", y="Salario", data=df_empleados, kind="reg", height=7)

g.set_axis_labels("Experiencia (años)", "Salario (Dólares)", fontsize=12)
plt.subplots_adjust(top=0.9) 
plt.suptitle("Relación entre Experiencia y Salario", fontsize=16, color='green', fontweight='bold', ha='center')
plt.tight_layout() 
plt.show()