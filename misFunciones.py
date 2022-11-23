from datetime import date
from datetime import datetime
import json

#Función que permite obtener los datos del archivo json.
def leer_datos():
    with open(".\\regAsistencia.json") as file:
        return json.load(file)
    
#Función que permite escribir datos en el archivo json.
def escribir_datos():
    
    pass

#Función que permite obtener los datos del usuario según su id.
def getUserInfo(id):
    regAsistencia=leer_datos()
    return regAsistencia[id]

