import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()
G.add_node("Title")
G.add_node("Title2")
G.add_node("Title3")
G.add_node("Title4")
G.add_edge("Title","Title2")


nx.draw(G)
plt.show()
