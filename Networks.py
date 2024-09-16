# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:45:42 2024

@author: sreekar
"""

import networkx as nx
import matplotlib.pyplot as plt

'''G =nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())
print(G)
#G=nx.complete_graph()
nx.draw(G)
nx.write_gexf(G,'analysis2.gexf')
print(id(G))
#n=random.randint(1,10)
#print(n)
'''

#g1=nx.gnp_random_graph(20,0.1)
g1=nx.barabasi_albert_graph(50,2)
#nx.draw(G)
nx.draw(g1)
plt.show(1)
nx.write_gexf(g1,'analysis1.gexf')
