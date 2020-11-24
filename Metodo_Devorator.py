#({('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
#'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
#'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
#'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
#'SMR'): 121, ('CTG', 'CTG'): 0},['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']))

# ruta_inicial = ['BOG','MED','PEI','SMR','CTG']

# distancias = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
# ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
# ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
# ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
# ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
# ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

# ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E']

distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
              ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
              ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
              ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
              ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
              ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
              ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F']

def ruteo(distancias: dict, ruta_inicial: list)-> dict:

    circuito = []                #variable concatenador
    desplazamiento = 0           #variable acumulador
    
    
    descarte = {}                #rutas descartadas
    for estacion in ruta_inicial :
        descarte.update({estacion:0})
    
    origen = ruta_inicial[0]     #inicio del recorrido
    
    for transito in range(1, len(ruta_inicial)):
        trazas = []
        
        for estacion in ruta_inicial :
            if estacion != origen and descarte[estacion]==0:
                recorrido = (origen, estacion)
                trazas.append(recorrido) # agregar a lugares
         
        max_distancia=[]
        for dst_tmp in distancias:
            max_distancia.append(distancias[dst_tmp])
        max_num=max(max_distancia)
               
        for recorrido in trazas:
            if distancias[recorrido] < max_num:
                max_num = distancias[recorrido]
                ruta_min = (max_num,recorrido)
                   
        circuito.append(ruta_min[1])
        desplazamiento = desplazamiento + ruta_min[0]
        
        descarte[ruta_min[1][0]] = 1
        descarte[ruta_min[1][1]] = 1
        origen = ruta_min[1][1]
        
    regreso = (origen, ruta_inicial[0])
    circuito.append(regreso)
    desplazamiento = desplazamiento + distancias[regreso]
    
    final = {}
    final.update({'ruta':circuito})  
    final.update({'distancia':desplazamiento})
    
    final = {'ruta':circuito,'distancia':desplazamiento}
    
    return final

print(ruteo(distancias,ruta_inicial))


# circuito = [('H', 'A'), ('A', 'F'), ('F', 'C'), ('C', 'E'), ('E', 'B'), ('B', 'D'), ('D', 'H')]
# ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F']
# origen = ruta_inicial[0] 

# breaker = [origen]
# for paso in range(0,len(circuito)-1):
#         salame = list(circuito[paso])
#         cartuche = salame.pop(0)
#         salame = str(salame)
#         breaker.append(salame)
# breaker.append(origen)
# print(breaker)



