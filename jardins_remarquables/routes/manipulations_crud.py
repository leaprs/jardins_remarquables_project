from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from ..app import app, db
from ..modeles.donnees import Jardins_remarquables


@app.route("/ajouter_jardin", methods=["POST", "GET"])
@login_required
def ajouter_jardin():
    """ Route permettant l'ajout d'un jardin remarquable dans la base de données

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    # Si la méthode est POST, le formulaire est envoyé
    if request.method == "POST":
        # Application de la méthode creation de la classe Jardins_remarquables
        entrees, infos = Jardins_remarquables.creation(
            nom=request.form.get("nom", None),
            code_id=request.form.get("code_id", None),
            annee_labellisation=request.form.get("annee_labellisation", None),
            adresse=request.form.get("adresse", None),
            ville=request.form.get("ville", None),
            code_postal=request.form.get("code_postal", None),
            departement=request.form.get("departement", None),
            region=request.form.get("region", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            descriptif=request.form.get("descriptif", None),
            site_web=request.form.get("site_web", None),
            facebook=request.form.get("facebook", None),
            instagram=request.form.get("instagram", None),
            twitter=request.form.get("twitter", None),
            dailymotion=request.form.get("dailymotion", None),
            tags=request.form.get("tags", None)
        )
        if entrees is True:
            flash("L'ajout d'un nouveau jardin a été enregistré.", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées lors de la création : " + ",".join(infos), "danger")
            return render_template("pages/ajouter_jardin.html")
    else:
        return render_template("pages/ajouter_jardin.html")


@app.route("/jardin/<int:id>/editer_jardin", methods=["POST", "GET"])
@login_required
def editer_jardin(id):
    """ Route permettant de modifier les données d'un jardin remarquable existant dans la base de données

    :param id : identifiant du jardin remarquable dont les données sont à modifier
    :type id: int
    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    # Récupération de l'identifiant du jardin remarquable à modifier
    jardin_modification = Jardins_remarquables.query.get(id)

    # Si la méthode est POST, le formulaire est envoyé
    if request.method == "POST":
        # Application de la méthode edition de la classe Jardins_remarquables
        modification, infos = Jardins_remarquables.edition(
            id=id,
            nom=request.form.get("nom", None),
            code_id=request.form.get("code_id", None),
            annee_labellisation=request.form.get("annee_labellisation", None),
            adresse=request.form.get("adresse", None),
            ville=request.form.get("ville", None),
            code_postal=request.form.get("code_postal", None),
            departement=request.form.get("departement", None),
            region=request.form.get("region", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            descriptif=request.form.get("descriptif", None),
            site_web=request.form.get("site_web", None),
            facebook=request.form.get("facebook", None),
            instagram=request.form.get("instagram", None),
            twitter=request.form.get("twitter", None),
            dailymotion=request.form.get("dailymotion", None),
            tags=request.form.get("tags", None)
        )

        if modification is True:
            flash("Les modifications du jardin remarquable sont enregistrées.", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées lors de la modification : " + ",".join(infos), "danger")
            return render_template("pages/editer_jardin.html")
    else:
        return render_template("pages/editer_jardin.html", jardin_modification=jardin_modification)


@app.route("/jardin/<int:id>/supprimer_jardin", methods=["POST", "GET"])
@login_required
def supprimer_jardin(id):
    """ Route permettant de supprimer un jardin remarquable de la base de données

    :param id : Identifiant du jardin remarquable à supprimer
    :type id: int
    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    # Récupération de l'identifiant du jardin remarquable à supprimer
    jardin_supprime = Jardins_remarquables.query.get(id)

    # Si la méthode est POST, le formulaire est envoyé
    if request.method == "POST":
        # Application de la méthode suppression de la classe Jardins_remarquables
        statut = Jardins_remarquables.suppression(id=id)

        if statut is True:
            flash("Suppression réussie", "success")
            return redirect("/")
        else:
            flash("La suppression a échoué.", "error")
            return redirect("/")
    else:
        return render_template("pages/supprimer_jardin.html", jardin_supprime=jardin_supprime)