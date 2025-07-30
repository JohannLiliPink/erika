import pandas as pd
import matplotlib.pyplot as plt
import os
from fredapi import Fred
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

API_KEY = '72d303b09805418524099e4673432602'

def obtener_datos():
    fred = Fred(api_key=API_KEY)
    fechas = ('2000-01-01', '2023-12-31')
    series = {
        'house_price_index': 'CSUSHPINSA',
        'inflacion': 'CPIAUCSL',
        'desempleo': 'UNRATE',
        'interes': 'FEDFUNDS',
        'ingreso': 'MEPAINUSA672N'
    }

    df = pd.DataFrame()
    for nombre, codigo in series.items():
        df[nombre] = fred.get_series(codigo, *fechas)

    df.index = fred.get_series(series['house_price_index'], *fechas).index
    df = df.dropna()

    return df

def entrenar_modelo():
    df = obtener_datos()
    X = df[['inflacion', 'desempleo', 'interes', 'ingreso']]
    y = df['house_price_index']

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    # Graficar predicción vs real
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.index, y_test, label='Real')
    plt.plot(y_test.index, y_pred, label='Predicción', linestyle='--')
    plt.xlabel('Fecha')
    plt.ylabel('Índice de Precios Vivienda')
    plt.title('Real vs Predicción del Precio de la Vivienda')
    plt.legend()
    plt.tight_layout()

    # Guardar gráfico en static
    path_static = os.path.join('prediccion_vivienda', 'static', 'prediccion_vivienda')
    os.makedirs(path_static, exist_ok=True)
    grafico_path = os.path.join(path_static, 'grafico.png')
    plt.savefig(grafico_path)
    plt.close()

    resultado = {
        'r2_score': r2_score(y_test, y_pred),
        'mse': mean_squared_error(y_test, y_pred),
        'coeficientes': dict(zip(X.columns, modelo.coef_)),
        'intercepto': modelo.intercept_,
        'grafico_url': 'prediccion_vivienda/grafico.png',
    }

    return resultado





# import pandas as pd
# from fredapi import Fred
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score, mean_squared_error

# API_KEY = 'TU_API_KEY'  # ← reemplaza con tu clave real

# def obtener_datos():
#   fred = Fred(api_key=API_KEY)

#   fechas = ('2000-01-01', '2023-12-31')

#   series = {
#     'house_price_index': 'CSUSHPINSA',  # Índice nacional precios vivienda
#     'inflacion': 'CPIAUCSL',
#     'desempleo': 'UNRATE',
#     'interes': 'FEDFUNDS',
#     'ingreso': 'MEPAINUSA672N'
#   }

#   df = pd.DataFrame()
#   for nombre, codigo in series.items():
#     df[nombre] = fred.get_series(codigo, *fechas)

#   df.index = fred.get_series(series['house_price_index'], *fechas).index
#   df = df.dropna()

#   return df

# def entrenar_modelo():
#   df = obtener_datos()

#   X = df[['inflacion', 'desempleo', 'interes', 'ingreso']]
#   y = df['house_price_index']

#   X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

#   modelo = LinearRegression()
#   modelo.fit(X_train, y_train)

#   y_pred = modelo.predict(X_test)

#   resultado = {
#     'r2_score': r2_score(y_test, y_pred),
#     'mse': mean_squared_error(y_test, y_pred),
#     'coeficientes': dict(zip(X.columns, modelo.coef_)),
#     'intercepto': modelo.intercept_
#   }

#   return resultado
