from tabulate import tabulate

def asignar(campus:dict,students:dict,trainers:dict,horarios:dict):
    horario=''
    progrmas={
    
    }
    
    validar=True 
    while validar:
        print('1.Ruta Java\n2.Ruta C#\n3.Ruta JavaScript')
        op=int(input('Ingrese un valor: '))
        if op==1:
            progrmas=asignacion(students,trainers,'java')
            validar=False
            input()
            pass
        elif op==2:
            progrmas=asignacion(students,trainers,'c#') 
            validar=False
        elif op==3:
            progrmas=asignacion(students,trainers,'javaScript')
            validar=False
            input()
            pass
        else: 
             print('Seleccione un valor valido')
    if len(progrmas)>0:
        if len(progrmas['students'])>=25:
            progrmas.update({'fechaInicio':1})
            progrmas.update({'fechaFinalizacion':(progrmas['fechaInicio']+10)})
        else:
            progrmas.update({'fechaInicio':'En proceso'})
        
        if progrmas['fechaInicio']!='En proceso':
            for key,value in horarios.items():
                if value['cupo']<=2:
                    progrmas['horario']=value['horario']
                    value['cupo']+=1
                    break


            
        campus.update({len(campus)+1:progrmas})

def asignacion(students:dict,trainers:dict,ruta:str):
    progrmas={
        'students':{},
        'ruta':'',
        'trainer':'',
        'horario':''
    }
    idx=1
    for key,value in students.items():
        if value['estado']=='Aprobado' and idx<=33 and not(value['cupo']):
            progrmas['students'].update({len(progrmas['students'])+1:value['id']})                    
            value['cupo']=True
            progrmas['ruta']=ruta
            idx+=1
    for key,value2 in trainers.items():
        if value2['cupo']<2:
            progrmas['trainer']=value2['name']
            value2['cupo']+=1
            break
                    
        

    return progrmas

def movercupos(campus:dict,students:dict):
    x=False
    id=int(input('ingrese el id del estudiante a mover: '))
    for key,value in campus.items():
        for key2,value2 in value['students'].items():
            if id==value2:
                print(f'El estudiante se encuentra en el programa #{key} de la ruta ', {value['ruta']})
                validar=True
                while validar:
                    op=bool(input('desea cambiar al estudiante\n1.Si presiona s\n2.No presiona enter\n'))
                    if op:
                        value['students'].pop(key2)
                        validar=False
                    else:
                        op=False
                x=True
                break
    print('A que programa lo va a mover')
    for key,value in campus.items():
        if len(value['students'])<2:
            print(f'{key}.Programa #{key}. de ', value['ruta'])
    op=int(input('Ingresa una opcion'))
    for i in range(len(campus)):
        if op==i+1:
            campus[op]['students'].update({len(campus[op]['students'])+1:id})
            break
    
def verCupos(campus:dict,students:dict):
    for key,value in campus.items():
        print(f'{key}.Programa {key} de ', value['ruta'],' con horario ',value['horario'])
    op=int(input('Selecciona una opcion: '))
    for i in range(len(campus)):
        if op==i+1:
            mostrarTabla(campus[op],students)

def mostrarTabla(cam:dict,students:dict):
    tabla=[]
    for key,value in cam['students'].items():
        tabla.append([key,value])
        for key2,value2 in students.items():
            if value2['id']==value:
                tabla[key-1].append(value2['name'] + ' ' + value2['lastName'])

    headers=['posicion','id','nombre']
    print(tabulate(tabla, headers=headers, tablefmt='grid'))          