vuelosEjemplo = [{"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 5, "duracion": 120, "salida":600},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 2, "duracion": 115, "salida":555},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "CTG", "destino": "BOG", "distancia": 295, "retraso": 15, "duracion": 120, "salida":830},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "CTG", "destino": "PEI", "distancia": 325, "retraso": 5, "duracion": 135, "salida":800},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "BOG", "destino": "CLO", "distancia": 255, "retraso": 25, "duracion": 170, "salida":605},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "PEI", "destino": "BOG", "distancia": 220, "retraso": 5, "duracion": 60, "salida":1030},
                 {"aerolinea": "LATAM", 'codigo': "HK301", "origen": "BOG", "destino": "PEI", "distancia": 220, "retraso": 10, "duracion": 30, "salida":2000},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "CLO", "destino": "CTG", "distancia": 400, "retraso": 20, "duracion": 160, "salida":1200}]

def aerolinea_con_vuelos(vuelos: list) -> tuple:
  
    aerolineas = { vuelo['aerolinea'] for vuelo in vuelos }
    contador = { aerolinea : 0 for aerolinea in aerolineas }
    
    for vuelo in vuelos:
        contador[vuelo['aerolinea']] += 1

    mas_vuelos = 0
    mejor_aerolinea = ''

    for empresa in aerolineas:
        if contador[empresa] > mas_vuelos:
            mas_vuelos = contador[empresa]
            mejor_aerolinea = empresa
                
    return (mejor_aerolinea, mas_vuelos)
print(aerolinea_con_vuelos(vuelosEjemplo))

############################################################################################

def aerolinea_con_vuelos_comprension(vuelos: list) -> tuple:

    aerolineas = { vuelo['aerolinea'] for vuelo in vuelos }
    return max ( [ ( sum([ 1 if vuelo['aerolinea'] == aerolinea else 0 for vuelo in vuelos]) ,aerolinea) for aerolinea in aerolineas ] )

print(aerolinea_con_vuelos_comprension(vuelosEjemplo))

############################################################################################

def avion_con_vuelos(vuelos: list) -> tuple:

    aviones = { vuelo['codigo'] for vuelo in vuelos }
    contador = { avion : 0 for avion in aviones }

    for vuelo in vuelos:
        contador[vuelo['codigo']] += 1

    mas_vuelos = 0
    mejor_avion = ''

    for avion in aviones:
        if contador[avion] > mas_vuelos:
            mas_vuelos = contador[avion]
            mejor_avion = avion

    return (mejor_avion, mas_vuelos)
print(avion_con_vuelos(vuelosEjemplo))

############################################################################################

def imprimir_datos(vuelos: list) -> None:

    for vuelo in vuelos:
        print('AQUI EMPIEZA UN NUEVO VUELO')
        for concepto, valor in vuelo.items():
            print('{}:{}'.format(concepto, valor))

imprimir_datos(vuelosEjemplo)

############################################################################################

def ciudad_con_vuelos(vuelos: list) -> tuple:

    ciudades = { vuelo['origen'] for vuelo in vuelos }
    ciudades.union( { vuelo['destino'] for vuelo in vuelos} )
    contador = { ciudad : 0 for ciudad in ciudades }
        
    for vuelo in vuelos:
        contador[vuelo['origen']] += 1
        contador[vuelo['destino']] += 1

    mas_vuelos = 0
    mejor_ciudad = []
   
    for ciudad in ciudades:
        if contador[ciudad] > mas_vuelos:
            mas_vuelos = contador[ciudad]
            mejor_ciudad = [ciudad]
        elif contador[ciudad] == mas_vuelos:
            mejor_ciudad.append(ciudad)

    return (mejor_ciudad, mas_vuelos)
print(ciudad_con_vuelos(vuelosEjemplo))

############################################################################################

def avion_con_uso(vuelos: list) -> tuple:

    aviones = { vuelo['codigo'] for vuelo in vuelos }
    sumador = { avion : 0 for avion in aviones }

    for vuelo in vuelos:
        for avion in aviones:
            if vuelo['codigo'] == avion:
                sumador[avion] += (vuelo['duracion'] + vuelo['retraso'])
    mas_vuelos = 0
    mejor_avion = ''

    for avion in aviones:
        if sumador[avion] > mas_vuelos:
            mas_vuelos = sumador[avion]
            mejor_avion = avion

    return (mejor_avion, mas_vuelos)
print(avion_con_uso(vuelosEjemplo))