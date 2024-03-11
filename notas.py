def asignarNotas(campus:dict,students:dict,rutas:dict):
    num=0
    idx=0
    print('Estos son los programas en curso')
    for key,value in campus.items():
        if value['fechaInicio'] != 'En proceso':
            print(f'{key}.Programa {key} de ', value['ruta'],' con horario ',value['horario'])
    op=int(input('Elige una opcion: '))

    for i in range(len(rutas['java'])):
        if campus[op]['ruta']=='java':
            print(f'{idx+1}.Ruta Java ciclo ', rutas['java'][idx+1] )
            idx+=1
        elif campus[op]['ruta']=='javaScript':
            print(f'{idx+1}.Ruta javaScript ciclo ', rutas['javaScript'][idx+1] )
            idx+=1
        elif campus[op]['ruta']=='c#':
            print(f'{idx+1}.Ruta C# ciclo ', rutas['c#'][idx+1] )
            idx+=1
    op2=int(input('Selecciona un ciclo: '))
    

    print('1.Quices\n2.Trabajos\n3.Examenes')
    typenote=['quices','trabajos','examenes']
    op3=int(input('Selecciona el valor: '))
    for i in range(len(campus)):
        if op==i+1:
            notas(campus[op],students,op2,typenote[op3-1])
    input()



def notas(campus:dict,students:dict,op2:int,op3:str):
        for key,value in campus['students'].items():
            for key2,value2 in students.items():
                if value==value2['id']:
                    print(f'Ingrese la nota de ', {value2['name']})
                    num=float(input())
                    value2['notas'][op2][op3].append(num)

def eliminarNotas(students:dict, rutas:dict):
    id=int(input('ingrese el id del estudiante a eliminar: '))
    for i in range(len(rutas['java'])):
        print(f'{i+1}.Ciclo {i+1}')
    op2=int(input('Selecciona un ciclo: '))
    print('1.Quices\n2.Trabajos\n3.Examenes')
    typenote=['quices','trabajos','examenes']
    op3=int(input('Selecciona el valor: '))
    idx=1
    for Key,value in students.items():
        if id== value['id']:
            for value2 in value['notas'][op2][typenote[op3-1]]:
                print(idx,'.',value2)
                idx+=1
   
    op4=int(input('Selecciona el valor: '))
    for Key,value in students.items():
        if id== value['id']:
            value['notas'][op2][typenote[op3-1]].pop(op4-1)
            input()
            break
            

def verNotas(students:dict):
    id=int(input('ingrese el id del estudiante a ver: '))
    for i in range(5):
        print(f'{i+1}.Ciclo {i+1}')
    op2=int(input('Selecciona un ciclo: '))
    print('1.Quices\n2.Trabajos\n3.Examenes')
    typenote=['quices','trabajos','examenes']
    op3=int(input('Selecciona el valor: '))
    idx=1
    for Key,value in students.items():
        if id== value['id']:
            for value2 in value['notas'][op2][typenote[op3-1]]:
                print(idx,'.',value2)
                idx+=1

def obtenerDefinitiva(student:dict,campus:dict):
    
    definitive=0
    print('Estos son los programas en curso')
    for key,value in campus.items():
        if value['fechaInicio'] != 'En proceso':
            print(f'{key}.Programa {key} de ', value['ruta'],' con horario ',value['horario'])
    op=int(input('Elige una opcion: '))
    for i in range(5):
        print(f'{i+1}.Ciclo {i+1}')
    op2=int(input('Selecciona el ciclo'))
    try:
        for key,value in campus[op].items():
            for key2,value2 in value.items():
                for key3,value3 in student.items():
                    if value2==value3['id']:
                        promedios=[]
                        for key4,value4 in value3['notas'][op2].items():
                            if len(value4)!=0:
                                promedios.append(promedio(value4))
                            else:
                                promedios.append(0)
                        definitive=definitiva(promedios)
                        value3['notas'][op2].update({'definitiva':definitive})
    except AttributeError:
        pass
    



        # if len(value2['examenes'])==0:

        #     print('debe ingresar la nota de examen de',value['id'])  
        #     input()
        # elif len(value2['quices'])==0:
        #     promedioexamen=promedio(value2['examenes'])
        #     promediotrabajo=promedio(value2['trabajos'])
        #     definitiva=promedioexamen*0.8 + promediotrabajo*0.2
        #     value2.update({'notaDefinitiva':definitiva})
        # elif len(value2['trabajos'])==0:
        #     promedioexamen=promedio(value2['examenes'])
        #     promedioquiz=promedio(value2['quices'])
        #     definitiva=promedioexamen*0.7 + promedioquiz*0.3
        #     value2.update({'notaDefinitiva':definitiva})
        # else:
        #     promedioexamen=promedio(value2['examenes'])
        #     promedioquiz=promedio(value2['quices'])
        #     promediotrabajo=promedio(value2['trabajos'])
        #     definitiva=promedioexamen*0.7 + promediotrabajo*0.1+ promedioquiz*0.2
        #     value2.update({'notaDefinitiva':definitiva})

def promedio(notas:list):
    suma=0
    promedio=0
    for i in notas:
        suma+=i
    promedio= suma/(len(notas))
    return promedio

def definitiva(promedios:list):
    definitiva=0
    if promedios[2]==0:
        print('debe añadir notas de examen')
    elif promedios[1]==0:
        definitiva=promedios[0]*0.3 + pormeds[2]*0.7
    elif promedios[0]==0:
        definitiva=promedios[1]*0.2 + pormeds[2]*0.8
    else:
        definitiva=promedios[0]*0.2 + promedios[2]*0.7 + promedios[1]*0.1
    return definitiva

def validarEstado(student:dict):
    
    for key,value in student.items():
        for key2,value2 in value['notas'].items():
            contador=0
            if 'definitiva' in value2:
                
                if value2['definitiva']<60:
                    contador+=1
                    print(contador)
                    print('_______________________________________')
            
                if contador==1:
                    value['estado']='En riesgo'
                elif contador==2:
                    value['estado']='Por fuera'
                elif contador==0:
                    value['estado']='Normal'
