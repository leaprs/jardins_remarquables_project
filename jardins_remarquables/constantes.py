from warnings import warn

# Attribution d'une valeur constante pour la pagination
JARDINS_PAR_PAGE = 22

# Attribution de la clé secrète
SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)