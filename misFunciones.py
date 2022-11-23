from datetime import date
from datetime import datetime
import json


ruta = ".\\regAsistencia.json"
#Función que permite obtener los datos del archivo json.
def leer_datos():
    with open(ruta) as file:
        return json.load(file)
    
#Función que permite obtener los datos del usuario según su id.
def getUserInfo(id):
    regAsistencia=leer_datos()
    return regAsistencia[id]

#Función que permite escribir datos en el archivo json.
def escribir_datos(id):
    archivo = leer_datos() 
    datos = getUserInfo(id)
    fecha = "{}-{}-{}".format(date.today().day, date.today().month, date.today().year)
    if (not(fecha in datos["asistencias"])):
        datos["asistencias"].append(fecha)
    archivo[id] = datos
    with open(ruta, "w") as file:
        json.dump(archivo, file, indent=4)



# datos = getUserInfo("01")
# print(datos)
