# Jeu-du-pendu

Bienvenue sur le jeu du pendu.

Il a été codé par Cyril Traineau dans le cadre du cours de MGA802.

Voici ce que fait ce code:

Il se compose de deux fichiers principaux, un contenant le code et un autre contenant une liste de mot dans un fichier texte.
Téléchargez tous les fichiers au même endroit.

Le code se compose de plusieurs fonctions.
Une sert à lire un mot aléatoirement dans le fichier.
Une fonction pour afficher ce mot mais avec des underscores _.

L'utilisateur peut choisir de spécifier un fichier propre à lui ou de choisir d'utiliser le fichier par défaut.
Dans le cas où il a un fichier déjà existant, il doit spécifier le chemin d'accès sans mettre de guillemets;
Cela appelera la fonction qui lira les mots de son fichier.

Une fonction permet de retirer les caractères spéciaux du mot tiré.

BOUCLE PRINCIPALE:
La boucle principale se met en route lorsque le programme est lancé.
Elle lance au moins une fois la fonction qui permet de jouer au pendu puis à la fin demande à l'utilisateur s'il veut rejouer, en fonction de sa réponse la boucle continue ou s'arrête.

FONCTION PRINCIPALE:
Une des fonctions principale est "jouer_au_pendu". C'est une fonction qui appelle les autres fonctions.
C'est une boucle qui tourne tant que le nombre de vie n'est pas au égal à 0, ce qui signifie que le joueur à perdu,
ou tant que le mot n'a pas été trouvé.

Il est demande à l'utilisateur de rentrer une lettre, si celle-ci fait partie du mot, la lettre s'affiche dans le mot caché.
Si elle ne fait pas partie du mot, le joueur perd une vie.
Lorsque le joueur n'a plus qu'une vie, une indice lui est donné, c'est une lettre parmi celles restantes à trouver.