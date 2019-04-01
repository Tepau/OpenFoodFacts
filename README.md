OpenFoodFacts Projet n°5
========================

Description
-----------
Programme qui interagit avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

Description du parcours utilisateur
-----------------------------------

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ? 

2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1.

Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]

Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

Fonctionnalités
---------------

Recherche d'aliments dans la base Open Food Facts.

L'utilisateur interagit avec le programme dans le terminal.

Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question.

La recherche doit s'effectuer sur une base MySql.

En tant qu'utilisateur, je veux sélectionner un aliment pour accéder à son substitut.
En tant qu’utilisateur, je veux sélectionner une catégorie de produits, pour accéder à la liste des produits.
En tant qu'utilisateur, je veux enregistrer une recherche, pour y accéder plus tard.
En tant qu'utilisateur, je veux me créer un compte pour pouvoir enregistrer des données.
En tant qu'utilisateur, je veux me connecter, pour accéder à mon compte.
En tant qu'utilisateur, je veux accéder à mes recherches enregistrées, pour 
En tant qu'administrateur, je veux ajouter des aliments à la base données, pour offrir plus de choix aux utilisateurs.
