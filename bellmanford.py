class Graph:

	def __init__(self, vertices):
		self.V = vertices # Nº de vértices
		self.graph = []

	# função para adicionar uma aresta ao gráfico
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
		
	# função utilitária usada para imprimir a solução
	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))
	
# A função principal que encontra as distâncias mais curtas de src a
# todos os outros vértices usando o algoritmo de Bellman-Ford. A função
# também detecta ciclo de peso negativo
	def BellmanFord(self, src):

# Passo 1: Inicialize as distâncias de src para todos os outros vértices
# como INFINITO
		dist = [float("Inf")] * self.V
		dist[src] = 0


# Passo 2: Relaxe todas as arestas |V| - 1 vezes. Um simples mais curto
# caminho de src para qualquer outro vértice pode ter no máximo |V| - 1
# arestas
		for _ in range(self.V - 1):
# Atualiza o valor dist e o índice pai dos vértices adjacentes de
# o vértice escolhido. Considere apenas os vértices que ainda estão em
# fila
			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						dist[v] = dist[u] + w

# Etapa 3: verifique se há ciclos de peso negativo. O passo acima
# garante distâncias mais curtas se o gráfico não contiver
# ciclo de peso negativo. Se conseguirmos um caminho mais curto, então
# é um ciclo.

		for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						print("Graph contains negative weight cycle")
						return
						
		#imprimir toda a distância
		self.printArr(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Imprima a solução
g.BellmanFord(0)