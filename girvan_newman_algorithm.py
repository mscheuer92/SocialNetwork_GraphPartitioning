import matplotlib.pyplot as plt
import networkx as nx

# Girvan-Newman Algorithm
# 1. Calculate betweenness of all edges
# 2. Remove edges(s) with highest betweenness
# 3. Repeat 1 and 2 until the graph is partitioned into as many regions as desired
from networkx.algorithms.community import greedy_modularity_communities

G = nx.karate_club_graph()

clusterCount = nx.number_connected_components(G)
edgeCount = nx.number_of_edges(G)

color = ["#1f78b4"] * 34
color[0] = "green"  # Mr. Hi
color[33] = "red"   # John

while edgeCount > 0 and clusterCount < 2:
    try:
        allEdgeBetweenness = nx.edge_betweenness_centrality(G)
        max_betweenness = max(allEdgeBetweenness.values())
        max_edge = max(allEdgeBetweenness.items(), key=lambda x: x[1])[0]
        G.remove_edge(*max_edge) # unpack tuple
        print(max_edge)
    except ValueError: # this eliminates max() arg empty sequence error when we get to the end of the loop
        break

    nx.draw_spring(G, with_labels=True, node_color=color)
    plt.show()
