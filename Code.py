#%%
import numpy as np
import pandas as pd
#%%
df=pd.read_csv("Apprentissage.csv")
dp=pd.read_csv("apprentissage.csv")
# %%
df = df.drop(df.columns[[0,7,15,18,20,21,25,28,29,30]], axis=1)
# %%
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
print(df)
#%%

# Suppression de "ans" ou "Ans" dans la première colonne
df.iloc[:, 1] = df.iloc[:, 1].str.replace(r'\s*[aA]ns', '', regex=True)

# Affichage du DataFrame mis à jour
print(df)
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%
#print(df.iloc[:, 1])
print(df[["Age"]])
#pour supprimer des colonnes 
#df = df.drop(df.columns[[0,27, 28,29]], axis=1)
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
print(df)
# %%
rows, cols = dp.shape
print(f"Nombre de lignes : {rows}")
print(f"Nombre de colonnes : {cols}")
#print(df.iloc[:, 4])
# %%

# Fonction de conversion
def convertir_en_minutes(val):
    val = str(val).lower().strip()  # Mettre en minuscule et supprimer les espaces
    if "h" in val or "heure" in val:  # Détecter les heures
        return int("".join(filter(str.isdigit, val))) * 60  # Extraire le chiffre et convertir en minutes
    elif "min" in val:  # Détecter les minutes
        return int("".join(filter(str.isdigit, val)))  # Extraire juste le chiffre
    elif val.isdigit():  # Si c'est un chiffre seul (supposé être des heures)
        return int(val) * 60
    else:
        return np.nan  # Gérer "ça dépend" ou autres valeurs invalides

# Appliquer la conversion
df["Temps (min)"] = df["Temps d'apprentissage"].apply(convertir_en_minutes)

# Afficher le DataFrame nettoyé
print(df)

# %%
# Supprimer les mots 'heure', 'heures', 'Heure', 'Heures'
df["Temps d'apprentissage"] = df["Temps d'apprentissage"].replace({
    'heure': '',
    'h': '',
    'H': '',
    'HEURE': '',
    'EURE': '',
    'HEURES': '',
    'heures': '', 
    'Heure': '', 
    'Heures': ''
}, regex=True)

# Afficher le DataFrame modifié
print(df)
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%
# Extraire la colonne comme une liste
colonne_extraite_liste = df["Temps d'apprentissage"].tolist()

# Afficher la liste
print(colonne_extraite_liste)

# %%
def rename_columns(df: pd.DataFrame, rename_dict: dict) -> pd.DataFrame:
    """
    Renomme les colonnes d'un DataFrame selon un dictionnaire de correspondance.
    
    :param df: DataFrame pandas
    :param rename_dict: Dictionnaire contenant les anciens noms comme clés et les nouveaux noms comme valeurs
    :return: DataFrame avec les colonnes renommées
    """
    return df.rename(columns=rename_dict)
#%%
dp=pd.read_csv("apprentissage.csv")
print("Avant renommage:\n", dp)
# Dictionnaire de renommage
rename_dict = {
    "Age": "Age",
    "Etablissement": "Etablissement",
    "Classe": "Classe",
    "Commune de domicile": "Commune",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage des mathématiques?": "Heures_Maths",
    "Quel est votre rapport aux mathématiques ? Sur une échelle de 1 à 10 (du très mauvais à un excellent rapport), à combien auto-évaluez-vous ?": "Auto_eval_Maths",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage des autres sciences?": "Heures_Sciences",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage de la langue française?": "Heures_Francais",
    "Sur une échelle de 1 à 10, donnez votre dernière moyenne de trimestre (note sur 10) en mathématiques?": "Moyenne_Maths",
    "Vos parents ou tuteurs travaillent-ils? Que font-ils comme travail?": "Travail_Parents",
    "Recevez-vous des cours particuliers à domicile?": "Cours_Particuliers",
    "Avez-vous éprouvé des difficultés d'apprentissage à l’entrée en classe de 6ème (en seconde), maintenant ? Si oui, dans quelles matières et notions ?": "Difficultes_6e",
    "Où avez-vous obtenu (allez-vous obtenir) votre Brevet ?": "Lieu_Brevet",
    "Y a-t-il eu des changements dans votre parcours depuis la 6è du collège ? lesquels ?": "Changements_Parcours",
    "Quels sont vos projets actuels une fois le BAC obtenu ? Quelle spécialité/option du BAC ?": "Projets_BAC",
    "Selon vous, vos difficultés en sciences, en maths sont-elles liées à l’utilisation de la langue ?": "Difficultes_Langue",
    "Quelle est votre langue maternelle ?": "Langue_Maternelle",
    "Etes-vous né sur le territoire de Mayotte ?": "Ne_Mayotte",
    "Avez-vous un accès internet chez vous à la maison ? Combien de devoirs faits nécessitaient une connexion ?": "Acces_Internet",
    "Quelle notion de mathématiques retenez-vous aujourd’hui ? Qu’est ce qui fait que vous l’aimiez ou pas ?": "Notion_Maths",
    "Expression libre sur l'apprentissage/enseignement de mathématiques, d'informatique, de sciences.": "Expression_Libre"
}

