#correos
listaCorreos = []

#facultades
facultades = set()

#diccionario para calculo de notas
diccionarioNotaXFacultad = dict()
#diccionario para calculo de creditos
diccionarioCreditoXFacultad = dict()

#diccionario de los restulados. Clave (facultad) : Valor (promedio ponderado)
diccionarioResultado = dict()

def promedio_facultades(info:dict, contando_externos: bool = True) -> tuple:
    mivariable = info.items()
    
    #ciclo por codigo del estudiante
    try:
        for key, value in mivariable:
            
            #datos generales de cada estudiante
            nombre = value['nombres']                           #nombres
            apellido = value['apellidos']                       #apellidos
            numeroDocumento = str(value['documento'])           #numero de documento
            programaEstudiante = value['programa']              #codigo del programa del estudiante
            materias = value['materias']                        #datos de las materias (global)
            
            if(len(materias) == 0):
                #no tiene ninguna materia
                continue
            
            i = 0
            creacionCorreo = False
            
            while i < len(materias):
                #acceder a los datos de cada materia
                cadaFacultadMateria = materias[i]['facultad']       #nombre de la facultad de la materia
                cadaCodigoMateria = materias[i]['codigo']           #codigo de la materia
                cadaNotaMateria = materias[i]['nota']               #nota en esa materia
                cadaCreditosMateria = materias[i]['creditos']       #creditos de esa materia
                cadaRetiradaMateria = materias[i]['retirada']       #se retiro la materia (Si/No)
    
                if(cadaCreditosMateria == 0 or cadaNotaMateria == 0 or cadaRetiradaMateria == "Si"):
                    #esta materia no cuenta por nota, credito o retirada
                    i = i + 1
                    continue
    
                else:
                    
                    #ahora comprobar si se puede sumar los externos
                    if(contando_externos == True):
                        #aqui toca contar de todo ya que cuenta locales y externos
                        #-----------------------------
                        
                        #añado la facultad del estudiante en un conjunto
                        facultadAdicionada = adicionarFacultad(cadaFacultadMateria)
                        
                        #vamos a proceder a calcular el promedio notas con sus creditos
                        NotasXCreditos(cadaNotaMateria, cadaCreditosMateria, cadaFacultadMateria) 
                        
                        if(creacionCorreo == False):
                            #calcular el correo por estudiante
                            miCorreo = sacarCorreo(nombre,apellido,numeroDocumento)
                        
                            #añadir el correo a una lista
                            listaCorreos.append(miCorreo)
                            
                            creacionCorreo = True
                    
                    #aqui si contando externos es False
                    else:
                        #no vamos a contar los externos
                        #hallando el codigo de externos
                        codigoDeExterno = str(key)
                        codigoExterno = codigoDeExterno[4:6]
                        
                        #hallando que sea su materia de la misma carrera del estudiante
                        #mira si esa materia pertenece a su programa
                        materiaDeSuPrograma = materiaEsDePrograma(programaEstudiante, cadaCodigoMateria, cadaFacultadMateria)
                        if(materiaDeSuPrograma == False or codigoExterno == "05"):
                            #no cuenta para sumarse ya que es externo y no los vamos a tener en cuenta
                            i = i + 1
                            continue
                        
                        else:
                            #si cuenta para sumarse

                            #añado la facultad del estudiante en un conjunto
                            facultadAdicionada = adicionarFacultad(cadaFacultadMateria)
                            
                            #vamos a proceder a calcular el promedio notas con sus creditos
                            NotasXCreditos(cadaNotaMateria, cadaCreditosMateria, cadaFacultadMateria) 
                        
                            if(creacionCorreo == False):
                                #calcular el correo por estudiante
                                miCorreo = sacarCorreo(nombre,apellido,numeroDocumento)
                            
                                #añadir el correo a una lista
                                listaCorreos.append(miCorreo)
                                
                                creacionCorreo = True
    
                i = i + 1
    
        for n in facultadAdicionada:
            #capturar el resultado de cada facultad
            notaDeDiccionario = diccionarioNotaXFacultad[n]
            creditoDeDiccionario = diccionarioCreditoXFacultad[n]
            
            #hacer el calculo de nota / credito
            calculoSinRedondear = notaDeDiccionario / creditoDeDiccionario
            
            #redondear el resultado del calculo
            calculo = round(calculoSinRedondear,2)
            diccionarioResultado[n] = calculo
    
        #ordenar mi diccionario de manera alfabetica    
        diccionarioResultadoOrdenado = dict(sorted(diccionarioResultado.items()))
        
        #ordenar los correos de manera alfabetica
        listaCorreosOrdenada = sorted(listaCorreos)
        
        nuevalista = []
        nuevalista.append(diccionarioResultadoOrdenado)
        nuevalista.append(listaCorreosOrdenada)
        
        tuplaResultado = tuple(nuevalista)
        return tuplaResultado
    except:
        return "Error numérico."










