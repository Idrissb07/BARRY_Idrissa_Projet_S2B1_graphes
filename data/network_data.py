import networkx as nx


def create_social_network():
    G = nx.Graph()

    G.add_edges_from([
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David"),
        ("Charlie", "David"),
        ("David", "Emma"),
        ("Emma", "Frank"),
        ("Frank", "Alice"),
        ("Charlie", "Emma")
    ])

    return G