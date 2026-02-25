import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G, communities=None, export=False):
    pos = nx.spring_layout(G)

    degrees = dict(G.degree())
    sizes = [degrees[node] * 300 + 300 for node in G.nodes()]

    if communities:
        colors = [communities[node] for node in G.nodes()]
    else:
        colors = "skyblue"

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=sizes,
        node_color=colors,
        cmap=plt.cm.Set3,
        edge_color="gray"
    )

    plt.title("Analyse du réseau social")

    if export:
        plt.savefig("reseau_social.png")

    plt.show()