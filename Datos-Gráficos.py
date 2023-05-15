import pandas as pd
import plotly.express as px

# Cargar los datos desde el archivo de Excel
df = pd.read_excel('Datos_Sensores_PIR.xlsx', header=None)

# Obtener las etiquetas de los días de la semana
dias_semana = df.iloc[0, 1:5].values

# Crear gráfico de barras interactivo para el total de clientes por día
fig1 = px.bar(x=dias_semana, y=df.iloc[11, 1:5].values, labels={'x': 'Día', 'y': 'Total de clientes'})
fig1.update_traces(hovertemplate='Día: %{x}<br>Total de clientes: %{y}')
fig1.update_layout(title='Total de clientes por día')
fig1.show()

# Crear gráfico de línea interactivo para el total de clientes por intervalo de hora
intervalos = df.iloc[1:11, 0].values
total_clientes = df.iloc[1:11, 5].values

fig2 = px.line(x=intervalos, y=total_clientes, labels={'x': 'Intervalo de hora', 'y': 'Total de clientes'})
fig2.update_traces(mode='lines+markers', hovertemplate='Intervalo de hora: %{x}<br>Total de clientes: %{y}')
fig2.update_layout(title='Total de clientes por intervalo de hora')
fig2.show()
