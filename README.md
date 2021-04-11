# À la découverte des jardins remarquables français

## Présentation du projet

Cette application Flask a été développée par Léa Perissier dans le cadre de l'évaluation du module python de M. Clérice à l'École nationale des chartes. Elle permet l'exposition et la représentation géographique des jardins remarquables français d'après un jeu de données disponible sur [data.gouv](https://www.data.gouv.fr/fr/datasets/liste-des-jardins-remarquables/). Afin de rendre les données davantage lisible, de légères modifications ont eu lieu à partir du set de données intial. Ces changements sont mesurables via le dossier "documentation" au sein duquel se trouvent les jeux de données à la base de l'application.

## Description de l'application

Le visiteur pourra parcourir la base de données à l'aide de plusieurs outils :
- des notices descriptives pour chaque jarin comportant une représentation géographique grâce à la librairie JavaScript Leaflet
- un index alphabétique des jardins remarquables
- une barre de recherche
- une carte intéractive mondiale où chaque pointeur renvoie à la notice du jardin concerné

En s'inscrivant et en se connectant, le visiteur pourra bénéficier de fonctionnalités supplémentaires à savoir : l'ajout, la modification et la suppression d'un jardin remarquable dans la base de données.

## Installation et lancement de l'application

Veuillez suivre les étapes suivantes à exécuter dans un terminal (Linux) :

1. Vérifier que la version de python installée est bien python3 : ``` python --version ```
2. Clôner le dépôt git sur sa machine : ``` git clone https://github.com/leaprs/jardins_remarquables.git ``` 
3. Créer un environnement virtuel ``` env ``` : ``` virtualenv -p python3 env ```
4. Sourcer l'environnement virtuel créé : ``` source env/bin/activate ```
5. Se déplacer dans l'environnement virtuel : ``` cd env ```
6. Installer les librairies nécessaires au fonctionnement de l'application : ``` pip install -r requirements.txt ```
7. Lancer l'application : ``` python3 run.py ```

Seules les étapes 4, 5 et 7 seront à refaire une fois passée la première installation.
