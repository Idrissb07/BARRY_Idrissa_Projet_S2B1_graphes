import networkx as nx
import community as community_louvain


def degrees(G):
    return dict(G.degree())


def most_influential(G):
    deg = dict(G.degree())
    max_person = max(deg, key=deg.get)
    return max_person, deg[max_person]


def connected_components(G):
    return list(nx.connected_components(G))


def cliques(G):
    return list(nx.find_cliques(G))


def network_diameter(G):
    if nx.is_connected(G):
        return nx.diameter(G)
    else:
        return "Le réseau n'est pas connexe"


def detect_communities(G):
    partition = community_louvain.best_partition(G)
    return partition