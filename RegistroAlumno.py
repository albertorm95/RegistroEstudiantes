# -*- coding: cp1252 -*-
from record import record
import os

materias=['Dinamica','Estructura','Administracion','Ingles',\
          'Diseño','Redes','Metodos','Practicas']

grupo=[0 for i in range(40)]

class nacimiento(record):
    dia=1
    mes=1
    anio=1
    
class alumno(record):
    a_id=0
    a_nom=''
    a_ap=''
    a_am=''
    fecha=None
    calificaciones=[[0 for i in range(5)] for i in range(8)]

def impresion(alumno):
    print 'ID: '+ str(alumno.a_id)
    print 'Nombre: '+alumno.a_nom
    print 'Apellido Paterno: '+alumno.a_ap
    print 'Apellido Materno: '+alumno.a_am
    print 'Fecha de Nacimiento: '+str(alumno.fecha.dia)+'/'\
          +str(alumno.fecha.mes)+'/'+str(alumno.fecha.anio)
    for i in range(8):
        acumulador=0
        promedio=0
        for j in range(4):
            acumulador=alumno.calificaciones[i][j]+acumulador
            promedio=acumulador/4
            alumno.calificaciones[i][4]=promedio
    for i in range(8):
        print 'Promedio de '+materias[i]+': '+str(alumno.calificaciones[i][4])
    return

n=int(raw_input("Ingrese el tamaño del grupo: "))

for h in range(n):
    grupo[h]=alumno(a_id=int(raw_input('Ingrese id: ')),\
                    a_nom=raw_input('Ingrese nombre: '),\
                    a_ap=raw_input('Ingrese apeliido paterno: '),\
                    a_am=raw_input('Ingrese apeliido materno: '),\
                    fecha=nacimiento(dia=int(raw_input('Ingrese dia de nacimiento: ')),\
                                    mes=int(raw_input('Ingrese mes de nacimiento: ')),\
                                    anio=int(raw_input('Ingrese año de nacimiento: ')))
                    )
    
    for i in range(8):
        for j in range(4):
            grupo[h].calificaciones[i][j]=int(raw_input('Ingrese calificacion '+str(j+1)+\
                                                  ' de la materia '+materias[i]+': '))

'''primo=alumno(a_id=int(raw_input('Ingrese id: ')),\
             a_nom=raw_input('Ingrese nombre: '),\
             a_ap=raw_input('Ingrese apeliido paterno: '),\
             a_am=raw_input('Ingrese apeliido materno: '),\
             fecha=nacimiento(dia=int(raw_input('Ingrese dia de nacimiento: ')),\
                              mes=int(raw_input('Ingrese mes de nacimiento: ')),\
                              anio=int(raw_input('Ingrese año de nacimiento: ')))'''
            


os.system('cls')
for k in range(n):
    impresion(grupo[k])

