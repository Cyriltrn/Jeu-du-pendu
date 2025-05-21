'''
        Programme de Cyril Traineau
-----------Jeu du pendu--------------
        MGA802 - Python - 21/05/2025
'''

import random       #Bibliothèque permettant de choisir un item random

"""------------Début des Fonctions------------"""

def choisir_mot():          #Fonctions qui lit le fichier texte et en ressort un mot aléatoire
    f = open('mots_pendu.txt', 'r', encoding='utf-8')  #Ouvre le fichier texte par défaut selon l'encodage de caractère utf8
    mots = f.readlines()                        #lit les lignes de ce fichier
    return random.choice(mots).strip()          #Rend une ligne aléatoire (un mot), supprime le saut de ligne avec .strip

def cache_mot(mot_aleatoire):       #Fonction qui affiche le mot caché sous des underscores _
    affiche_mot = ""                #Chaîne initialement vide
    for i in mot_aleatoire:         #On parcourt le mot aléatoire pour connaitre sa taille
        affiche_mot += "_"          #On incrémente pour chaque lettre un équivalent underscore _
    return affiche_mot              #Rend la chaine de caractères _ de la taille du mot aléatoire

# Cas ou l'utilisateur à déjà son fichier de mots
def choisir_mot_fichier(fichier):          #Fonction qui lit le chemin fichier texte fourni par l'utilisateur et en ressort un mot aléatoire
    print(f"Tentative d'ouverture du fichier: {fichier}")   #Pour vérifier le chemin de recherche
    try:                                            #Effectue le code suivant
        f = open(fichier, 'r', encoding='utf-8')    #Ouvre le fichier texte selon l'encodage de caractère utf8
        mots = f.readlines()                        #lit les lignes de ce fichier
        return random.choice(mots).strip()          #Prend une ligne aléatoire (un mot), supprime le saut de ligne avec .strip
    except FileNotFoundError:                       #S'éxécute si une erreur est trouvée lors du 'try'
        print("Le fichier spécifié n'a pas été trouvé. Utilisation du fichier par défaut.")
        return choisir_mot()    #Retourne un mot issu de la liste par défaut

#Fonction donnée par la prof
def enlever_caracteres_speciaux(mot):      #Fonction qui remplace les caractères spéciaux
    import unicodedata
    # Solution obtenue sur https://www.geeksforgeeks.org/how-to-remove-string-accents-using-python-3/
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word if not unicodedata.combining(char)])

#fonction qui vérifie si les lettres données sont correctes
def verifier_lettre(lettre, mot_aleatoire, liste_lettre, nb_chances):
    if lettre in mot_aleatoire:                         #si la lettre est dans le mot
        print("\nLa lettre est bien dans le mot.")      #On l'indique
        liste_lettre += lettre            #On incrémente la liste des lettres
    else:
        print("\nLa lettre n'est pas dans le mot.")     #On indique que c'est faux
        nb_chances -= 1                                 #On perd une vie
        print(f"Il vous reste {nb_chances} chances")    #On indique le nombre de vie restantes
    return liste_lettre, nb_chances                     #Rend la liste de lettre et le nombre de chances

def maj_du_mot(mot_aleatoire, liste_lettre):        #On met à jour le mot qui s'affiche au joueur
    mot_cache = ""
    for lettre_soluce in mot_aleatoire:             #On parcourt les lettres du mot à trouver
        if lettre_soluce in liste_lettre:           #Si une lettre fait partie des lettres trouvées
            mot_cache += lettre_soluce              #On incrémente le mot caché avec la lettre qui s'affichera
        else:
            mot_cache += "_"                        #Si les lettres ne correspondent pas on garde l'underscore _
    return mot_cache                                #rend le mot caché avec les lettres trouvées

