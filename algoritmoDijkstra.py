# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:36:24 2022

@author: FabricoCS
"""

from pqdict import minpq
import networkx as nx
import random
import matplotlib.pyplot as plt

def dijkstra(grafo, origem, destino=None):
    dist = {}  # distância dos caminhos mais curtos para cada nó
    pai = {}  #nó pai (predecessor) em cada caminho mais curto
    caminho = [] #caminho mínimo do algoritmo

    # Armazena custo da distância em um dicionário de fila de prioridade
    pq = minpq()
    for no in grafo:
        if no == origem:
            pq[no] = 0
        else:
            pq[no] = float('inf')
            
    # popitems sempre mostra o nó com custo mínimo
    # Faz a verificação dos nós ainda a explorar, a determinação da distância do nó e a remoção do nó inexplorado
    for no, min_dist in pq.popitems():
        dist[no] = min_dist
        caminho.append(no)
        if no == destino:
            break
        # Verifica se vizinho é um no inexplorado e atualiza a dist caso teja um caminho com menos custo
        for vizinho in grafo[no]:
            if vizinho in pq:
                novo_custo = dist[no] + grafo[no][vizinho]
                if novo_custo< pq[vizinho]:
                    # Atualiza o custo de um nó .
                    pq[vizinho] = novo_custo
                    pai[vizinho] = no
               
    return dist, pai,caminho

if __name__=='__main__':

    
    #Geração grafo1
    grafo1 = {i:{random.randint(1,100): random.randint(1,10) for i in range(random.randint(1,5))} for i in range(1, 101)}
    
    plt.figure(1)
    G1 = nx.Graph(grafo1)
    nx.draw(G1, with_labels=True)
    plt.show()
    
    no_inicial1=random.randint(1,100)
    dist1, pai1,caminho1 = dijkstra(grafo1, no_inicial1)
    print("GRAFO 1")
    print("")
    print("-------------------------------------------")
    print("Origem:", no_inicial1)
    print("Caminhos mínimos desde a origem:", caminho1)
    print("")
    print("Distância", dist1)
    print("")
    print("Pai", pai1)

    plt.figure(2)
    H1 = nx.path_graph(caminho1)
    nx.draw(H1, with_labels=True, node_color="red",width=6)
    plt.show()
    
    #Geração grafo2
    grafo2 = {i:{random.randint(1,100): random.randint(1,10) for i in range(random.randint(1,5))} for i in range(1, 101)}
    plt.figure(3)
    G2 = nx.Graph(grafo2)
    nx.draw(G2, with_labels=True)
    
    no_inicial2=random.randint(1,100)
    dist2, pai2,caminho2 = dijkstra(grafo2, no_inicial2)
    print("-------------------------------------------")
    print("GRAFO 2")
    print("")
    print("Origem:", no_inicial2)
    print("Caminhos mínimos desde a origem:", caminho2)
    print("")
    print("Distância", dist2)
    print("")
    print("Pai", pai2)
   
    plt.figure(4)
    H2 = nx.path_graph(caminho2)
    nx.draw(H2, with_labels=True, node_color="green",width=6)
    plt.show()
    
    #Geração grafo3
    grafo3 = {i:{random.randint(1,100): random.randint(1,10) for i in range(random.randint(1,5))} for i in range(1, 101)}
    plt.figure(5)
    G3 = nx.Graph(grafo3)
    nx.draw(G3, with_labels=True)
    
    no_inicial3=random.randint(1,100)
    dist3, pai3,caminho3 = dijkstra(grafo3, no_inicial3)
    print("-------------------------------------------")
    print("GRAFO 3")
    print("")
    print("Origem:", no_inicial3)
    print("Caminhos mínimos desde a origem:", caminho3)
    print("")
    print("Distância", dist3)
    print("")
    print("Pai", pai3)
   
    plt.figure(6)
    H3 = nx.path_graph(caminho3)
    nx.draw(H3, with_labels=True, node_color="yellow",width=6)
    plt.show()
    
    
    
    