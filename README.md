# À la découverte des jardins remarquables français

## Présentation du projet

Cette application a été développée par Léa Perissier dans le cadre de l'évaluation du module Python de l'École nationale des chartes. Elle permet l'exposition et la géolocalisation des jardins remarquables français d'après un jeu de données disponible sur [data.gouv](https://www.data.gouv.fr/fr/datasets/liste-des-jardins-remarquables/). 
Afin de rendre les données davantage lisibles, de légères modifications ont été apportées à partir du set de données initial. Ces changements sont mesurables à travers le dossier "documentation" au sein duquel se trouvent les jeux de données à la base de l'application.

Crédits : L'application a été développée à l'aide du framework Flask ainsi que de la librairie JavaScript Leaflet pour les visualisations. Quant au design de l'application, le framework Bootstrap a été utilisé pour l'ensemble de l'application.

## Description des fonctionnalités de l'application

Le visiteur pourra parcourir la base de données à l'aide de plusieurs outils :
- des notices descriptives pour chaque jardin comportant ses caractéristiques et sa géolocalisation
- un index alphabétique des noms des jardins remarquables
- une barre de recherche pour faire des requêtes à travers les noms des jardins remarquables
- une carte intéractive d'ensemble où chaque pointeur renvoie à la notice du jardin concerné

En s'inscrivant et en se connectant, le visiteur pourra bénéficier de fonctionnalités supplémentaires à savoir : l'ajout, la modification et la suppression d'un jardin remarquable dans la base de données.

## Installation et lancement de l'application

Veuillez suivre les étapes suivantes à exécuter dans un terminal (Linux) :

1. Vérifier que la version de python installée est bien python3 : ``` python --version ```
2. Clôner le dépôt git sur sa machine : ``` git clone https://github.com/leaprs/jardins_remarquables_project.git ``` 
3. Se déplacer dans le dossier créé : ``` cd jardins_remarquables_project/ ```
4. Créer un environnement virtuel ``` env ``` : ``` virtualenv -p python3 env ```
5. Sourcer l'environnement virtuel créé : ``` source env/bin/activate ```
6. Installer les librairies nécessaires au fonctionnement de l'application : ``` pip install -r requirements.txt ```
7. Lancer l'application : ``` python3 run.py ```
8. Ouvrir l'application dans votre navigateur en cliquant sur l'URL qui s'affiche : http://127.0.0.1:5000/

Seules les étapes 3, 5, 7 et 8 seront à refaire une fois passée la première installation.
