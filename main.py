import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt

f = open("C:\\Users\\aliev\source\\repos\FriendsFriend\FriendsFriend\\bin\Debug\\net7.0\data\\Vertex.txt", "r")
G = nx.Graph()

for c in f.readlines():
    G.add_node(c)

print(G)
nx.draw(G)
plt.savefig("filename.png")
