# Posiblemente se cambie por el archivo de funciones 

# funcion validacion le das un numero y un rango


import requests

# Como usar la API
response = requests.get('https://github.com/Algoritmos-y-Programacion-2223-3/api-proyecto/blob/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
data = response.json()
