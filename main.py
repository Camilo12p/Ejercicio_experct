import menu as m

students={
    # 1: {'id': 1,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'pruebaInicial':20,
    #     'notas':{
    #         1:{
    #             'quices':[20,30],
    #             'trabajos':[20],
    #             'examenes':[30]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     }     
    #     },
    # 2: {'id': 2,
    #     'name': 'Jose', 
    #     'lastName': 'Patiño',
    #     'age': 22, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[70],
    #             'trabajos':[70],
    #             'examenes':[70]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } },
    # 3: {'id': 3,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } 
    #     },
    # 4: {'id': 4,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } 
    #     },
    # 5: {'id': 5,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } },
    # 6: {'id': 6,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } },
    # 7: {'id': 7,
    #     'name': 'Camilo', 
    #     'lastName': 'Patiño',
    #     'age': 21, 
    #     'direccion': {'kra': '26a', 'cl': '11'},
    #     'acudiente': {'Aid': 9, 'Aname': 'Luz elena', 'AlastName': 'Martinez'}, 
    #     'contacto': {'celular': 3145052248, 'fijo': 1}, 
    #     'estado': 'Aprobado',
    #     'cupo':False,
    #     'notas':{
    #         1:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         2:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         3:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         4:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         },
    #         5:{
    #             'quices':[],
    #             'trabajos':[],
    #             'examenes':[]
    #         } 
    #     } }
}

rutas={
    'java':{
        1:['Pseint','Pyhon'],
        2:['html','css','bootstraps'],
        3:'java',
        4:['MySQL','MongoDb'],
        5:'Spring Boot'

    },
    'javaScript':{
        1:['Pseint','Pyhon'],
        2:['html','css','bootstraps'],
        3:'javaScript',
        4:['MySQL','Postgresql'],
        5:'Node Js y Express'
    },
    'c#':{
        1:['Pseint','Pyhon'],
        2:['html','css','bootstraps'],
        3:'C#',
        4:['MongoDb','Postgresql'],
        5:'NetCore'

    }
}

trainers={
    1:{
        'name':'Joiver Solano',
        'cupo':0
    },
    2:{
        'name':'Trainer 2',
        'cupo':0
    },
    3:{
        'name':'Trainer 3',
        'cupo':0
    }
}
horarios={
        1:{
            'horario':'6 am a 9 am',
            'cupo':0
        },
        2:{
            'horario':'10 am a 1 pm',
            'cupo':0
        },
        3:{
            'horario':'2 pm a 5 pm',
            'cupo':0
        },
        4:{
            'horario':'5 pm a 9 pm',
            'cupo':0
        }
}
campus={
   #1: {'students': {1: 1, 2: 2}, 'ruta': 'java', 'trainer': 'Joiver Solano', 'horario': '6 am a 9 am', 'fechaInicio': 1, 'fechaFinalizacion': 11}, 2: {'students': {1: 3, 2: 4}, 'ruta': 'c#', 'trainer': 'Joiver Solano', 'horario': '6 am a 9 am', 'fechaInicio': 1, 'fechaFinalizacion': 11}, 3: {'students': {1: 5, 2: 6}, 'ruta': 'javaScript', 'trainer': 'Trainer 2', 'horario': '6 am a 9 am', 'fechaInicio': 1, 'fechaFinalizacion': 11}, 4: {'students': {1: 7}, 'ruta': 'c#', 'trainer': 'Trainer 2', 'horario': '', 'fechaInicio': 'En proceso'}

}

validar=True
while validar:
    try:
        m.Principal()
        print('1.Inscribir Estudiante\n2.Asignar cupos\n3.Asignar Notas\n4.Salir.')
        op=int(input('Selecciona una opcion: '))
        if op==1:
            m.AddStudent(students)
            
            input()
            pass
        elif op==2:
            m.asignarCupos(campus,students,rutas,trainers,horarios)
            
            input()
            pass
        elif op==3:
            m.asignarNotas(campus,students,rutas,horarios)
            m.n.validarEstado(students)
            
            input()
            pass
        elif op==4:
            validar=False
            input()
    except ValueError: 
        print('Ingrese un valor valido')