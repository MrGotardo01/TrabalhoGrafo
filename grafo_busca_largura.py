# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 22:38:15 2022

@author: FabricoCS
"""
#importação da Class de Fila
from queue import Queue

#definição da lista de adjacência do grafo
grafo = {
    'a': ['b', 'd'],
    'b': ['a', 'c'],
    'c': ['b'],
    'd': ['a', 'e', 'f'],
    'e': ['d', 'f', 'g'],
    'f': ['d', 'e', 'h'],
    'g':['e', 'h'],
    'h':['g','f']
}

visitado = {} #definição de dicionário vazio para atribuição de vértices visitados e não visitados 
largura = {} #definição de dicionário vazio para guardar a distância de cada vértice para origem
pai = {} #definição de dicionário vazio para guardar o pai de cada vértice
caminho = [] #definição de lista para guardar o percurso BFS
queue = Queue() #inicialização de fila vazia

#inicialização de cada vértice do grafo
for v in grafo.keys():
    visitado[v] = False 
    pai[v] = None
    largura[v] = -1
    
#inicialização e definição vértice de origem
s = 'h'
visitado[s] = True
largura[s] = 0
queue.put(s) #adição do vértice na fila

#enquanto a fila não for vazia continuar a busca. Grafos nao-conexos nao estao sendo tratados!
while not queue.empty():
    u = queue.get() #retira o primeiro elemento da fila
    caminho.append(u) #marca o vértice como visitado e adiciona ao percurso BFS

    #explora todos os vértices adjacentes,determina se foi ou não visitado, determina seu vértice pai,
    #define a largura do vértice
    for v in grafo[u]:
        if not visitado[v]: #se não foi visitado então...
            visitado[v] = True
            pai[v] = u
            largura[v] = largura[u]+1
            queue.put(v) #adiciona o vértice a fila

#imprime o caminho BFS
print("BFS = ",caminho)
#imprime o pai de cada vértice
print("\nPai de cada vértice")
for v in grafo.keys():
    print(v, " ->", pai[v])
#imprime o nível de cada vértice 
print("\nLargura de cada vértice")
for v in grafo.keys():
    print(v, " ->", largura[v])

         
