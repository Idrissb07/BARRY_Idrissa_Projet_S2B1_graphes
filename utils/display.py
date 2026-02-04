import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(G, layout="spring", title="Graph"):
    plt.figure(figsize=(7, 6))

    if layout == "spring":
        pos = nx.spring_layout(G)
    elif layout == "circular":
        pos = nx.circular_layout(G)
    elif layout == "kamada":
        pos = nx.kamada_kawai_layout(G)
    else:
        pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1200,
        node_color="skyblue",
        edge_color="black",
        font_size=12,
        width=2,
        arrows=G.is_directed()
    )

    weights = nx.get_edge_attributes(G, "weight")
    if weights:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    plt.title(title)
    plt.show()
