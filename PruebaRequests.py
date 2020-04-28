import requests
import pandas as pd

url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

response = requests.get(url)

print(response.json())

tablaprecios = pd.DataFrame(response.json()['ListaEESSPrecio']).head()

print ( "Muestro de la lista del diccionario")
print(tablaprecios)