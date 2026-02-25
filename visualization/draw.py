import matplotlib.pyplot as plt
import networkx as nx


def draw_network(G):
    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightgreen",
        edge_color="gray",
        font_size=10
    )

    plt.title("Social Network Graph")
    plt.show()