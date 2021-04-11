from flask import render_template, request, flash, redirect
from flask_login import current_user, login_user, logout_user

from ..app import app, login
from ..modeles.utilisateurs import Utilisateur


@app.route("/register", methods=["GET", "POST"])
def inscription():
    """ Route permettant l'inscriptions des futurs utilisateurs

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    # Si la méthode est POST, le formulaire a été envoyé
    if request.method == "POST":
        statut, infos = Utilisateur.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Vous êtes maintenant inscrit, vous pouvez vous identifier.", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées lors de l'inscription : " + ",".join(infos), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route permettant la connexions aux utilisateurs

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")

    # Si la méthode est POST, le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = Utilisateur.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Vous êtes connecté.", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus. La connexion échoue.", "error")

    return render_template("pages/connexion.html")
login.login_view = 'connexion'


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    """ Route permettant la déconnexions aux utilisateurs

    :returns: Redirection vers la page HTML souhaitée
    :rtype: page HTML
    """

    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté.", "info")
    return redirect("/")