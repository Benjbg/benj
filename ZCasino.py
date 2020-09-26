from random import randrange
from math import ceil
print("Bonjour et bienvenue dans notre Casino !")
print("Nous sommes heureux de vous proposer une partie de roulette")
portefeuille = 500
print("Au début de la partie, vous disposer de {}$".format(portefeuille))

regles = input("Avez vous besoin d'un rappel des règles?    1. Oui  2.Non")
regles = int(regles)
if regles <2:
    print("50 numéros sont présentés sur la roulette allant de 0 à 49 et de deux couleurs différentes:")
    print("les nombres pairs sont noirs et les nombres impairs sont rouges")
    print("Vous devez choisir un numéro et miser la sommes qui vous convient sur celui-ci")
    print("En cas de victoire, vous remportez 3 fois votre mise.\
         Dans le cas où le numéro gagnant est de la même couleur que celui de votre mise, vous remportez la moitié de votre mise")
nouvelle_partie = True
while nouvelle_partie == True and portefeuille >0:
    numero = input("Sur quel numéro voulez-vous miser ?")
    numero = int(numero)
    couleur = numero % 2
    print("Votre portefeuille de jeu s'élève à {}$".format(portefeuille))
    mise = input("Combien voulez-vous miser sur ce numéro ?")
    mise = int(mise)
    portefeuille -= mise
    aleatoire = randrange(50)
    print(aleatoire)

    if aleatoire == numero:
        mise *= 3
        portefeuille += mise
        print("Vous avez gagné ! Vos gains sont de {}$ élevant votre portefeuille à {}$ !". format(mise, portefeuille))
    elif couleur == (aleatoire % 2):
        mise *=0.5
        mise = ceil(mise)
        portefeuille += mise
        print("Vous remportez la couleur ! Vos gains sont de {}$ élevant votre portefeuille à {}$ !".format(mise, portefeuille))
    else : 
        print("Dommage, retentez pour gagner au prochain tour !")

    if portefeuille >0: 
        fin_partie = input("Voulez-vous refaire une partie ?    1. Oui  2. Non")
        fin_partie = int(fin_partie)
        if fin_partie > 1:
            nouvelle_partie = False

print("Merci d'avoir participé à notre jeu. Le montant de votre portefeuille de jeu est de {}$, nous espérons vous revoir rapidement !".format(portefeuille))
