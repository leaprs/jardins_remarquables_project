# Import des modules et packages nécessaires
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Import local
from .constantes import SECRET_KEY


# Définition des chemins grâce au package os
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# Création de l'application Flask
app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)

# Configuration de la base de données jardins.db dans l'application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jardins.db'

# Initiation de l'extension SQLALchemy
# L'application est stockée dans la variable db
db = SQLAlchemy(app)

# Désactivation du suivi des modifications par SQLALchemy (car provoque des baisses de performance)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration de la clé secrète
app.config['SECRET_KEY'] = SECRET_KEY

# Ajout de la gestion des utilisateurs
login = LoginManager(app)

# Import des routes dans l'application
from .routes import general, utilisateur, manipulations_crud
