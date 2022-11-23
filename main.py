from misFunciones import getUserInfo
from tkinter import *
from datetime import date
from datetime import datetime
import json


def botEntrada():
    idUsuario=V_C_entry.get()#obtener el valor asociado a la variable de control asignada al Entry
    print(idUsuario, "HAROLD", date.today())
    V_C_label.set(idUsuario)#establecer el
    print("El boton ha sido oprimido")

   
def botID(): 
    idUsuario = V_C_entry.get()
    V_C_label.set(getUserInfo(idUsuario))
    print(getUserInfo(idUsuario))

raiz=Tk()
raiz.title("Asistencia")

marco=Frame(raiz)
marco.pack()
marco.configure(height='600',width='600')
marco.grid_propagate(False)

V_C_label=StringVar()
mostrar=Label(marco,textvariable=V_C_label).place(x=30,y=30)#label
V_C_entry=StringVar()
entrada=Entry(marco,textvariable=V_C_entry).place(x=30,y=150)
botEntrada=Button(marco,text="REGISTRAR ENTRADA",command=botEntrada).place(x=30,y=60)#boton
botID=Button(marco,text="OBTENER DATOS DEL JSON segun id",command=botID).place(x=30,y=90)#boton

print('uno')
raiz.mainloop()