import networkx as nx
import random


def generate_social_network(n=15, p=0.3):
    """
    Génère un réseau social aléatoire.
    n = nombre de personnes
    p = probabilité de connexion
    """
    G = nx.erdos_renyi_graph(n, p)

    # Renommer les sommets en noms simples
    mapping = {i: f"Person_{i}" for i in G.nodes()}
    G = nx.relabel_nodes(G, mapping)

    return G