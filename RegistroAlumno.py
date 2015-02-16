# -*- coding: cp1252 -*-
from record import record
import os

materias=['Administracion','Diseño','Dinamica','Estructura',\
          'Ingles','Metodos','Practicas','Redes']

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
    print 'Fecha de Nacimiento: '+alumno.fecha.dia+'/'\
          +alumno.fecha.mes+'/'+alumno.fecha.anio
    #for i in range(8):
    #    acumulador=0
    #    promedio=0
    #    for j in range(4):
    #        acumulador=alumno.calificaciones[i][j]+acumulador
    #        promedio=acumulador/4
    #        alumno.calificaciones[i][4]=promedio
    #for i in range(8):
    #    print 'Promedio de '+materias[i]+': '+str(alumno.calificaciones[i][4])
    return

def busquedaid(id0, n, *grupo):
    encontrados=0
    for i in range(n):
        if id0==grupo[i].a_id:
            ubicacion=i
            encontrados=encontrados+1
    if encontrados <= 0:
        print 'No existen coincidencias'
    else:
        print 'Encontrado!'
        impresion(grupo[ubicacion])
    return

def busquedanombre(nombre, n, *grupo):
    encontrados=0
    for i in range(n):        
        if nombre==grupo[i].a_nom:
            ubicacion=i
            print 'Encontrado!'
            encontrados=encontrados+1
            impresion(grupo[ubicacion])
    if encontrados<=0:
        print 'No existen coincidencias'
    return

def busquedaedad(age, n, *grupo):
    for i in range(n):
        encontrados=0
        edad=grupo[i].fecha.dia+'/'+grupo[i].fecha.mes+'/'+grupo[i].fecha.anio
        if age == edad:
            ubicacion=i
            encontrados=encontrados+1
        if encontrados <=0:
            print 'No existen coincidencias'
        if encontrados > 0:
            print 'Encontrado!'
            impresion(grupo[ubicacion])
    return
       
n=int(raw_input("Ingrese el tamaño del grupo: "))

for h in range(n):
    grupo[h]=alumno(a_id=int(raw_input('Ingrese id: ')),\
                    a_nom=raw_input('Ingrese nombre: '),\
                    a_ap=raw_input('Ingrese apeliido paterno: '),\
                    a_am=raw_input('Ingrese apeliido materno: '),\
                    fecha=nacimiento(dia=raw_input('Ingrese dia de nacimiento: '),\
                                     mes=raw_input('Ingrese mes de nacimiento: '),\
                                     anio=raw_input('Ingrese año de nacimiento 4 digitos: '))
                    )
    
    grupo[h].a_nom=grupo[h].a_nom.capitalize()
    grupo[h].a_ap=grupo[h].a_ap.capitalize()
    grupo[h].a_am=grupo[h].a_am.capitalize()
    
    dialen=len(grupo[h].fecha.dia)
    if dialen<2:
        grupo[h].fecha.dia='0'+grupo[h].fecha.dia

    meslen=len(grupo[h].fecha.mes)
    if meslen<2:
        grupo[h].fecha.mes='0'+grupo[h].fecha.mes
    
    '''for i in range(8):
        for j in range(4):
            grupo[h].calificaciones[i][j]=int(raw_input('Ingrese calificacion '+str(j+1)+\
                                                        ' de la materia '+materias[i]+': '))'''
    impresion(grupo[h])
    print '\n' 

   

programa='s'
while(programa=='s'):
    print 'BUSQUEDA\n1.- ID\n2.- Nombre\n3.- Fecha\n'
    valor=int(raw_input('Seleccione su metodo de busqueda: '))
    if valor==1:
        print 'BUSQUEDA POR ID'
        id0=int(raw_input('Ingrese ID: '))
        busquedaid(id0, n, *grupo)
        print '\n'
        
    elif valor==2:
        print 'BUSQUEDA POR NOMBRE'
        nombre=raw_input('Ingrese Nombre: ')
        nombre=nombre.capitalize()
        busquedanombre(nombre, n, *grupo)
        print '\n'
        
    elif valor==3:
        print 'BUSQUEDA POR NACIMIENTO'
        day=raw_input('Ingrese Dia: ')
        month=raw_input('Ingrese Mes: ')
        year=raw_input('Ingrese Año 4 digitos: ')
        daylen=len(day)
        if daylen<2:
            day='0'+day

        monthlen=len(month)
        if monthlen<2:
            month='0'+month

        age=day+'/'+month+'/'+year
        busquedaedad(age, n, *grupo)
        print '\n'

        

    programa=raw_input('¿Desea seguir buscando? (s/n)')

