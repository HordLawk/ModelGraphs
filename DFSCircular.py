import re
from io import StringIO
import csv

path = input()
with open(path, 'r') as f:
    text = f.read()

text = re.sub(r'^\s*%.*$', '', text, flags=re.MULTILINE)
text = re.sub(r'\n+', '\n', text)
num_vertices = int(StringIO(text).readline().split()[-1])
vertex_text, edges_text = re.split(r'\*[^\n]+\n', text)[1:]
e_df = list(csv.reader(StringIO(edges_text), delimiter=' '))
connections = [[] for _ in range(num_vertices)]
for e in e_df:
    connections[int(e[0]) - 1].append(int(e[1]))

whites = list(range(1, num_vertices + 1))
grays = []
blacks = []
first = whites[0]
def dfs(v):
    whites.remove(v)
    grays.append(v)
    if first in connections[v - 1]:
        return 1
    for w in connections[v - 1]:
        if w in whites:
            return dfs(w)
    grays.remove(v)
    blacks.append(v)
    return 0

if(dfs(first)):
    print("Y")
else:
    print("N")