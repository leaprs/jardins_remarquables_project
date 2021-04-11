from flask import render_template, request

from ..app import app
from ..constantes import JARDINS_PAR_PAGE
from ..modeles.donnees import Jardins_remarquables


@app.route("/")
def accueil():
    """ Route permettant l'affichage de la page d'accueil

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    tous_jardins = Jardins_remarquables.query.all()
    derniers_jardins = Jardins_remarquables.query.order_by(Jardins_remarquables.id.desc()).limit(10).all()
    return render_template("pages/accueil.html", nom="Jardins", tous_jardins=tous_jardins, derniers_jardins=derniers_jardins)


@app.route("/description_projet")
def description_projet():
    """ Route permettant l'affichage de la page "À propos" apportant des informations
    sur la nature du projet

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    return render_template("pages/description_projet.html")


@app.route("/jardin/<int:id>")
def jardin(id):
    """ Route permettant l'affichage de la page "À propos" donnant des informations sur la nature du projet

    :param id: Identifiant du jardin remarquable
    :type id: int
    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    unique_jardin = Jardins_remarquables.query.get(id)
    return render_template("pages/jardin.html", nom="Jardins", jardin=unique_jardin)


@app.route("/index")
def index():
    """ Route permettant l'affichage d'un index des noms des jardins remarquables classés par ordre alphabétique

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1
    liste_jardins = Jardins_remarquables.query.order_by(Jardins_remarquables.nom.asc()).paginate(page=page, per_page=JARDINS_PAR_PAGE)
    return render_template("pages/index.html", nom="Jardins", liste_jardins=liste_jardins)


@app.route("/carte")
def carte():
    """ Route permettant l'affichage d'une carte générale au projet avec toutes les localisations des jardins exposées

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    tous_jardins = Jardins_remarquables.query.all()
    return render_template("pages/carte.html", nom="Jardins", tous_jardins=tous_jardins)


@app.route("/recherche")
def recherche():
    """ Route permettant la recherche des jardins remarquables dans la base de données via leur nom

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """
    motclef = request.args.get("keyword", None)
    resultats = []
    titre = "Recherche"
    if motclef:
        resultats = Jardins_remarquables.query.filter(
            Jardins_remarquables.nom.like("%{}%".format(motclef))
        ).all()
        titre = "Résultat pour la recherche `" + motclef + "`"
    return render_template("pages/recherche.html", resultats=resultats, titre=titre)