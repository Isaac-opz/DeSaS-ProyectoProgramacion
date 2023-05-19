import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = 'Datos_Finales.xlsx'  # Reemplaza con el nombre de tu archivo Excel
datos = pd.read_excel(archivo_excel, header=1, index_col=0)

# Obtener los datos de clientes totales por día
clientes_por_dia = datos.iloc[:-1, -1].values

# Obtener los datos de clientes totales por intervalo de tiempo
intervalos = datos.columns[2:-1]  # Intervalos de tiempo desde la columna C hasta la columna L
clientes_por_intervalo = datos.iloc[:-1, 2:-1]  # Excluir la primera columna (INTERVALO) y la última columna (Total Semanal)

# Graficar clientes totales por día
dias_semana = datos.index[:-1]
plt.figure(figsize=(10, 6))
plt.plot(dias_semana, clientes_por_dia, marker='o')
plt.xlabel('Días de la semana')
plt.ylabel('Clientes totales por día')
plt.title('Clientes totales por día')
plt.xticks(rotation=45)
ax = plt.gca()
ax.set_facecolor('xkcd:light grey')
plt.grid(True)
plt.show()

# Graficar clientes totales por intervalo de tiempo
workbook = 'Datos_Finales.xlsx'

# Leer el archivo Excel
df = pd.read_excel(workbook)

# Obtener los datos de clientes totales por intervalo de tiempo
valores=df[["7:30 AM - 9:00 AM","9:00 AM - 10:30 AM","10:30 AM - 12:00 PM","12:00 PM - 1:30 PM","1:30 PM - 3:00 PM","3:00 PM - 4:30 PM","4:30 PM - 6:00 PM","6:00 PM - 7:30 PM","7:30 PM - 9:00 PM","9:00 PM - 10:30 PM"]]
#graficar clientes totales por intervalo de tiempo
plt.plot(valores.iloc[-1], marker='o')
plt.xlabel('Intervalo de tiempo')
plt.ylabel('Clientes totales por intervalo')
plt.title('Clientes totales por intervalo de tiempo')
plt.xticks(range(len(valores.iloc[-1])), valores.columns, rotation=45)
ax = plt.gca()
ax.set_facecolor('xkcd:light grey')
plt.grid(True)
plt.show()



