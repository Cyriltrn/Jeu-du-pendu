import random

def choisir_mot():          #Fonctions qui lit le fichier texte et en ressort un mot aléatoire
    f = open('mots_pendu.txt', 'r', encoding='utf-8')  #Ouvre le fichier texte
    mots = f.readlines()                        #lit les lignes de ce fichier
    return random.choice(mots).strip()          #Prend une ligne aléatoire, supprime le saut de ligne avec .strip

def cache_mot(mot_aleatoire):       #Fonction qui affiche le mot caché sous des underscores _
    affiche_mot = ""                #Chaîne initialement vide
    for i in mot_aleatoire:         #On parcourt le mot aléatoire pour connaitre sa taille
        affiche_mot += "_"          #On incrémente pour chaque lettre un équivalent underscore _
    return affiche_mot              #Rend la chaine de caractères _ de la taille du mot aléatoire

#fonction qui vérifie si les lettres sont correctes
def verifier_lettre(lettre, mot_aleatoire, liste_lettre, nb_chances):
    if lettre in mot_aleatoire:                         #si la lettre est dans le mot
        print("\nLa lettre est bien dans le mot.")       #On l'indique
        liste_lettre += lettre            #On incrémente la liste des lettres
    else:
        print("\nLa lettre n'est pas dans le mot.")      #On indique que c'est faux
        nb_chances -= 1                                 #On perd une vie
        print(f"Il vous reste {nb_chances} chances")    #On indique le nombre de vie restantes

    return liste_lettre, nb_chances

def maj_du_mot(mot_aleatoire, liste_lettre):        #On met à jour le mot qui s'affiche au joueur
    mot_cache = ""
    for lettre_soluce in mot_aleatoire:             #On parcourt les lettres du mot à trouver
        if lettre_soluce in liste_lettre:           #Si une lettre fait partie des lettres trouvées
            mot_cache += lettre_soluce              #On incrémente le mot caché avec la lettre qui s'affichera
        else:
            mot_cache += "_"                        #Si les lettres ne correspondent pas on garde l'underscore _
    return mot_cache



def jouer_au_pendu():    #Fonction principale du jeu du pendu
    #Initialisation du jeu
    mot_aleatoire = choisir_mot()
    nb_chances = 6
    liste_lettre = ""
    affichage_mot = cache_mot(mot_aleatoire)

    #Le jeu commence et se termine lorsque le nb de chances est épuisé
    while nb_chances > 0:
        print("\nLe mot à deviner est:", affichage_mot)
        lettre = input("Rentrez une lettre de votre choix: ")

        liste_lettre, nb_chances = verifier_lettre(lettre, mot_aleatoire, liste_lettre, nb_chances)

        affichage_mot = maj_du_mot(mot_aleatoire, liste_lettre)

        if nb_chances == 0:
            print("\nOh non, vous avez perdu...")
            print("le mot à trouver était: ", mot_aleatoire)

        elif affichage_mot == mot_aleatoire:
            print(f"\nVous avez bien trouvé le mot {affichage_mot}, félicitation !\n")
            nb_chances = 0

if __name__ == "__main__":
    choix = 1
    while choix == 1:
        jouer_au_pendu()
        choix = int(input("Vouler vous rejouer? Si Oui tapez 1 sinon tapez 0: "))
        if choix == 0:
            print("Merci d'avoir joué, à la revoyure.")
            break
