"""Les dictionnaires peuvent contenir, au même titre que les listes, plusieurs objets.
Toutefois ils sont utilisable à leur simple appel. Qui plus est, ils peuvent contenir des fonctions.
Le but de ce test est de jouer avec ces fonctions et de voir à quel point les fonctions peuvent être utilisables"""
#exemple 1
print_2 = print
print_2("") #Indiquer la chaine de caractères à afficher

#exemple 2
def fete():
    print("C'est la fête.")
def oiseau():
    print("Fais comme l'oiseau ...")
fonction = {"fete":fete, "oiseau":oiseau}
fonction["oiseau"]() #L'appel de la fonction va la faire fonctionner

#essai 1
def carre():
    n = float(input("Entrez le facteur que vous voulez:"))
    n *= n
    return n
fonction["carre"] = carre #Utilisation d'une fonction stockée
liste = []
while len(liste) < 5:
    i = fonction["carre"]()
    i
    print(i)
    liste.append(i) #Récupération des données trouvées et utilisation pour compléter une autre commande
print(liste)

"""En partant du principe que nous pouvons utiliser un dictionnaire pour stocker des fonctions pré-établies,
ayant une intéraction avec l'utilisateur -intéraction que nous pouvons récupérer-,
il peut être possible d'avoir une intéraction plus approfondie et moins encadrée avec le langage ?"""

"""Prochain objectif: réaliser un appel à une fonction intégrée à un dictionnaire sans passer par la commande directement"""