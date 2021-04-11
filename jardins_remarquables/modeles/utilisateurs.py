from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ..app import db, login

# Définition de la classe Utilisateur
class Utilisateur(UserMixin, db.Model):
    utilisateur_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    utilisateur_nom = db.Column(db.Text, nullable=False)
    utilisateur_login = db.Column(db.String(45), nullable=False)
    utilisateur_email = db.Column(db.Text, nullable=False)
    utilisateur_mdp = db.Column(db.String(64), nullable=False)
    # Ajout jointure avec la classe Participation
    participations = db.relationship("Participation", back_populates="utilisateur")

    @staticmethod
    def creer(login, email, nom, motdepasse):
        """ Fonction pour créer un compte utilisateur

        :param login: Login de l'utilisateur
        :type login: str
        :param email: Email de l'utilisateur
        :type email: str
        :param nom: Nom de l'utilisateur
        :type nom: str
        :param motdepasse: Mot de passe de l'utilisateur (minimum 6 caractères)
        :type motdepasse: str
        :returns: Si succès, True et envoie des données ; si échec, False et liste d'erreurs
        :rtype: bool
        """

        # Définition d'une liste vide où viendront s'ajouter les potentielles erreurs
        erreurs = []

        if not login:
            erreurs.append("Le champ réservé au login est vide")
        if not email:
            erreurs.append("Le champ réservé à l'adresse email est vide")
        if not nom:
            erreurs.append("Le champ réservé au nom est vide")
        if not motdepasse or len(motdepasse) < 6:
            erreurs.append("Le champ réservé au mot de passe est vide ou contient moins de six caractères.")

        # Vérification que l'email et le login fournis sont bien uniques dans la base de données
        uniques = Utilisateur.query.filter(
            db.or_(Utilisateur.utilisateur_email == email, Utilisateur.utilisateur_login == login)
        ).count()
        if uniques > 0:
            erreurs.append("L'email ou le login renseignées sont déjà inscrits dans la base de données.")

        # S'il existe au moins une erreur, renvoie de la liste d'erreurs
        if len(erreurs) > 0:
            return False, erreurs

        # Sinon, création d'un nouveau utilisateur
        utilisateur = Utilisateur(
            utilisateur_nom=nom,
            utilisateur_login=login,
            utilisateur_email=email,
            utilisateur_mdp=generate_password_hash(motdepasse)
        )

        try:
            # Stockage de l'ajout du nouvel utilisateur vers la base de données
            db.session.add(utilisateur)
            # Enregistrement de l'ajout dans la base de données
            db.session.commit()

            # On renvoie l'utilisateur
            return True, utilisateur

        except Exception as erreur:
            # On renvoie la liste d'erreurs
            return False, [str(erreur)]

    # Définition de la fonction get_id nécessaire à l'utilisation de l'outil UserMixin
    def get_id(self):
        """ Fonction pour retourner l'identifiant de l'objet utilisé

        :param self: Instance de Utilisateur en cours
        :returns: Identifiant de l'utilisateur
        :rtype: int
        """
        return self.utilisateur_id

    @staticmethod
    def identification(login, motdepasse):
        """ Fonction pour identifier un utilisateur

        :param login: Login de l'utilisateur
        :type login: str
        :param motdepasse: Mot de passe envoyé par l'utilisateur
        :type motdepasse: str
        :returns: Si succès, données de l'utilisateur ; si échec, None
        :rtype: bool
        """
        utilisateur = Utilisateur.query.filter(Utilisateur.utilisateur_login == login).first()
        if utilisateur and check_password_hash(utilisateur.utilisateur_mdp, motdepasse):
            return utilisateur
        return None

@login.user_loader
def trouver_utilisateur_via_id(identifiant):
    """ Fonction pour récupérer un utilisateur en fonction de son identifiant

    :param identifiant: Identifiant de l'utilisateur
    :type identifiant: int
    :returns: Identifiant de l'utilisateur
    :rtype: int
    """
    return Utilisateur.query.get(int(identifiant))


# Création de la table dans la base de données
db.create_all()