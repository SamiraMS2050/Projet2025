#%%
#charger les bibliothèques necessaire 
import numpy as np
import pandas as pd
from fuzzywuzzy import process
import unicodedata
# Charger le fichier CSV
df = pd.read_csv('nettoye.csv')
#%%
#Nettoyage de la colonne classe
#fonction pour recuperer la premiere lettre d un mot 
def premierlettre(chaine):
    if pd.isna(chaine) or len(chaine) == 0:
        return ''
    return chaine[0]
#fonction pour la correction
def mapper_classe(classe):
    premier_lettre = premierlettre(classe)
    if premier_lettre in ['2', 's', '*']:
        return 'Seconde'
    elif premier_lettre == '1' and classe not in {'1STI2D', '1ST2S', '1st2s', '1 std2a', '1 STMG3', '1 agora', '1er stmg4', '1mcv1', '1stmg4', '1mcvAPP'}:
        return 'Première'
    elif premier_lettre == 'P' and classe != 'P18STI2D':
        return 'Première'
    elif premier_lettre == '3':
        return 'Troisième'
    elif premier_lettre in ['4', '5', '6']:
        return { '4': 'Quatrième', '5': 'Cinquième', '6': 'Sixième' }[premier_lettre]
    elif premier_lettre == 'T' and classe not in {'TSTMG5', 'Terminal  STMG5', 'T OTM', 'Tstmg', 'T STMG'}:
        return 'Terminale'
    elif premier_lettre in ['B', 't']:
        return 'BTS'
    elif classe in {'TSTMG5', 'Terminal  STMG5', 'Tstmg', 'T STMG'}:
        return 'Terminale STMG'
    elif classe in {'1 STMG3', '1er stmg4', '1stmg4'}:
        return 'Première STMG'
    return classe

# Retourne la valeur originale si aucun chiffre n'est trouvé
#application de la correction à apprentissage 
df['Classe'] = df['Classe'].apply(mapper_classe)
#%%
################Nettoyage de la colonne Etablissement##########
#standarisation  de la colonne 
# Convertir la colonne 'Etablissement' en minuscules
df['Etablissement'] = df['Etablissement'].str.lower()
from unidecode import unidecode
# Retirer les accents des noms de lycées
df['Etablissement'] = df['Etablissement'].apply(unidecode)

# Supposons que df soit déjà défini
#df['Etablissement'] = df['Etablissement'].str.replace(r'^[\*\-\s]+', '', regex=True)  # Nettoyage des caractères spéciaux
df['Etablissement'] = df['Etablissement'].str.replace("lycée", "").str.strip()  # Supprime "lycée" et nettoie les espaces
df['Etablissement'] = df['Etablissement'].str.replace("lycee", "").str.strip()  # Supprime "lycée" et nettoie les espaces
#df.to_csv('apprentissage.csv', index=False)  # Sauvegarde du fichier mis à jour
df['Etablissement'] = df['Etablissement'].str.replace("s", "").str.strip()  # Supprime "lycée" et nettoie les espaces
# Supprimer "LPO" et "lycée" (en ignorant la casse) des noms de lycées
df['Etablissement'] = df['Etablissement'].str.replace(r'\b(lpo|lycee|college|des|de|-des|lycees|polyvalent|  |-  )\b', '', case=False, regex=True)
# Supprimer les espaces au début et à la fin des noms de lycées
df['Etablissement'] = df['Etablissement'].str.strip()
# Supprimer les astérisques, les tirets et les espaces en début de chaîne
df['Etablissement'] = df['Etablissement'].str.replace(r'^[\*\-\s]+', '', regex=True)
#application  des corrections à la base de données
df.to_csv('apprentissage.csv', index=False)
#nettoyage de la colonne 
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

# Appliquer la correction sur la colonne "Etablissement"
df["Etablissement"] = df["Etablissement"].apply(corrige_nom)
#%%
############NETTOYAGE DE LA COLONNE COMMUNE DE DOMICILE#######
#standarisation des noms 
#conversion en minuscule
df['Commune de  domicile'] = df['Commune de  domicile'].str.lower()
#df['Etablissement'] = df['Etablissement'].str.replace(r'^[\*\-\s]+', '', regex=True)  # Nettoyage des caractères spéciaux
df['Commune de  domicile'] = df['Commune de  domicile'].str.replace("commune", "").str.strip()  # Supprime "commune" et nettoie les espaces
# Supprimer les astérisques, les tirets et les espaces en début de chaîne
df['Commune de  domicile'] = df['Commune de  domicile'].str.replace(r'^[\*\-\s]+', '', regex=True)

