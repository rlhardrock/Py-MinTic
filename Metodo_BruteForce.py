""" distancias = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0,
('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B',
'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45,
('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'):
106, ('E', 'D'): 25, ('E', 'E'): 0}
ruta_inicial = ['H', 'B', 'E', 'A', 'C', 'D', 'H']

distancias = {('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
'SMR'): 121, ('CTG', 'CTG'): 0}
ruta_inicial = ['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE'] """

distancias = {('H','H'):0,('H','A'):21,('H','B'):57,('H','C'):58,('H','D'):195,('H','E'):245,('H','F'):241,
    ('A','H'):127,('A','A'):0,('A','B'):231,('A','C'):113,('A','D'):254,('A','E'):179,('A','F'):41,
    ('B','H'):153,('B','A'):252,('B','B'):0,('B','C'):56,('B','D'):126,('B','E'):160,('B','F'):269,
    ('C','H'):196,('C','A'):128,('C','B'):80,('C','C'):0,('C','D'):136,('C','E'):37,('C','F'):180,
    ('D','H'):30,('D','A'):40,('D','B'):256,('D','C'):121,('D','D'):0,('D','E'):194,('D','F'):109,
    ('E','H'):33,('E','A'):144,('E','B'):179,('E','C'):114,('E','D'):237,('E','E'):0,('E','F'):119,
    ('F','H'):267,('F','A'):61,('F','B'):79,('F','C'):39,('F','D'):135,('F','E'):55,('F','F'):0,    }
ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

# def ruteo_(distancias, ruta_inicial):
def ruteo(distancias: dict, ruta_inicial: list)-> dict:

    for arco, longitud in distancias.items():
#if any ((longitud < 0 ) or ((longitud == 0) == (arco[0] != arco [1]) ) or ((longitud != 0) == (arco[0] == arco [1]))):
        #   return 'Por favor revisar los datos de entrada.'
        if longitud < 0:
            return 'Por favor revisar los datos de entrada.'
        else:
            if longitud <= 0 and arco[0] != arco [1]:
                    return 'Por favor revisar los datos de entrada.'
            else:
                if longitud != 0 and arco[0] == arco [1]:
                   return 'Por favor revisar los datos de entrada.'

    def recorrido(distancias: dict, ruta_inicial: list):
        tramo = 0  
        for shift in range(0,len(ruta_inicial)-1):
            tramo = tramo + distancias[(ruta_inicial[shift],ruta_inicial[shift+1])]
        return tramo
    
    #circuito = []
    ruta_progreso = ruta_inicial
    ruta_optima = ruta_inicial
    distancia_optima = recorrido(distancias, ruta_inicial)
    distancia_proceso = distancia_optima

    mejora = False
    paso = True

    while paso == True:
        for origen in range(1, len(ruta_inicial)-2):
            for destino in range(origen+1, len(ruta_inicial)-1):
                swaps = ruta_optima.copy()     # siempre usar  copy () para poder hacer intercambios
                swaps[origen], swaps[destino] = swaps[destino], swaps[origen]
                distancia_cambio = recorrido(distancias, swaps)
                
                if distancia_cambio < distancia_proceso:
                    distancia_proceso = distancia_cambio
                    ruta_progreso = swaps.copy()
                    mejora = True
        
        if mejora == True:
            ruta_optima = ruta_progreso.copy()
            distancia_optima = distancia_proceso
            mejora = False
        else:
            paso = False

    solucion = {'ruta':'-'.join(ruta_optima), 'distancia':distancia_optima}
    return solucion

print(ruteo(distancias,ruta_inicial))