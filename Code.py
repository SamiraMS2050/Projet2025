#%%
import numpy as np
import pandas as pd
#%%
df=pd.read_csv("Apprentissage.csv")
dp=pd.read_csv("nettoye .csv")
#dp=dp.drop(116)
#dp.to_csv("apprentissage1.csv", index=False, encoding='utf-8')
# %%
#df = df.drop(df.columns[[0,7,15,18,20,21,25,28,29,30]], axis=1)
dp=dp.drop(dp.columns[[12,19,20]],axis=1)
dp.to_csv(" Base_de_donnee.csv", index=False, encoding='utf-8')
# %%
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
print(df)
#%%

# Suppression de "ans" ou "Ans" dans la première colonne
dp.iloc[:, 0] = dp.iloc[:, 0].str.replace(r'\s*[aA]ns', '', regex=True)

# Affichage du DataFrame mis à jour
print(dp)
dp.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%
#print(df.iloc[:, 1])
print(df[["Age"]])
#pour supprimer des colonnes 
#df = df.drop(df.columns[[0,27, 28,29]], axis=1)
df.to_csv("apprentissage.csv", index=False, encoding='utf-8')
print(df)
# %%
#fp=pd.read_csv("apprentissag.csv")
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
import pandas as pd
import re

def clean_and_extract_time(df, column_name):
    """
    Nettoie une colonne en supprimant les valeurs ne contenant pas de chiffres
    et en extrayant uniquement les expressions contenant 'h', 'H', 'min' ou des nombres seuls.

    Args:
        df (pd.DataFrame): Le DataFrame contenant la colonne à traiter.
        column_name (str): Le nom de la colonne à nettoyer.

    Returns:
        pd.DataFrame: Le DataFrame avec la colonne nettoyée.
    """
    def extraire_temps(val):
        val = str(val)  # Convertir en chaîne pour éviter les erreurs
        if re.fullmatch(r'\d+', val):  # Vérifie si c'est un nombre pur (ex: "45", "120")
            return val  
        correspondance = re.findall(r'\d+\s*[hH]|\d+\s*min|\d+', val)  # Capture heures, minutes et nombres seuls
        return ' '.join(correspondance) if correspondance else ''
    
    df[column_name] = df[column_name].apply(extraire_temps)
    return df
#%%
print(dp)

dp = clean_and_extract_time(dp, 'Heures_Maths')

print("\nAprès nettoyage:")
print(dp)

dp.to_csv("apprentissage.csv", index=False, encoding='utf-8')
#%%

dp = clean_and_extract_time(dp, 'Heures_Sciences')

print("\nAprès nettoyage:")
print(dp)

dp.to_csv("apprentissage.csv", index=False, encoding='utf-8')
# %%

dp = clean_and_extract_time(dp, 'Heures_Francais')

print("\nAprès nettoyage:")
print(dp)

dp.to_csv("apprentissage.csv", index=False, encoding='utf-8')
#%%
dp=pd.read_csv("apprentissag.csv")
def nettoyer_colonne(df, colonne):
    df[colonne] = pd.to_numeric(df[colonne], errors='coerce')  # Convertit en nombres, remplace les chaînes par NaN
    df[colonne] = df[colonne].apply(lambda x: x if 0 <= x <= 10 else None)  # Garde uniquement les nombres entre 0 et 10
nettoyer_colonne(dp, 'Moyenne_Maths') 
dp.to_csv("nettoye.csv", index=False, encoding='utf-8')   
# %%
import csv

def comparer_fichiers_csv(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        lignes_fichier1 = list(reader1)
        lignes_fichier2 = list(reader2)

        max_lignes = max(len(lignes_fichier1), len(lignes_fichier2))

        for i in range(max_lignes):
            nb_col1 = len(lignes_fichier1[i]) if i < len(lignes_fichier1) else "Ligne absente"
            nb_col2 = len(lignes_fichier2[i]) if i < len(lignes_fichier2) else "Ligne absente"

            if nb_col1 != nb_col2:
                print(f"🔴 Ligne {i+1} : {nb_col1} colonnes dans {fichier1}, {nb_col2} colonnes dans {fichier2}")
            else:
                print(f"✅ Ligne {i+1} : Même nombre de colonnes ({nb_col1})")

# Remplace ces chemins par ceux de tes fichiers
fichier1 = "apprentissage.csv"
fichier2 = "apprentissag.csv"

comparer_fichiers_csv(fichier1, fichier2)

# %%
