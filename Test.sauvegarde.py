""" Le but de cet essai est d'intéragir avec l'utilisateur et 
de conserver chacune des intéractions pour les auvegarder ensuite dans un fichier"""

import pickle
import os

os.chdir("C:/Users/asus/Desktop/repertoire")

nouvelle_interaction = True 
sauvegarde = []
while nouvelle_interaction is True:
    interaction = str(input("Entrez ce que vous désirez"))
    sauvegarde.append(interaction)
    encore = int(input("Voulez-vous ajouter une interaction ?       1. Oui  2.Non"))
    if encore > 1:
        nouvelle_interaction = False

print("Vous avez renseigné vos interations avec le programme. Ces dernières sont les suivantes:")
for chaine in enumerate(sauvegarde):
        print(chaine)

with open("fichier.sauvegarde.txt", "wb") as fichier:
    variable = pickle.Pickler(fichier)
    variable.dump(sauvegarde)

fin = input("Le programme a-t-il fonctionné ?")