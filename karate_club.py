import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community.modularity_max import greedy_modularity_communities

G = nx.karate_club_graph()

# nodes that represent John and Mr.Hi
color = ["#1f78b4"] * 34
color[33] = "yellow"  # Actual John
color[0] = "white"  # Actual Mr.Hi

# Actual John Node is 0, all associated with John are RED
# Actual Mr.Hi Node is 33, all associated with Mr.Hi are GREEN

# get club labels
labels = nx.get_node_attributes(G, 'club')
print(sorted(labels.items(), key=lambda kv: (kv[1], kv[0])))

# establish spring as a variable
spring = nx.spring_layout(G)

# Find the communities of this graph
c = list(greedy_modularity_communities(G))

# print(c) # The output is 3, so we have 3 communities

# Sort the community data
community_0 = sorted(c[0])
community_1 = sorted(c[1])
community_2 = sorted(c[2])

# Combine the like communities for form Mr.Hi's community
combined_community = community_1 + community_2
# print(combined_community)
# print(community_0)
# print(community_1)
# print(community_2)


# Draw the graphs according to community

nx.draw(G, spring, with_labels=True)
nx.draw_networkx_nodes(G, spring, nodelist=community_0, node_color='r', alpha=1, node_size=800)
nx.draw_networkx_nodes(G, spring, nodelist=combined_community, node_color='green', alpha=1, node_size=800)
nx.draw_networkx_edges(G, spring, style='solid', width=0.5)

# This is included to demonstrate that they are in fact sorted by member prediction.
# nx.draw_networkx_labels(G, spring, labels, font_size=9)

plt.show()
