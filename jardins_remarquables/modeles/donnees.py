from flask_login import current_user
import datetime

from .. app import db
from .utilisateurs import Utilisateur


# Définition de la classe Participation
class Participation(db.Model):
    __tablename__ = "participation"
    participation_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    participation_jardin_id = db.Column(db.Integer, db.ForeignKey('jardins_remarquables.id'))
    participation_utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateur_id'))
    participation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # Ajout de la jointure avec les classes Utilisateur et Jardins_remarquables
    utilisateur = db.relationship("Utilisateur", back_populates="participations")
    jardin = db.relationship("Jardins_remarquables", back_populates="participations")


# Définition de la classe Jardin_remarquable
class Jardins_remarquables(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    code_id = db.Column(db.Text, unique=True, nullable=False)
    nom = db.Column(db.Text, nullable=False)
    descriptif = db.Column(db.Text)
    annee_labellisation = db.Column(db.Integer, nullable=False)
    adresse = db.Column(db.Text)
    code_postal = db.Column(db.Integer)
    ville = db.Column(db.Text)
    departement = db.Column(db.Text)
    region = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    site_web = db.Column(db.Text)
    facebook = db.Column(db.Text)
    twitter = db.Column(db.Text)
    instagram = db.Column(db.Text)
    dailymotion = db.Column(db.Text)
    tags = db.Column(db.Text)
    # Ajout jointure avec la classe Participation
    participations = db.relationship("Participation", back_populates="jardin")


    @staticmethod
    def creation(nom, code_id, annee_labellisation, code_postal, adresse, ville,
                 descriptif, departement, region, latitude, longitude, site_web="",
                 facebook="", instagram="", twitter="", dailymotion="", tags=""):
        """ Fonction pour la création d'un jardin remarquable
        Pour certains paramètres non-obligatoires, notamment les réséaux sociaux et les mots clés,
        un valeur par défaut vide a été définie afin de ne pas bloquer l'ajout des données si ces valeurs faisaient défaut.

        :param nom: Nom du jardin remarquable
        :type nom: str
        :param code_id: Identifiant Mérimée du jardin remarquable
        :type code_id: str
        :param annee_labellisation: Année de labellisation du jardin remarquable
        :type annee_labellisation: int
        :param code_postal: Code postal du jardin remarquable
        :type code_postal: int
        :param adresse: Adresse du jardin remarquable
        :type adresse: str
        :param ville: Ville du jardin remarquable
        :type ville: str
        :param descriptif: Descriptif du jardin remarquable
        :type descriptif: str
        :param departement: Département du jardin remarquable
        :type departement: str
        :param region: Région du jardin remarquable
        :type region: str
        :param latitude: Latitude du jardin remarquable
        :type latitude: float
        :param longitude: Longitude du jardin remarquable
        :type longitude: float
        :param site_web: Site web du jardin remarquable
        :type site_web: str
        :param facebook: Facebook du jardin remarquable
        :type facebook: str
        :param instagram: Instagram du jardin remarquable
        :type instagram: str
        :param twitter: Twitter du jardin remarquable
        :type twitter: str
        :param dailymotion: Dailymotion du jardin remarquable
        :type dailymotion: str
        :param tags: Tags du jardin remarquable
        :type tags: str
        :returns: Si succès, True et envoie des données ; si échec, False et liste d'erreurs
        :rtype: bool
        """

        # Définition d'une liste vide où viendront s'ajouter les potentielles erreurs
        erreurs = []

        # Récupération de l'identifiant du dernier enregistrement
        # Si la base est vide, l'identifiant sera par défaut 0
        if Jardins_remarquables.query.filter(Jardins_remarquables.id).count() == 0:
            dernier_id = 0
        else:
            dernier_id = Jardins_remarquables.query.order_by(Jardins_remarquables.id.desc()).first().id

        # Récupération de l'identifiant de l'utilisateur à l'origine de l'ajout
        utilisateur = Utilisateur.query.get(current_user.utilisateur_id)

        # Critères pour l'insertion
        if not nom or nom.islower():
            erreurs.append("Le champ nom ne doit ni être vide, ni commencer par une minuscule.")
        if not annee_labellisation or int(annee_labellisation) < 2004:
            erreurs.append("Le champ de l'année de labellisation est vide ou  la date est antérieure à 2004.")
        if not code_id:
            erreurs.append("Le jardin remarquable doit obligatoirement avoir un identifiant Mérimée.")
        if not code_postal or len(code_postal) > 5:
            erreurs.append("Le champ code postal ne doit être ni vide, ni mal renseigné.")
        if not adresse:
            erreurs.append("L'adresse n'est pas renseignée.")
        if not descriptif:
            erreurs.append("Le champ descriptif ne peut être laissé vide.")
        if not ville:
            erreurs.append("Le champ ville ne peut être vide.")
        if not departement:
            erreurs.append("Le champ département ne peut être vide.")
        if not region:
            erreurs.append("Le champ région ne peut être vide.")
        if not latitude:
            erreurs.append("La latitude doit être renseignée.")
        if not longitude:
            erreurs.append("La longitude doit être renseignée.")

        # Vérification que le nom et l'identifiant Mérimée fournis pour le nouveau jardin ne soient pas déjà inscrits dans la base de données
        unique = Jardins_remarquables.query.filter(
            db.or_(Jardins_remarquables.nom == nom, Jardins_remarquables.code_id == code_id)
        ).count()
        if unique > 0:
            erreurs.append("Le nom ou l'identifiant Mérimée de ce jardin sont déjà inscrits dans la base de données.")

        # S'il existe au moins une erreur, on renvoie de la liste d'erreurs
        if len(erreurs) > 0:
            return False, erreurs

        # Si pas d'erreurs, ajout des données du nouveau jardin
        if not erreurs:
            nouveau_jardin = Jardins_remarquables(
                id=dernier_id + 1,
                code_id=code_id,
                nom=nom,
                descriptif=descriptif,
                annee_labellisation=annee_labellisation,
                adresse=adresse,
                code_postal=code_postal,
                ville=ville,
                departement=departement,
                region=region,
                latitude=latitude,
                longitude=longitude,
                site_web=site_web,
                facebook=facebook,
                twitter=twitter,
                instagram=instagram,
                dailymotion=dailymotion,
                tags=tags
            )

        try:
            # Stockage de l'ajout du nouveau jardin vers la base de données
            db.session.add(nouveau_jardin)
            # Enregistrement de l'ajout dans la base de données
            db.session.commit()

            # Récupération de l'identifiant du nouveau jardin ainsi créé
            jardin = Jardins_remarquables.query.order_by(Jardins_remarquables.id.desc()).limit(1).first()


            # Ajout dans la table Participation de l'identifiant de l'utilisateur créateur et de l'identifiant du nouveau jardin
            a_participe = Participation(utilisateur=utilisateur, jardin=jardin)
            # Stockage de l'ajout vers la base de données
            db.session.add(a_participe)
            # Enregistrement de l'ajout dans la base de données
            db.session.commit()

            # On renvoie le nouveau jardin
            return True, nouveau_jardin

        except Exception as erreur:
            # On renvoie la liste d'erreurs
            return False, [str(erreur)]


    @staticmethod
    def edition(id, nom, code_id, annee_labellisation, code_postal, adresse, ville,
                descriptif, departement, region, latitude, longitude, site_web,
                facebook, instagram, twitter, dailymotion, tags):
        """ Fonction permettant de modifier les données enregistrées d'un jardin remarquable dans la base de données

        :param id: Id du jardin remarquable
        :type id: int
        :param nom: Nom du jardin remarquable
        :type nom: str
        :param code_id: Identifiant Mérimée du jardin remarquable
        :type code_id: str
        :param annee_labellisation: Année de labellisation du jardin remarquable
        :param annee_labellisation: int
        :param code_postal: Code postal du jardin remarquable
        :param code_postal: int
        :param adresse: Adresse du jardin remarquable
        :type adresse: str
        :param ville: Ville du jardin remarquable
        :type ville: str
        :param descriptif: Descriptif du jardin remarquable
        :type descriptif: str
        :param departement: Département du jardin remarquable
        :type departement: str
        :param region: Région du jardin remarquable
        :type region: str
        :param latitude: Latitude du jardin remarquable
        :type latitude: float
        :param longitude: Longitude du jardin remarquable
        :type longitude: float
        :param site_web: Site web du jardin remarquable
        :type site_web: str
        :param facebook: Facebook du jardin remarquable
        :type facebook: str
        :param instagram: Instagram du jardin remarquable
        :type instagram: str
        :param twitter: Twitter du jardin remarquable
        :type twitter: str
        :param dailymotion: Dailymotion du jardin remarquable
        :type dailymotion: str
        :param tags: Tags du jardin remarquable
        :type tags: str
        :returns: Si succès, True et envoie des données ; si échec, False et liste d'erreurs
        :rtype: bool
        """

        # Définition d'une liste vide où viendront s'ajouter les potentielles erreurs
        erreurs = []

        # Récupération de l'identifiant du jardin remarquable à modifier
        jardin_modification = Jardins_remarquables.query.get(id)

        # Récupération de l'identifiant de l'utilisateur à l'origine des modifications
        utilisateur = Utilisateur.query.get(current_user.utilisateur_id)

        # Critères pour l'insertion
        if not nom or nom.islower():
            erreurs.append("Le champ nom ne doit ni être vide, ni commencer par une minuscule.")
        if not annee_labellisation or int(annee_labellisation) < 2004:
            erreurs.append("Le champ de l'année de labellisation est vide ou  la date est antérieure à 2004.")
        if not code_id:
            erreurs.append("Le jardin remarquable doit obligatoirement avoir un identifiant Mérimée.")
        if not code_postal or len(code_postal) > 5:
            erreurs.append("Le champ code postal ne doit être ni vide, ni mal renseigné.")
        if not adresse:
            erreurs.append("L'adresse n'est pas renseignée.")
        if not descriptif:
            erreurs.append("Le champ descriptif ne peut être laissé vide.")
        if not ville:
            erreurs.append("Le champ ville ne peut être vide.")
        if not departement:
            erreurs.append("Le champ département ne peut être vide.")
        if not region:
            erreurs.append("Le champ région ne peut être vide.")
        if not latitude:
            erreurs.append("La latitude doit être renseignée.")
        if not longitude:
            erreurs.append("La longitude doit être renseignée.")

        # S'il existe au moins une erreur, on renvoie de la liste d'erreurs
        if len(erreurs) > 0:
            return False, erreurs

        # Sinon, mise à jour des données de l'enregistrement du jardin remarquable identifié
        else:
            jardin_modification.code_id = code_id
            jardin_modification.nom = nom
            jardin_modification.annee_labellisation = annee_labellisation
            jardin_modification.descriptif = descriptif
            jardin_modification.adresse = adresse
            jardin_modification.code_postal = code_postal
            jardin_modification.ville = ville
            jardin_modification.departement = departement
            jardin_modification.region = region
            jardin_modification.latitude = latitude
            jardin_modification.longitude = longitude
            jardin_modification.site_web = site_web
            jardin_modification.facebook = facebook
            jardin_modification.twitter = twitter
            jardin_modification.instagram = instagram
            jardin_modification.dailymotion = dailymotion
            jardin_modification.tags = tags

        try:
            # Stockage de l'ajout des modifications vers la base de données
            db.session.add(jardin_modification)
            # Enregistrement de la modification dans la base de données
            db.session.commit()

            # Ajout dans la table Participation de l'identifiant de l'utilisateur modificateur et de l'identifiant du jardin modifié
            a_participe = Participation(utilisateur=utilisateur, jardin=jardin_modification)
            # Stockage de l'ajout vers la base de données
            db.session.add(a_participe)
            # Enregistrement de l'ajout dans la base de données
            db.session.commit()

            # On renvoie les modifications
            return True, jardin_modification

        except Exception as erreur:
            # On renvoie la liste d'erreurs
            return False, [str(erreur)]


    @staticmethod
    def suppression(id):
        """ Fonction permettant de supprimer un jardin remarquable de la base de données

        :param id: Identifiant du jardin remarquable à supprimer
        :type id: int
        :returns: Si succès, True et suppression du jardin ; si échec, False et liste d'erreurs
        :rtype: Bool
        """

        # Récupération du l'identifiant du jardin remarquable à supprimer
        supprimer_jardin = Jardins_remarquables.query.get(id)

        # Récupération des enregistrements dans la table Participation
        # où l'identifiant du jardin à supprimer est le même que celui sur lequel a lieu la modification/création
        enregistrements = Participation.query.filter(Participation.participation_jardin_id == id).all()

        try:
            # Suppression de chaque enregistrement
            for ligne in enregistrements:
                # Stockage de la suppression vers la base de données
                db.session.delete(ligne)
                # Enregistrement de la suppression dans la base de données
                db.session.commit()

            # Stockage de la suppression du jardin remarquable vers la base de données
            db.session.delete(supprimer_jardin)
            # Enregistrement de la suppression dans la base de données
            db.session.commit()
            return True

        except Exception as erreur:
            # On renvoie la liste d'erreurs
            return False, [str(erreur)]


# Création des tables dans la base de données
db.create_all()
