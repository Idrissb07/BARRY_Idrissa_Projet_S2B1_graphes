import numpy as np
import networkx as nx


def graph_from_matrix():
    M = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ])

    G = nx.Graph()
    n = len(M)
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != 0:
                G.add_edge(i, j)

    return G
