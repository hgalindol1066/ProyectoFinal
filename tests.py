from datetime import date
from datetime import datetime
import json
def cargar_datos():
    with open(".\\regAsistencia.json") as file:
        return json.load(file)

def getUserInfo(id):
    print(regAsistencia[id])

    
regAsistencia = cargar_datos()

print(regAsistencia)
getUserInfo("01")
