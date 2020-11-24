    #MinTic 2020 Reto 1
print("REP-COLOMBIA MINTIC - UTP  2020 // DATA SCIENCE ENGINEERING")


#Lista de contenedores
notas=[]
rendimiento=[]
estudiantes=[]

#forma dinamica para evaluar diferentes cantidades de estudiantes
mercenarios=int (input ("Digite cantidad de estudiantes a evaluar: "))

striker=0
while striker<mercenarios:
#ingreso de nombres en la lista de estudiantes  
    alias=input ("Digite Nombre o Codificacion del estudiante a evaluar: ")
    estudiantes.append(alias)


    #forma dinamica para evaluar diferentes notas
    cantidad_notas = int (input ("Digite la cantidad de notas a calcular: "))
    
    counter=0
    while counter<cantidad_notas:
    #ingreso de calificaciones en la lista notas para halla el promedio    
        calificacion=int(input("Ingrese las calificaciones entre 0 y 100: "))
        escala=round((calificacion*0.05),2)
    #condiciones de calificacion entre 0 y 100, escalado a 0 y 5    
        if (escala>=0 and escala<=5):
            notas.append(escala)
            counter = counter + 1
        else:
            print("Error! Calificacion fuera de rango, escribalo de nuevo")
            #contador = contador - 1 
    
    #cambio de orden a descendente y eliminacion del ultimo elemento
    notas_ord=sorted(notas, reverse=True)
    notas_ord.pop()
    
    #Test de resultados
    print(notas)
    print(notas_ord)
    
    #Obtener promedio
    def promedio_ind(notas_ord):
        suma=0
        for scorpio in notas_ord:
            suma+=scorpio
            promedio=round(suma/(len(notas_ord)),2)
    #ingreso a la lista de general de promedio por estudiante
            rendimiento.append(promedio)
        print ("el promedio del estudiante es: " + str(promedio))
    promedio_ind(notas_ord)
    #Test de resultados
    print(rendimiento) 
