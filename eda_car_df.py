import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
car_df = pd.read_csv('ruta/a/tu/archivo.csv')

# Mostrar las primeras filas del DataFrame
print(car_df.head())

# Información general del DataFrame
print(car_df.info())

# Resumen estadístico
print(car_df.describe())

# Histograma de todas las variables numéricas
car_df.hist(bins=30, figsize=(15, 10))
plt.show()

# Mapa de calor de la correlación entre variables
plt.figure(figsize=(12, 8))
sns.heatmap(car_df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Basado en la correlación, seleccionamos la mejor variable
best_variable = 'engine_size'  # Ejemplo
print(f"La mejor variable para predecir el precio del coche es: {best_variable}")

correlation_matrix = car_df.corr()

# Selección de la mejor variable basada en la correlación con el precio
print(correlation_matrix['price'].sort_values(ascending=False))

# Gráficos de dispersión para algunas variables
sns.pairplot(car_df)
plt.show()
