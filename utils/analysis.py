import networkx as nx


def graph_info(G):
    print("Order (number of nodes):", G.number_of_nodes())
    print("Size (number of edges):", G.number_of_edges())

    if nx.is_connected(G.to_undirected()):
        print("Diameter:", nx.diameter(G.to_undirected()))
    else:
        print("Diameter: graph is not connected")

    degrees = dict(G.degree())
    avg_degree = sum(degrees.values()) / G.number_of_nodes()
    print("Average degree:", avg_degree)


def is_regular(G):
    degrees = [G.degree(n) for n in G.nodes()]
    return len(set(degrees)) == 1
