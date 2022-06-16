# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:25:38 2022

@author: FabricoCS
"""

#função de verificação do caminho mínimo
def Verificar_minimo(no, vizinho, grafo, dist, pai):    
    if dist[no] + grafo[no][vizinho] < dist[vizinho]:
        dist[vizinho]  = dist[no] + grafo[no][vizinho]
        pai[vizinho] = no
       
#função de execução do algoritmo de Bellman_Ford         
def Bellman_Ford(grafo, origem):
    dist, pai = Inicializar(grafo, origem)
    for i in range(len(grafo)-1): #iteração com o tamanho do grafo
        #Para cada nó do grafo fazer a verificação do caminho mínimo a partir de seu vizinho
        for no in grafo:
            for vizinho in grafo[no]:
                Verificar_minimo(no, vizinho, grafo, dist, pai)
            
    return dist, pai

#Função de inicialização do peso(dist) e pai de cada nó
def Inicializar(grafo, origem):
    dist = {}
    pai = {}
    for no in grafo:
        pai[no]= "" #Inicia todos
        dist[no] = float('Inf')#Inicia todos os nós com peso infinito
       
    dist[origem] = 0 # Inicia o peso da origem com 0
    return dist, pai

def Mostrar_caminho(dist,pai,grafo,no_inicial):

    print("-------------------------------------------")
    print("Caminhos mínimos desde o nó:",no_inicial)
    for no in pai:
        for vizinho in pai[no]:
            print("Nó Destino:", no, " Anterior:", vizinho, "Distância:", dist[no], " Pai:", pai[no])
    
    print("Distância", dist)
    print("Pai", pai)

def Main():
    grafo = {
        's': {'a':5,'c':7},
        'a': {'c':6,'d':-4},
        'c': {'c':3,'b':-3},
        'd': {'b':7},
        'b': {'a':-2},
        }
    no_inicial='s'
    print("Nó inicial:", no_inicial)
    pesos, pai = Bellman_Ford(grafo, no_inicial)
    Mostrar_caminho(pesos,pai,grafo,no_inicial)
    
Main();
