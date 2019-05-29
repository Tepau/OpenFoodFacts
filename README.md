# Utilisez les données publiques de l'OpenFoodFacts

## Installer Python 3.7.3 en suivant le lien suivant
https://www.python.org/downloads/ 

### Cloner ou télécharge le projet

## Base de données utilisée : MySQL
https://dev.mysql.com/downloads/installer/ 

Créer la base de donnée à l'aide du fichier tables.sql

## Virtualenv en exécutant la commande suivante
    pip install virtualenv

## Se déplacer dans le dossier contenant le projet et créer un environnement virtuel grâce à la commande suivante :
    python -m venv env

## Se déplacer le fichier scripts en effectuant la commande suivante
    cd env 
    cd scripts

## Activer l'environnement virtuel
    activate.bat
    
Revenir dans le dossier contenant le projet

## Installer les dépendances nécessaires :
    pip install -r requirements.txt

## Pour récupérer les produits grâce à l'API openfoodfacts :
    python service.py

## Pour remplir la base de données grâce aux produits récupérés :
    python feed_db.py

## Puis lancer le programme
    python main.py
    
    
   

## Fonctionnalités:

### S'identifier
    -Indiquez votre pseudo pour vous identifier
    
#### 1 - Quel aliment souhaitez-vous remplacer ? 

### Cinq categories:
    -Choisir parmis les cinq catégories celle dont vous voulez voir les produits disponible.

### Sélectionnez l'aliment:
    -Le programme vous propose une sélection de produit correspondant à la catégorie sélectionnée, tous les produits ont une mauvaise note nutritionnelle (e)

### Voir aliment de meilleur qualité
    -Le programme vous affiche un produit de la même catégorie mais dont la note nutritionelle est excellente (a)
    -Vous avez la possibilité de sauvegarder votre recherche

#### 2 - Retrouver mes aliments substitués.
    -Revenu au menu principal, vous pouvez accéder aux recherches que vous avez sauvegardées  
