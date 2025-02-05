
# %%
def premierlettre(chaine):
    if pd.isna(chaine) or len(chaine) == 0:
        return ''
    return chaine[0]

def mapper_classe(classe):
    premier_lettre = premierlettre(classe)
    if premier_lettre == '1' or premier_lettre == 'P':
        return 'Première'
    elif premier_lettre == '2' or premier_lettre == 's' or premier_lettre == '*':
        return 'Seconde'
    elif premier_lettre == '3':
        return 'Troisième'
    elif premier_lettre == '4':
            return 'Quatrième'
    elif premier_lettre == '5':
            return 'Cinquième'
    elif premier_lettre == '6':
            return 'Sixième'
    elif premier_lettre == 'T' or premier_lettre == 't':
        return 'Terminale'
    elif premier_lettre == 'B' or premier_lettre == 't':
        return 'BTS'
    else:
        return classe  # Retourne la valeur originale si aucun chiffre n'est trouvé
df=pd.read_csv('apprentissage.csv')
df['Classe'] = df['Classe'].apply(mapper_classe)
print(df)
# Récupérer les noms uniques des lycées
lyceescor = df["Classe"].unique()
# Enregistrer le DataFrame modifié dans le même fichier CSV
df.to_csv('apprentissage.csv', index=False)

# Afficher les noms des lycées
print(lyceescor)
# %%
# Charger le fichier CSV
df = pd.read_csv('apprentissage.csv')
# Convertir la colonne 'Nom_Lycée' en minuscules
df['Etablissement'] = df['Etablissement'].str.lower()
from unidecode import unidecode

# Retirer les accents des noms de lycées
df['Etablissement'] = df['Etablissement'].apply(unidecode)


# Supprimer "LPO" et "lycée" (en ignorant la casse) des noms de lycées
df['Etablissement'] = df['Etablissement'].str.replace(r'\b(lpo|lycee|college|des|de|-des|lycees|polyvalent|  |-  )\b', '', case=False, regex=True)
# Supprimer les espaces au début et à la fin des noms de lycées
df['Etablissement'] = df['Etablissement'].str.strip()
# Supprimer les astérisques, les tirets et les espaces en début de chaîne
df['Etablissement'] = df['Etablissement'].str.replace(r'^[\*\-\s]+', '', regex=True)
df.to_csv('apprentissage.csv', index=False)
import pandas as pd


# Enregistrer le DataFrame modifié dans le même fichier CSV
df.to_csv('apprentissage.csv', index=False)

# %%

import pandas as pd
from fuzzywuzzy import process

# Fonction pour nettoyer les noms avant de les corriger
def nettoyer_nom(nom):
    return nom.strip().replace('(', '').replace(')', '').replace(',', '').replace('é', 'e').lower()

# Fonction pour corriger les noms automatiquement
def corrige_nom(classe):
    premier_lettre = premierlettre(classe)
    if premier_lettre == 'm':
        return 'Lycée de Mamoudzou Nord'
    elif premier_lettre == 'o' or premier_lettre == 'c' or premier_lettre == 'u':
        return 'Collège de Ouangani' 
    elif premier_lettre == 'y'or premier_lettre == 'b':
        return 'Lycée Younoussa Bamana'
    elif premier_lettre == 'l':
            return 'Lycée des Lumières'
    elif premier_lettre == 'd':
            return 'Lycée de Dembéni'
    else:
        return classe  # Retourne la valeur originale si aucun chiffre n'est trouvé
# Charger ton DataFrame
df = pd.read_csv("apprentissage.csv")

# Appliquer la correction sur la colonne "Etablissement"
df["Etablissement"] = df["Etablissement"].apply(corrige_nom)

# Sauvegarder le fichier corrigé
df.to_csv("apprentissage.csv", index=False)

# Charger le fichier corrigé
df1 = pd.read_csv("apprentissage.csv")

# Récupérer les noms uniques des lycées
lyceescor = df1["Etablissement"].unique()

# Afficher les noms des lycées
print(lyceescor)

# %%

import pandas as pd
import unicodedata

# Charger le fichier CSV
df = pd.read_csv('apprentissage.csv')
df['Commune de  domicile'] = df['Commune de  domicile'].str.lower()
from unidecode import unidecode

# Retirer les accents des noms de lycées
df['Commune de  domicile'] = df['Commune de  domicile'].apply(unidecode)
df.to_csv("apprentissage.csv", index=False)
# Afficher le DataFrame modifié
df1 = pd.read_csv("apprentissage.csv")
lyceescor = df["Commune de  domicile"].unique()

# Afficher les noms des lycées
print(lyceescor)# %%

# %%