#funcion para almacenar las notas y los creditos
def NotasXCreditos(nota, credito, facultad):
    
    producto = nota * credito
        
    if(facultad in diccionarioNotaXFacultad or facultad in diccionarioCreditoXFacultad):
        
        diccionarioNotaXFacultad[facultad] = producto + diccionarioNotaXFacultad[facultad]
        diccionarioCreditoXFacultad[facultad] = credito + diccionarioCreditoXFacultad[facultad]
        
    else:
        diccionarioNotaXFacultad[facultad] = producto
        diccionarioCreditoXFacultad[facultad] = credito



#funcion para adicionar la facultad en el conjunto
def adicionarFacultad(cadaFacultadMateria):
    facultades.add(cadaFacultadMateria)
    #convertir el conjunto en una lista
    listaFacultades = list(facultades)
    
    #organizar las facultades por orden alfabetico
    listaFacultadesOrganizadas = sorted(listaFacultades)
    return listaFacultadesOrganizadas





#funcion para verificar si esta materia es del programa del estudiante
def materiaEsDePrograma(programaEstudiante, cadaCodigoMateria,cadaFacultadMateria) -> bool:
    #valida si esta materia es de su programa
    if programaEstudiante in cadaCodigoMateria:
        
        #la materia si es de su programa
        materiaDeSuPrograma = True
    else:
        
        #la materia no es de su programa
        materiaDeSuPrograma = False
    return materiaDeSuPrograma





#funcion para crear los correos
def sacarCorreo(x,y,doc):
    #x es nombre
    #y es apellido
    #doc es documento
    
    #armar un array con primer y segundo dato separados
    trozo = x.split()
    trozoApellido = y.split()
    
    if(len(trozo) == 2):
        
        #capturar los nombres
        primerNombre = trozo[0]
        segundoNombre = trozo[1]
        
        #capturar la primera letra de los nombres
        primerCaracter = primerNombre[0]
        segundoCaracter = segundoNombre[0]
        
        #capturar primer apellido
        primerApellido = trozoApellido[1]
        
        #capturar ultimos 2 digitos del documento
        ultimosNumeroDoc = doc[len(doc)-2:len(doc):]
    
        #armar nuestro correo
        correo = primerCaracter + segundoCaracter + "." + primerApellido + ultimosNumeroDoc
    
    elif(len(trozo) == 1):
        
        #capturar el nombre y el primer caracter
        primerNombre = trozo[0]
        primerCaracter = primerNombre[0]
        
        #capturar primer apellido y el primer caracter
        primerApellido = trozoApellido[1]
        primerCaracterApellido = primerApellido[0]
        
        #capturar el segundo apellido
        original = trozoApellido[0]
        segundoApellido = original.replace(",", "")
        
        #capturar ultimos 2 digitos del documento
        ultimosNumeroDoc = doc[len(doc)-2:len(doc):]
        
        #armar nuestro correo
        correo = primerCaracter + primerCaracterApellido + "." + segundoApellido + ultimosNumeroDoc
    
    #convertir nuestro correo a minusculas
    correo = correo.lower()
    
    #quitar tildes y eñes
    for letra in correo:
        if ("á" == letra):
            correo = correo.replace("á", "a")
        elif ("é" == letra):
            correo = correo.replace("é", "e")
        elif ("í" == letra):
            correo = correo.replace("í", "i")
        elif ("ó" == letra):
            correo = correo.replace("ó", "o")
        elif ("ú" == letra):
            correo = correo.replace("ú", "u")
        elif ("ñ" == letra):
            correo = correo.replace("ñ", "n")

    return correo
