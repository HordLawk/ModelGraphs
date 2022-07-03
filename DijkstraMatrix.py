import re
from io import StringIO
import csv
from queue import PriorityQueue
import numpy

path = input()
with open(path, 'r') as f:
    texto = f.read()

texto = re.sub(r'^\s*%.*$', '', texto, flags=re.MULTILINE)
texto = re.sub(r'\n+', '\n', texto)
num_vertices = int(StringIO(texto).readline().split()[-1])
vertex_texto, edges_texto = re.split(r'\*[^\n]+\n', texto)[1:]
e_df = list(csv.reader(StringIO(edges_texto), delimiter=' '))
pesos = [[-1 for _ in range(num_vertices)] for _ in range(num_vertices)]
for e in e_df:
    pesos[int(e[0]) - 1][int(e[1]) - 1] = int(e[2])

distancias = []
for i in range(num_vertices):
    visitados = []
    distanciasVert = [float('inf') for _ in range(num_vertices)]
    distanciasVert[i] = 0
    pq = PriorityQueue()
    pq.put((0, i))
    while not pq.empty():
        (dist, aux) = pq.get()
        visitados.append(aux)
        for vizinho in range(num_vertices):
            if pesos[aux][vizinho] != -1:
                distancia = pesos[aux][vizinho]
                if vizinho not in visitados:
                    custoi = distanciasVert[vizinho]
                    custof = distanciasVert[aux] + distancia
                    if custof < custoi:
                        pq.put((custof, vizinho))
                        distanciasVert[vizinho] = custof
    
    distancias.append(distanciasVert)

transposta = numpy.array([[len(str(el)) for el in e] for e in distancias]).T
for e in distancias:
    print(' '.join([((' ' * (max(transposta[i]) - len(str(el)))) + str(el)) for i,el in enumerate(e)]))