# Retirer les accents des noms de commune
df['Commune de  domicile'] = df['Commune de  domicile'].apply(unidecode)
#definition de la fonction correction 
def corrige_commune(commune):
    premier_lettre = premierlettre(commune)
    if premier_lettre == 'o' or commune=='kanani' or commune=='kahani' or commune=='hapandzo' or commune=='handzo' or commune=='hapandza' or commune=='barakani' or commune=='de ouangani':
        return 'Commune de Ouangani'
    elif commune=='trevani' or commune=='kongou' or commune=="9 rue zena m'dere" or commune=='koungou' or commune=='konkou' :
        return 'Commune de Koungou' 
    elif commune=='kaweni' or commune=='mamoudzou' or commune=='mamoudzou97600' or commune=='mamoudzou (97600)' or commune=='mtsapere' :
        return 'Commune de Mamoudzou'
    elif commune=='chiconi':
            return 'Commune de Chiconi'
    elif commune== 'dembeni':
            return 'Commune de Dembeni'
    elif commune== "m'tsangamouji" or commune=='mtsangamouji':
            return "Commune de M'Tsangamouji" 
    elif commune== "pamandzi":
            return "Commune de Pamandzi"
    elif commune== "tsingoni":
            return "Commune de Tsingoni"
    elif commune== "bandraboua":
            return "Commune de Bandraboua"
    else:
        return commune 
# Appliquer la correction sur la colonne "Commune de domicile"
df["Commune de  domicile"] = df["Commune de  domicile"].apply(corrige_commune)
#%%
########NETTOYAGE DE LA COLONNE LANGUE MATERNELLE ############
#standarisation
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.lower()
# 2. Suppression des mots inutiles (comme "le", "langues", "lague", "ce", etc.) dans la colonne
#    Utilisation de regex pour cibler ces mots précis et les supprimer
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("le", "").str.strip() 
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("langues", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("lague", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("ce", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("la", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("ngue", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("je", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("maternel", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("ma langue maternel c'est", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("c'est", "").str.strip()
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace("parle ", "").str.strip()
# 3. Suppression des caractères spéciaux au début des chaînes (comme *,-, espaces)
df['Langue_Maternelle'] = df['Langue_Maternelle'].str.replace(r'^[\*\-\s]+', '', regex=True)
# 4. Suppression des accents (conversion des caractères spéciaux en caractères ASCII)
df['Langue_Maternelle'] = df['Langue_Maternelle'].apply(unidecode)
#definition de la fonction 
def corrige_langue(langue):
    if langue=='shimaore' or langue=='comorien' or langue=='comorienne' or langue=='mahoraise' or langue=='chimaore' or langue=='shimaorais' or langue=='maore' or langue=='chimaore.' or langue=='shimahorais' or langue=='chim1ore'or langue=='shimaoree' or langue=='chimaorai' or langue=='mahorais' or langue=='chimahore' or langue=='maorai' or langue=='shiamore' or langue=='shimaorer' or langue=='chimaorais' or langue=='chi maore' or langue=='mahorais.' or langue=='shimahorais'  or langue=='ma   shimaore' or langue=='ma     chimaorais' or langue=='schimaore' or langue=='maores':
        return 'Shimaoré'
    elif langue=="ma   depuis toute petite que mes parents m'ont appris c  francais mais comme  vis a mayotte   par aussi.  par plus  francais que  mahorais":
        return "Français"
    elif langue=='kibushi' or langue=='kibouchi' or langue=='shiboushi' or langue=='chibuchi' or langue=='chibouchi' or langue=='shibushi' or langue=='malgache(shibushi)' or langue=='malgache: chibouchi':
         return 'kibushi'
    elif langue=='shimaore et shi comores (ngazidza)' or langue=='comorien, mahorais' or langue=='par  chi-mahore &  chi-comores' or langue=='shimaore / shibouchi' or langue=='chimaorais ou principament  comorien' or langue=='shimaore et francais.' or langue=='ma nge    shimaore et  francais' 'fracais' or langue=='shimahorais ( mayotte)' or langue=='ma nge    shimaore et  francais':
        return 'Shimaoré'
    elif langue=='chindzouani' or langue=='shindzouani' or langue=='comorienne ( anjouan )' or langue=='anjouanais':
         return 'Shindzouani'
    elif langue=='francais' or langue=='fracais' or langue=='Français':
        return 'Français'
    elif langue=='chinoi':
         return 'Chinois'
    elif langue=='creo reunionnais':
         return 'Creole'
    elif langue=='swahili, ( par un peu  linga)':
        return 'Swahili'
    elif langue=='pion' or langue=='pas':
        return np.nan
    elif langue=='malgache' or langue== 'malgashe':
         return 'Malgache'
    else:
        return langue 
# Appliquer la correction sur la colonne "Etablissement"
df["Langue_Maternelle"] = df["Langue_Maternelle"].apply(corrige_langue)
#%%
#################application des correction a la base de donnée
df.to_csv("nettoye.csv", index=False)
# %%
df = pd.read_csv('nettoye.csv')
def corrige(nom):
    if nom=="9 rue zena m'dere":
        return 'Commune de Koungou'
    else:
        return nom
# Appliquer la correction sur la colonne "Commune de domicile"
df["Commune de  domicile"] = df["Commune de  domicile"].apply(corrige)   
df.to_csv("nettoye.csv", index=False)   
# %%
