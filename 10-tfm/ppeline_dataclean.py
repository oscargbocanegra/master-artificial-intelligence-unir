# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 1: Cargar el dataset
def cargar_datos(ruta):
    """Carga un archivo CSV en un DataFrame de pandas."""
    return pd.read_csv(ruta)

# Paso 2: Estadísticas descriptivas
def estadisticas_descriptivas(df):
    """Genera un resumen estadístico del DataFrame."""
    print("Estadísticas descriptivas:\n", df.describe())

# Paso 3: Detección y manejo de valores nulos
def manejar_valores_nulos(df):
    """Detecta y maneja valores nulos en el DataFrame."""
    print("Valores nulos por columna:\n", df.isnull().sum())
    df.fillna(df.mean(), inplace=True)  # Sustituir valores nulos por la media

# Paso 4: Detección de outliers mediante z-score e IQR
def detectar_outliers(df, columna):
    """Identifica outliers en una columna utilizando z-score e IQR."""
    # Z-score
    df['z_score'] = (df[columna] - df[columna].mean()) / df[columna].std()
    outliers_z = df[np.abs(df['z_score']) > 3]
    print(f"Outliers detectados por z-score en {columna}:\n", outliers_z)

    # IQR
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers_iqr = df[(df[columna] < Q1 - 1.5 * IQR) | (df[columna] > Q3 + 1.5 * IQR)]
    print(f"Outliers detectados por IQR en {columna}:\n", outliers_iqr)

# Paso 5: Visualizaciones
def generar_visualizaciones(df, columna):
    """Genera histogramas y diagramas de caja para una columna."""
    plt.figure(figsize=(12, 6))
    
    # Histograma
    plt.subplot(1, 2, 1)
    sns.histplot(df[columna], kde=True, bins=30, color='blue')
    plt.title(f"Histograma de {columna}")

    # Diagrama de caja
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[columna], color='green')
    plt.title(f"Diagrama de caja de {columna}")

    plt.tight_layout()
    plt.show()

# Paso 6: Conversión a formatos estándar
def conversion_formatos(df, columnas):
    """Convierte columnas especificadas a formatos estándar (por ejemplo, texto en minúsculas)."""
    for columna in columnas:
        df[columna] = df[columna].str.lower()

# Pipeline principal
def pipeline(ruta_datos):
    """Pipeline principal que integra todos los pasos del EDA."""
    df = cargar_datos(ruta_datos)
    estadisticas_descriptivas(df)
    manejar_valores_nulos(df)
    detectar_outliers(df, df.columns[0])  # Sustituir por el nombre de la columna relevante
    generar_visualizaciones(df, df.columns[0])  # Sustituir por el nombre de la columna relevante
    conversion_formatos(df, ['columna_texto'])  # Sustituir por el nombre de la columna textual relevante

    return df

# Ejecución del pipeline
ruta_datos = "D:/datasets/synthetic_dataset.csv"  # Sustituir por la ruta real
# resultado_df = pipeline(ruta_datos)