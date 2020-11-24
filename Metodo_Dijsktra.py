unvisited = {'A','B','C','D','E','F'}

distances = {('A','B'):5, ('B','A'):5, ('B','C'):6, ('C','B'):6, ('C','D'):8, ('D','E'):8, ('E','F'):10, ('F','E'):10,}

neightbours = {

            'A':['B','D']


}

def dijkstra(unvisited: set, distances:dict,  neightbours:dict,  start:src):
    ''' conocido las distancias iniciales 0 ó inf '''
    know ={node: (0 if nodo == start  else float('infinitum')) for nodo in unvisited}
    ''' desconocido a los nodos '''
    unknow = { nodo : none for nodo in unvisited}
    
    ''' repetir hasta  que se acaben los elementos no visitados'''
    while len(unvisited) > 0:
        ''' visitar el nodo con la menor distancia '''
        
    
    pass
