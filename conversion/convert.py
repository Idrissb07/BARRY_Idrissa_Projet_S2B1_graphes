import networkx as nx


def from_adjacency_matrix(M):
    G = nx.Graph()
    n = len(M)
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != 0:
                G.add_edge(i, j)

    return G


def from_adjacency_list(adj):
    G = nx.Graph()
    for node in adj:
        for neighbor in adj[node]:
            G.add_edge(node, neighbor)

    return G