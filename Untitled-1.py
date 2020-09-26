#Essai de restitution de contenu en language programmation
#L'utilisation de modules semble de premier abord difficile dû à la réutilisation de fonctions dans les différents modules
requete = input("Quelle action voulez vous réaliser?")
requete = str(requete)
if requete == afficher:
    print("print", "()")
elif requete == "multiplier":
    i = input("Entrez le nombre de facteurs")
    while i == 0:
        n = (i-i)+1
        input("Entrez le facteur n°", (n),":")
        n += 1
    