from data.generate_network import generate_social_network
from analysis.metrics import *
from visualization.display import draw_graph
import numpy as np


def menu():
    G = generate_social_network()

    while True:
        print("\n--- ANALYSE RESEAU SOCIAL ---")
        print("1 - Afficher le graphe")
        print("2 - Degré de chaque personne")
        print("3 - Personne la plus influente")
        print("4 - Composantes connexes")
        print("5 - Cliques")
        print("6 - Diamètre")
        print("7 - Détection des communautés")
        print("8 - Conversion matrice -> graphe")
        print("0 - Quitter")

        choice = input("Choix : ")

        if choice == "1":
            draw_graph(G)

        elif choice == "2":
            print(degrees(G))

        elif choice == "3":
            person, value = most_influential(G)
            print("Personne la plus influente :", person)
            print("Nombre de connexions :", value)

        elif choice == "4":
            print(connected_components(G))

        elif choice == "5":
            print(cliques(G))

        elif choice == "6":
            print(network_diameter(G))

        elif choice == "7":
            communities = detect_communities(G)
            draw_graph(G, communities)

        elif choice == "8":
            M = np.array([
                [0,1,1],
                [1,0,1],
                [1,1,0]
            ])
            G2 = from_adjacency_matrix(M)
            draw_graph(G2)

        elif choice == "0":
            break

        else:
            print("Choix invalide")


if __name__ == "__main__":
    menu()