import networkx as nx
import matplotlib.pyplot as plt
import csv

f1 = csv.reader(open("C:\\Users\\aliev\\Downloads\\Chinim_bitoe.csv"))
G = nx.Graph()
i=0

for row in f1:
    if (i < 3240):
        i+=1
        G.add_nodes_from(row)
        G.add_edge(row[0], row[1])

#plt.figure(3, figsize=(10, 10))
#nx.draw(G, node_size=1, pos=nx.shell_layout(G))
#plt.show()

bet_centr = nx.betweenness_centrality(G)
clo_centr = nx.closeness_centrality(G)
#eig_centr = nx.eigenvector_centrality(G)

print(bet_centr)
print(clo_centr)
#print(eig_centr)

results = [(k,bet_centr[k],clo_centr[k]) #,eig_centr[k]

for k in G]
f = open('Centrality', 'w')
for item in results:
    f.write(','.join(map(str,item)))
    f.write('\n')
f.close()