import networkx as nx
from utils.display import draw_graph
from utils.analysis import graph_info, is_regular
from graphs.example_matrix import graph_from_matrix
from graphs.example_dict import graph_from_dict


def simple_graph():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
    return G


def menu():
    while True:
        print("\n--- GRAPH ANALYSIS TOOL ---")
        print("1 - Simple graph")
        print("2 - Graph from adjacency matrix")
        print("3 - Graph from adjacency list")
        print("0 - Quit")

        choice = input("Choice: ")

        if choice == "1":
            G = simple_graph()
            graph_info(G)
            print("Regular graph:", is_regular(G))
            draw_graph(G, title="Simple Graph")

        elif choice == "2":
            G = graph_from_matrix()
            graph_info(G)
            draw_graph(G, title="Graph from Matrix")

        elif choice == "3":
            G = graph_from_dict()
            graph_info(G)
            draw_graph(G, title="Graph from Adjacency List")

        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
