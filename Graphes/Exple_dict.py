import networkx as nx


def graph_from_dict():
    adj = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    G = nx.Graph()
    G.add_nodes_from(adj.keys())

    for k in adj:
        for v in adj[k]:
            G.add_edge(k, v)

    return G
