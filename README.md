### BARRY_Idrissa_Projet_S2B1_graphes

Projet Graphes S2 B1

## Analyse d’un réseau social à l’aide des graphes

# Fonctionnalités

- Charger un réseau social (JSON, CSV ou généré automatiquement)
- Afficher le graphe avec couleurs :
- nœuds = personnes
- couleurs = communautés
- taille du nœud = degré (influence)

# Calculer :

- degré de chaque personne
- personnes les plus influentes
- composantes connexes
- cliques (groupes d’amis très soudés)
- diamètre du réseau
- Conversion :
- matrice d’adjacence → graphe
- liste d’adjacence → graphe
- Menu interactif
  
# En resumé: 

Mon projet modélise un réseau social sous forme de graphe non orienté.
Chaque personne est un sommet et chaque relation est une arête.
Le programme permet d’afficher le réseau avec une visualisation dynamique:
    la taille des nœuds dépend du degré (plus une personne a d’amis, plus son nœud est grand)
    les couleurs représentent les communautés détectées automatiquement avec l’algorithme de Louvain
on peut calculer le diamètre du réseau, les cliques, les composantes connexes
on peut convertir une matrice d’adjacence ou une liste d’adjacence en graphe
Le menu interactif permet de tester toutes les fonctionnalités facilement

# Technologies

- Python
- NetworkX
- Matplotlib
- Algorithme de Louvain

# Pour lancer; il faut installer les dépendances :
pip install -r requirements.txt
Puis exécuter python main.py