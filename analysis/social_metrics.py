import networkx as nx


def basic_info(G):
    print("Number of people:", G.number_of_nodes())
    print("Number of connections:", G.number_of_edges())


def most_connected(G):
    degrees = dict(G.degree())
    max_person = max(degrees, key=degrees.get)
    print("Most connected person:", max_person)
    print("Connections:", degrees[max_person])


def centrality(G):
    centrality = nx.degree_centrality(G)
    for person, value in centrality.items():
        print(person, ":", round(value, 2))