dh = rename_columns(dp, rename_dict)
print("Après renommage:\n", dh)
dh.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%
df=pd.read_csv("apprentissage.csv")
# Vérification des noms de colonnes avant renommage
print("Colonnes avant nettoyage :", df.columns.tolist())

# Nettoyage des noms de colonnes
df.columns = df.columns.str.strip()  # Supprime les espaces invisibles
df.columns = df.columns.str.replace("’", "'", regex=False)  # Remplace les apostrophes typographiques

# Vérification après nettoyage
print("Colonnes après nettoyage :", df.columns.tolist())

# Dictionnaire de renommage
rename_dict = {
    "Age": "Age",
    "Etablissement": "Etablissement",
    "Classe": "Classe",
    "Commune de domicile": "Commune",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage des mathématiques?": "Heures_Maths",
    "Quel est votre rapport aux mathématiques ? Sur une échelle de 1 à 10 (du très mauvais à un excellent rapport), à combien auto-évaluez-vous ?": "Auto_eval_Maths",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage des autres sciences?": "Heures_Sciences",
    "Combien d'heures consacrez-vous par semaine à la révision, apprentissage de la langue française?": "Heures_Francais",
    "Sur une échelle de 1 à 10, donnez votre dernière moyenne de trimestre (note sur 10) en mathématiques?": "Moyenne_Maths",
    "Vous parents ou tuteurs travaillent-ils? Que font-ils comme travail?": "Travail_Parents",
    "Recevez-vous des cours particuliers à domicile?": "Cours_Particuliers",
    "Avez-vous éprouvé des difficultés d'apprentissage à l'entrée en  classe de 6ème (en seconde), maintenant ?  Si oui, dans quelles matières et notions ?": "Difficultes_entree_6e_ou_seconde",
    "Où avez-vous obtenu (allez-vous obtenir) votre Brevet ?": "Lieu_Brevet",
    "Y a-t-il eu des changements dans votre parcours depuis la 6è du collège ? lesquels ?": "Changements_Parcours",
    "Quels sont vos projets actuels une fois le BAC obtenu ? Quelle spécialité/option du BAC ?": "Projets_BAC",
    "Selon vous, vos difficultés en sciences, en maths sont-elles liées à l'utilisation de la langue ?": "Difficultes_Langue",
    "Quelle est votre langue maternelle ?": "Langue_Maternelle",
    "Etes-vous né sur le territoire de Mayotte ?": "Ne_Mayotte",
    "Avez-vous un accès internet chez vous à la maison ? Combien de devoirs faits nécessitaient une connexion ?": "Acces_Internet",
    "Quelle notion de mathématiques retenez-vous aujourd'hui ? Qu'est ce qui fait que vous l'aimiez ou pas ?": "Notion_Maths",
    "Expression libre sur l'apprentissage/enseignement de mathématiques, d'informatique, de sciences.": "Expression_Libre"
}

# Application du renommage
df = df.rename(columns=rename_dict)

# Vérification après renommage
print("Colonnes après renommage :", df.columns.tolist())

# Sauvegarde du fichier
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%
