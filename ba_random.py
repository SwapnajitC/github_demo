import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(23)

G= nx.barabasi_albert_graph(50,40)
nx.draw_networkx(G, with_labels=True)
plt.show()

random.seed(23) # no effect
G= nx.erdos_renyi_graph(50,0.1)
nx.draw_networkx(G, with_labels=True)
