# Présentation du projet

Cette application Flask a été développée par Léa Perissier dans le cadre de l'évaluation du cours python de M. Clérice à l'École nationale des chartes. Elle permet l'exposition et la représentation géographique des jardins remarquables français d'après un jeu de données disponible sur data.gouv.

# Description de l'application

Le visiteur pourra parcourir la base de données à l'aide de plusieurs outils :
- des notices descriptives pour chaque jarin comportant une représentation géographique grâce à la librairie JavaScript Leaflet
- un index alphabétique des jardins remarquables
- une barre de recherche
- une carte intéractive mondiale où chaque pointeur renvoie à la notice du jardin concerné

En s'inscrivant et en se connectant, le visiteur pourra bénéficier de fonctionnalités supplémentaires à savoir, l'ajout, la modification et la suppression d'une jardin remarquable dans la base de données.

# Installation et lancement de l'application

Veuillez suivre les étapes suivantes à exécuter dans un terminal (Linux) :

- Vérifier que la version de python installée est bien python3 : ``` python --version ```
- Clôner le dépôt git sur sa machine : git clone 
- Créer un environnement virtuel ``` env ``` : ``` virtualenv -p python3 env ```
- Sourcer l'environnement virtuel créé : ``` source env/bin/activate ```
- Se déplacer dans l'environnement virtuel : ``` cd env ```
- Installer les librairies nécessaires au fonctionnement de l'application : ``` pip install -r requirements.txt ```
- Lancer l'application : ``` python3 run.py ```