#Fonction principale du jeu du pendu
def jouer_au_pendu(fichier):
    #Initialisation du jeu
    if fichier == 0:                                            #Si le joueur n'a pas de fichier de mot
        mot = choisir_mot()                                     #Mot aléatoire pris dans la liste existante
        mot_aleatoire = enlever_caracteres_speciaux(mot)        #On enlève les caractères spéciaux
    elif fichier == 1:                                            #Si le joueur à un fichier de mot .txt
        fichier_mots = input("Veuillez entrer le chemin de votre fichier de mots (sans guillemets !): ")   #Garde le chemin du fichier
        mot_aleatoire = choisir_mot_fichier(fichier_mots)
    else:                   #Si une autre valeur est rentrée on utilisera dans tous les cas le fichier défaut
        mot = choisir_mot()
        mot_aleatoire = enlever_caracteres_speciaux(mot)

    nb_chances = 6                                          #On fixe un nombre de chances
    liste_lettre = ""                                       #Chaine vide des lettres qui seront trouvées
    affichage_mot = cache_mot(mot_aleatoire)                #On cache le mot en fonction du mot aléatoire
    indice_donne = False                                    #Variable bonus pour ne donner l'indice qu'une fois

    #Le jeu commence et se termine lorsque le nb de chances est épuisé
    while nb_chances > 0:
        print("\nLe mot à deviner est:", affichage_mot)             #On affiche le mot mais caché
        lettre = input("Rentrez une lettre de votre choix: ")       #On demande au joueur de rentrer une lettre

        #On vérifie si la lettre fait partie du mot avec la fonction
        liste_lettre, nb_chances = verifier_lettre(lettre, mot_aleatoire, liste_lettre, nb_chances)

        #On affiche le mot avec les lettres trouvées à l'aide de la fonction
        affichage_mot = maj_du_mot(mot_aleatoire, liste_lettre)

        #On lance la fonction pour donner un indice (elle vérifie qu'il reste bien une chance)
        indice_donne = donne_une_chance(nb_chances, mot_aleatoire, liste_lettre, indice_donne)

        if nb_chances == 0:                                     #Si le nb de vie est épuisé
            print("\nOh non, vous avez perdu...")               #on l'indique
            print("le mot à trouver était: ", mot_aleatoire)    #on donne le mot à trouver

        elif affichage_mot == mot_aleatoire:                #Si le mot en entier est trouvé
            print(f"\nVous avez bien trouvé le mot: '{affichage_mot}', félicitation !\n")   #C'est gagné
            nb_chances = 0              #On fixe le nombre de vie à  pour sortir de la boucle

def donne_une_chance(nb_chances, mot_aleatoire, liste_lettre, indice_donne):    #Fonction qui donne une lettre aléatoirement en indice
    if nb_chances == 1 and indice_donne == False:       # Si jamais il reste une chance au joueur et que l'indice n'a pas encore été donnée
        liste_lettres_restantes = ""                    #On créé une liste vide qui prendra les lettres non trouvées restantes
        for lettre_non_trouve in mot_aleatoire:         #On parcourt les lettre du mot à trouver
            if lettre_non_trouve not in liste_lettre:   #Si la lettre du mot ne fait pas partie de celle déjà trouvée
                liste_lettres_restantes += lettre_non_trouve    #On l'ajoute au la liste de lettres restantes à trouver
        indice = random.choice(liste_lettres_restantes)         #On choisi au hasard une lettre parmi celles restantes
        print("\nVoici un INDICE:", indice)                        #On affiche la lettre en indice
        indice_donne = True         #On change la valeur de l'indice donnée pour True pour ne plus rentrer dans la boucle
    return indice_donne             #On renvoie la valeur de indice_donne True ou False

"""------------Fin des Fonctions------------"""

#-----------  BOUCLE PRINCIPALE  ----------------'''

if __name__ == "__main__":

    print("----Bienvenue sur le jeu du Pendu----")

    choix = 1                   #le lancement du jeu dépend du choix du joueur qui au début est 1 pour rentrer dans la boucle
    while choix == 1:           #Tant que le choix est 1, le jeu se lance
        fichier = int(input("\nAvez-vous votre propre fichier de mot? Oui = 1, Non = 0 : "))
        jouer_au_pendu(fichier)        #Fonction qui lance le jeu du pendu, prend en paramètre si le joueur a un fichier ou non
        choix = int(input("\nVouler vous rejouer? Si Oui tapez 1 sinon tapez 0: "))   #Le joueur peut décider de rejouer ou non
        if choix == 0:          #Si le choix est 0, le jeu est terminé on sort de la boucle
            print("\nMerci d'avoir joué, au revoir!")

    print("\n----Fermeture du jeu----\n")