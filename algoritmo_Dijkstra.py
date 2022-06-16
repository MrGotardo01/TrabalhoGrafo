# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:46:34 2022

@author: FabricoCS
"""

from pqdict import PQDict

def dijkstra(G, inicio, fim=None):
    '''
    Implementação do algoritmo de Dijkstra em python
    '''
    inf = float('inf')
    D = {inicio: 0}          # mapeamento de nós para sua distância desde o início
    Q = PQDict(D)           # fila de prioridade para rastrear o caminho mínimo
    P = {}                  # mapeamento de nós para seus predecessores diretos ''Pai''
    U = set(G.keys())       # nós inexplorados

    # Fazer a verificação dos nós ainda a explorar, determinação da distância do nó e remoção do nó inexplorado
    while U:                                    
        (v, d) = Q.popitem()                    
        D[v] = d                                
        U.remove(v)                             
        if v == fim: break

        # considerar as arestas de v com um no inexplorado e atualizar a dist de sucessores inexplorados 
        for w in G[v]:                          
            if w in U:                          
                d = D[v] + G[v][w]             
                if d < Q.get(w, inf):
                    Q[w] = d                    
                    P[w] = v                    

    return D, P

if __name__ == '__main__':

    graph = {'x': {'a': 3, 'c': 4, 'e': 10, 'b': 8},
             'a': {'c': 6, 'x': 3},
             'b': {'x': 8, 'd': 2},
             'c': {'a': 6, 'x': 4, 'd': 1, 'e': 3},
             'd': {'b': 2, 'c': 1, 'e': 1},
             'e': {'c': 3, 'x': 10, 'd': 1}}
    
    no_inicial='x'
    dist, pai = dijkstra(graph, no_inicial)
print("Nó inicial:", no_inicial)    
print("-------------------------------------------")
print("Caminhos mínimos desde o nó:", no_inicial)    
print("Distância", dist)
print("Pai", pai)

