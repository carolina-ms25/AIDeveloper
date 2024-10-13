import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Especificar manualmente la ruta del archivo CSV 
file_path = 'data/Dataset_La_Molina_cleaned.csv'

# 2. Cargar el archivo CSV
data = pd.read_csv(file_path)

# 3. Seleccionar las características (features) y la variable objetivo (target)
X = data[['Antiguedad', 'Nro_pisos', 'Dormitorios', 'Area_constr_m2', 'Area_total_m2']]
y = data['Precio']

# 4. Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# 5. Función para predecir el precio de una casa con nuevos datos
def predecir_precio_casa(antiguedad, nro_pisos, dormitorios, area_constr_m2, area_total_m2):
    entrada = np.array([[antiguedad, nro_pisos, dormitorios, area_constr_m2, area_total_m2]])
    prediccion = model.predict(entrada)
    return prediccion[0]
