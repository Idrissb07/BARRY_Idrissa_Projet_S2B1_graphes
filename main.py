from data.network_data import create_social_network
from analysis.social_metrics import basic_info, most_connected, centrality
from visualization.draw import draw_network


def menu():
    G = create_social_network()

    while True:
        print("\n--- SOCIAL NETWORK ANALYSIS ---")
        print("1 - Basic info")
        print("2 - Most connected person")
        print("3 - Centrality")
        print("4 - Show network")
        print("0 - Quit")

        choice = input("Choice: ")

        if choice == "1":
            basic_info(G)

        elif choice == "2":
            most_connected(G)

        elif choice == "3":
            centrality(G)

        elif choice == "4":
            draw_network(G)

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()