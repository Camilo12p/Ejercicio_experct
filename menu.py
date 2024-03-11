import os 
import student as e
import cupos as c
import notas as n

def Principal():
    titulo='''
                ++++++++++++++++++++++++++++++++
                +     Sistema Campuslands      +
                ++++++++++++++++++++++++++++++++
    
    '''
    os.system('cls')

    print(titulo)


def AddStudent(source:dict):
    titulo='''
                ++++++++++++++++++++++++++++++++
                +     modificar estudiantes    +
                ++++++++++++++++++++++++++++++++

                1. Añadir estudiantes
                2. Asignar Prueba inicial
                3. Borrar estudiantes
                4. Salir
    '''
    validar=True 
    while validar:
        print(titulo)
        op=int(input('Selecciona una opcion: '))
        if op==1:
            e.AddStudent(source)
            input()
            pass
        elif op==2:
            e.pruebaInicial(source) 
            input()
        elif op==3:
            e.deleteStudent(source)
            input()
            pass
        elif op==4:
                validar=False
                pass
        else: 
             print('Seleccione un valor valido')


def asignarCupos(campus:dict,students:dict,rutas:dict,trainers:dict,horarios:dict):
    titulo='''
                ++++++++++++++++++++++++++++++++
                +        Asignar cupos         +
                ++++++++++++++++++++++++++++++++

                1. Asignar cupos
                2. Mover estudiantes
                3. Ver cupos
                4. Salir
    '''
    validar=True 
    while validar:
        print(titulo)
        op=int(input('Selecciona una opcion: '))
        if op==1:
            c.asignar(campus,students,trainers,horarios)
            print(campus)
            print(trainers)
            input()
            pass
        elif op==2:
            c.movercupos(campus,students)
        elif op==3:
            c.verCupos(campus,students)
            input()
            pass
        elif op==4:
                validar=False
                pass
        else: 
             print('Seleccione un valor valido')
 
def asignarNotas(campus:dict,student:dict,rutas:dict,horarios:dict):
    titulo='''
                ++++++++++++++++++++++++++++++++
                +        Asignar Notas         +
                ++++++++++++++++++++++++++++++++

                1. Asignar nota
                2. eliminar nota
                3. Obtener definitiva
                4. Ver notas
                5. Salir
    '''
    validar=True 
    while validar:
        print(titulo)
        op=int(input('Selecciona una opcion: '))
        if op==1:
            n.asignarNotas(campus,student,rutas)
            input()
            pass
        elif op==2:
            n.eliminarNotas(student,rutas)
            print(student)
        elif op==3:
            n.obtenerDefinitiva(student,campus)
            print(student)
            input()
            pass
        elif op==4:
            n.verNotas(student)
            input()
            pass
        elif op==5:
                validar=False
                pass
        else: 
             print('Seleccione un valor valido')