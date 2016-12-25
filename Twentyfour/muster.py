# code by /u/adventofcode2016

import networkx as nx
from itertools import *

f = open('input.txt')
rows = []
for line in f:
  rows.append(line.strip())

nr,nc = len(rows),len(rows[0])
c = {}
G = nx.generators.classic.grid_2d_graph(nr,nc)
for i in xrange(nr):
  for j in xrange(nc):
    if rows[i][j]=='#':
      G.remove_node((i,j))
    if rows[i][j].isdigit():
      c[int(rows[i][j])] = (i,j)

d = {}
for i in xrange(8):
  for j in xrange(8):
    d[i,j]=d[j,i]= nx.shortest_path_length(G,c[i],c[j])

best = 10**100
for p in permutations(range(1,8)):
  l = [0] + list(p) + [0]
  t = sum(d[l[i+1],l[i]] for i in xrange(len(l)-1))
  best = min(t,best)
print best