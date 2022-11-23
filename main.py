from funciones_json import getUserInfo, escribir_datos
from tkinter import *
from datetime import date
from datetime import datetime
import json

 
def botAsistencias():
    idUsuario = V_C_entry.get()
    #Se toma la lista de asistencias del usuario deseado y se halla su longitud.
    cantAsistencias = len(getUserInfo(idUsuario)["asistencias"])
    mensaje = "El usuario " +(getUserInfo(idUsuario))["nombre"]+" ha asistido "+str(cantAsistencias)+ " veces"
    V_C_label.set(mensaje)

def botRegEntrada():
    idUsuario = V_C_entry.get()
    escribir_datos(idUsuario)

def botMaxAsistencias():
    id = "0"
    #variable de control
    maxAsistencias = 0
    userMaxAsistencias = ""
    #El ciclo encuentra el usuario con mayor cantidad de asistencias
    #recorriendo cada usuario y asignando la longitud de la lista de
    #sus asistencias a la variable de control si esta es mayor a la
    #variable de control.
    for i in range(4):
        if(len(getUserInfo(id+str(i+1))["asistencias"])>maxAsistencias):
            maxAsistencias = len(getUserInfo(id+str(i+1))["asistencias"])
            userMaxAsistencias = getUserInfo(id+str(i+1))["nombre"]
    V_C_label.set(userMaxAsistencias)

#Función que halla la mayor cantidad de asistencias.
def maxAsistencias():
    id = "0"
    maxAsistencias = 0
    for i in range(4):
        if(len(getUserInfo(id+str(i+1))["asistencias"])>maxAsistencias):
            maxAsistencias = len(getUserInfo(id+str(i+1))["asistencias"])
    return maxAsistencias 

def botMinAsistencias():
    id = "0"
    #variable de control
    minAsistencias = maxAsistencias()
    userMinAsistencias = ""
    #El ciclo encuentra el usuario con menor cantidad de asistencias
    #recorriendo cada usuario y asignando la longitud de la lista de
    #sus asistencias a la variable de control si esta es menor a la
    #variable de control.
    for i in range(4):
        if(len(getUserInfo(id+str(i+1))["asistencias"])<minAsistencias):
            minAsistencias = len(getUserInfo(id+str(i+1))["asistencias"])
            userMinAsistencias = getUserInfo(id+str(i+1))["nombre"]
    V_C_label.set(userMinAsistencias)



raiz=Tk()
raiz.title("Asistencia")

marco=Frame(raiz)
marco.pack()
marco.configure(height='300',width='300')
marco.grid_propagate(False)

V_C_label=StringVar()
mostrar=Label(marco,textvariable=V_C_label).place(x=30,y=30)#label
V_C_entry=StringVar()
entrada=Entry(marco,textvariable=V_C_entry).place(x=30,y=180)

botRegEntrada=Button(marco,text="REGISTRAR ASISTENCIA",command=botRegEntrada).place(x=30,y=60)#boton

botAsistencias=Button(marco,text="OBTENER CANTIDAD DE ASISTENCIAS",command=botAsistencias).place(x=30,y=90)#boton

botMaxAsistencias=Button(marco,text="USUARIO CON MAXIMAS ASISTENCIAS",command=botMaxAsistencias).place(x=30,y=120)#boton

botMinAsistencias=Button(marco,text="USUARIO CON MINIMAS ASISTENCIAS",command=botMinAsistencias).place(x=30,y=150)#boton

raiz.mainloop()