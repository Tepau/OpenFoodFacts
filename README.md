OpenFoodFacts Projet n°5
========================
# Utilisez les données publiques de l'OpenFoodFacts

##Installer Python 3.7.3 en suivant le lien suivant
https://www.python.org/downloads/ 

##Cloner ou télécharge le projet

##Base de données utilisée : MySQL
https://dev.mysql.com/downloads/installer/ 

##Créer la base de donnée à l'aide du fichier tables.sql

##Dans l'invite de commande installer Virtualenv en exécutant la commande suivante
pip install virtualenv

##Dans l'invite de commande, se déplacer dans le dossier contenant le projet et créer un environnement virtuel grâce à la commande suivante :
python -m venv env

##Dans l'invite de commande se déplacer le fichier scripts en effectuant la commande suivante
cd env 
cd scripts

##Activer l'environnement virtuel
activate.bat

##Revenir dans le dossier contenant le projet

##Installer les dépendances nécessaires :
pip install -r requirements.txt

##Pour récupérer les produits grâce à l'API openfoodfacts :
python service.py

##Pour remplir la base de données grâce aux produits récupérés :
python feed_db.py

##Puis lancer le programme
python main.py


