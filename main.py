from misFunciones import getUserInfo, escribir_datos
from tkinter import *
from datetime import date
from datetime import datetime
import json


def botID(): 
    idUsuario = V_C_entry.get()
    V_C_label.set(getUserInfo(idUsuario))
    print(getUserInfo(idUsuario))

def botAsistencias():
    idUsuario = V_C_entry.get()
    cantAsistencias = "El usuario " +(getUserInfo(idUsuario))["nombre"]+" ha asistido "+str(len(getUserInfo(idUsuario)["asistencias"]))+ " veces"
    V_C_label.set(cantAsistencias)

def botRegEntrada():
    idUsuario = V_C_entry.get()
    escribir_datos(idUsuario)


raiz=Tk()
raiz.title("Asistencia")

marco=Frame(raiz)
marco.pack()
marco.configure(height='600',width='600')
marco.grid_propagate(False)

V_C_label=StringVar()
mostrar=Label(marco,textvariable=V_C_label).place(x=30,y=30)#label
V_C_entry=StringVar()
entrada=Entry(marco,textvariable=V_C_entry).place(x=30,y=120)

botAsistencias=Button(marco,text="OBTENER CANTIDAD DE ASISTENCIAS",command=botAsistencias).place(x=30,y=60)#boton

botRegEntrada=Button(marco,text="REGISTRAR ASISTENCIA",command=botRegEntrada).place(x=30,y=90)#boton

raiz.mainloop()