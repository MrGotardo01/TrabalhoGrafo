# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:20:29 2022

@author: FabricoCS
"""

#representação da lista de adjacência do grafo
grafo = {
    'a':['b','c'],
    'b':['d', 'e'],
    'c':['b','f'],
    'd':[],
    'e':['f'],
    'f':[]
}

#definição de dicionário vazio de cores para atribuição de vértices visitados e não visitados 
#B - Branco: vértices não visitados, C - cinza: vértice explorado pela 1ª vez, P - preto: vértice totalmente explorado
cor = {}   
pai = {}  #definição de dicionário vazio para guardar o pai de cada vértice  
tempo_trav = {} # [inicio, fim]   - dicionário vazio para guardar o tempo de travessia inicial e final de cda vértice
caminho = []  #definição de lista para guardar o percurso DFS  

#inicialização de cada vértice do grafo
for v in grafo.keys():
    cor[v] = "B" 
    pai[v] = None
    tempo_trav[v] = [-1,-1]
    
#função para o algortimo DFS
time = 0
def dfs_util(u):
    global time
    cor[u] = "C" 
    tempo_trav[u][0] = time
    caminho.append(u)
    time +=1
    
    #explora todos os vértices adjacentes,verifica se foi ou não visitado, determina seu vértice pai,
    #define o tempo de travessia do vértice
    for v in grafo[u]:
        if cor[v] == "B":
            pai[v] = u     
            dfs_util(v)
    cor[u] = "P"
    tempo_trav[u][1] = time
    time +=1

#encontra o vértice de origem e executa o algoritmo DFS a partir disso
for u in grafo.keys():
    if cor[u] == "B":   
        dfs_util(u)

#imprime o caminho DFS    
print("DFS = ",caminho)
#imprime o pai de cada vértice
print("\nPai de cada vértice")
for v in grafo.keys():
    print(v, " ->", pai[v])
#imprime o tempo de travessia de cada vértice 
print("\nTempo de Travessia de cada vértice")
for v in grafo.keys():
    print(v, " ->", tempo_trav[v])

