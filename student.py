def AddStudent(source:dict):
    id=int(input('Ingrese su nro de identificacion (sin espacios): '))
    name=str(input('Ingrese los nombres del estudiante: ')).capitalize()
    lastName=str(input('Ingrese los apellidos del estudiante: ')).capitalize()
    age=int(input(f'Ingrese la edad de {name}: '))
    direccion={}
    for i in range(2):
        print('1.carrera\n2.calle\n3.Trasversal\n4.Diagonal')
        op=int(input(f'ingrese el valor {i} de su direccion: '))
        if op==1:
            x=str(input('Ingresa la carrera: '))
            direccion.update({'kra':x})
            pass
        elif op==2:
            x=str(input('Ingresa la calle: '))
            direccion.update({'cl':x})
            pass
        elif op==3:
            x=str(input('Ingresa la Trasversal: '))
            direccion.update({'tv':x})
            pass
        elif op==4:
            x=str(input('Ingresa la diagonal: '))
            direccion.update({'diag':x})
            pass
    Aid=int(input('Ingrese su nro de identificacion del acudiente (sin espacios): '))
    Aname=str(input('Ingrese los nombres del acudiente: ')).capitalize()
    AlastName=str(input('Ingrese los apellidos del acudiente: ')).capitalize()
    celular=int(input('Ingrese su nro de telefono celular(sin espacios): '))
    fijo=int(input('Ingrese su nro de telefono fijo(sin espacios): '))
    
    
    estudiante={
        'id':id,
        'name':name,
        'lastName':lastName,
        'age':age,
        'direccion':direccion,
        'acudiente':{
                            'Aid':Aid,
                            'Aname':Aname,
                            'AlastName':AlastName,
                                    },
        'contacto':{
                            'celular':celular,
                            'fijo':fijo
                            },
        'estado':'Inscrito',
        'cupo':False,
        'notas':{
            1:{
                'quices':[],
                'trabajos':[],
                'examenes':[]
            },
            2:{
                'quices':[],
                'trabajos':[],
                'examenes':[]
            },
            3:{
                'quices':[],
                'trabajos':[],
                'examenes':[]
            },
            4:{
                'quices':[],
                'trabajos':[],
                'examenes':[]
            },
            5:{
                'quices':[],
                'trabajos':[],
                'examenes':[]
            }
        }
    }
    source.update({len(source):estudiante})


def pruebaInicial(source:dict):
    id=int(input('Ingrese el id de la persona a la que va a registrar la nota inicial'))
    resultadoInicial=float(input('ingrese el resultado de la prueba inicial'))
    for key, value in source.items():
        if resultadoInicial>=60:
            if id==value['id']:
                value.update({'pruebaInicial':resultadoInicial})
                value['estado']='Aprobado'
                break
            else:
                print('El id no esta en el sistema')
        else:
            value.update({'pruebaInicial':resultadoInicial})
            value['estado']='no-Aprobado'
            break


def deleteStudent(source:dict):
    id=int(input('Ingrese el id del estudiante a borrar: '))
    for key, value in source.items():
        if id==value['id']:
            source.pop(key)
            break