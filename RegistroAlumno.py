# -*- coding: cp1252 -*-
from record import record
import os

materias=['Administracion','Diseño','Dinamica','Estructura',\
          'Ingles','Metodos','Practicas','Redes']
grupo=[0 for i in range(40)]


#REGISTROS/CLASES
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
    
#IMPRESION
def impresion(alumno):
    print 'ID: '+ str(alumno.a_id)
    print 'Nombre: '+alumno.a_nom
    print 'Apellido Paterno: '+alumno.a_ap
    print 'Apellido Materno: '+alumno.a_am
    print 'Fecha de Nacimiento: '+alumno.fecha.dia+'/'\
          +alumno.fecha.mes+'/'+alumno.fecha.anio
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

#FUNCIONES
def FINDid(ID, k, *grupo):
    encontrados=0
    for i in range(k):
        if ID==grupo[i].a_id:
            ubicacion=i
            encontrados=encontrados+1
            print 'Encontrado!'
            impresion(grupo[ubicacion])
    if encontrados<=0:
        print 'No existen coincidencias'
    return

def FINDname(nombre, k, *grupo):
    encontrados=0
    for i in range(k):        
        if nombre==grupo[i].a_nom:
            ubicacion=i
            print 'Encontrado!'
            encontrados=encontrados+1
            impresion(grupo[ubicacion])
    if encontrados<=0:
        print 'No existen coincidencias'
    return

def FINDage(age, k, *grupo):
    encontrados=0
    for i in range(k):        
        edad=grupo[i].fecha.dia+'/'+grupo[i].fecha.mes+'/'+grupo[i].fecha.anio
        if age == edad:
            ubicacion=i
            encontrados=encontrados+1
            print 'Encontrado!'
            impresion(grupo[ubicacion])
    if encontrados <=0:
        print 'No existen coincidencias'           
    return
       
k=int(raw_input("Ingrese el tamaño del grupo: "))

#LLENADO
for l in range(k):
    print '\n'
    grupo[l]=alumno(a_id=int(raw_input('Ingrese id: ')),\
                    a_nom=raw_input('Ingrese nombre: '),\
                    a_ap=raw_input('Ingrese apeliido paterno: '),\
                    a_am=raw_input('Ingrese apeliido materno: '),\
                    fecha=nacimiento(dia=raw_input('Ingrese dia de nacimiento: '),\
                                     mes=raw_input('Ingrese mes de nacimiento: '),\
                                     anio=raw_input('Ingrese año de nacimiento 4 digitos: ')))
    
    grupo[l].a_nom=grupo[l].a_nom.capitalize()
    grupo[l].a_ap=grupo[l].a_ap.capitalize()
    grupo[l].a_am=grupo[l].a_am.capitalize()
    
    LEN=len(grupo[l].fecha.dia)
    if LEN<2:
        grupo[l].fecha.dia='0'+grupo[l].fecha.dia

    LEN=len(grupo[l].fecha.mes)
    if LEN<2:
        grupo[l].fecha.mes='0'+grupo[l].fecha.mes
    
    for i in range(8):
        for j in range(4):
            grupo[l].calificaciones[i][j]=int(raw_input('Ingrese calificacion '+str(j+1)+\
                                                        ' de la materia '+materias[i]+': '))
    print '\n'
    impresion(grupo[l])
     
#BUSQUEDA
programa='s'
while(programa=='s'):
    print '\n'
    print 'BUSQUEDA\n1.- ID\n2.- Nombre\n3.- Fecha\n'
    valor=int(raw_input('Seleccione su metodo de busqueda: '))
    if valor==1:
        print '\nBUSQUEDA POR ID'
        ID=int(raw_input('Ingrese ID: '))
        print '\n'
        FINDid(ID, k, *grupo)
        
    elif valor==2:
        print '\nBUSQUEDA POR NOMBRE'
        nombre=raw_input('Ingrese Nombre: ')
        nombre=nombre.capitalize()
        print '\n'
        FINDname(nombre, k, *grupo)
        
    elif valor==3:
        print '\nBUSQUEDA POR NACIMIENTO'
        day=raw_input('Ingrese Dia: ')
        month=raw_input('Ingrese Mes: ')
        year=raw_input('Ingrese Año 4 digitos: ')
        LEN=len(day)
        if LEN<2:
            day='0'+day

        LEN=len(month)
        if LEN<2:
            month='0'+month

        age=day+'/'+month+'/'+year
        print '\n'
        FINDage(age, k, *grupo)
        
    print '\n'
    programa=raw_input('¿Desea seguir buscando? (s/n)')
