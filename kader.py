#%%
import pandas as pd
import re
import shutil

# Chemin du fichier d'entrée
file_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/apprentissage.csv'

# Charger le fichier
df = pd.read_csv(file_path)

# Fonction de nettoyage et correction de la colonne 'Age'
def clean_and_correct_age(age):
    if isinstance(age, str):
        age = age.strip().lower()

        # Gestion des cas "A ans et B mois"
        match = re.search(r'(\d+)\s*ans?\s*et\s*(\d+)\s*mois?', age)
        if match:
            years, months = map(int, match.groups())
            return years + (1 if months >= 6 else 0)

        # Extraction du premier nombre trouvé
        match = re.search(r'\d+', age)
        if match:
            return int(match.group())
    
    return None

# Appliquer la correction généralisée à la colonne 'Age'
df['Age'] = df['Age'].apply(clean_and_correct_age)

# Convertir la colonne en entier après correction
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Enregistrer le fichier nettoyé
new_file_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/apprentissage_nettoye.csv'
df.to_csv(new_file_path, index=False)

print(f'Fichier nettoyé enregistré sous : {new_file_path}')

# %%
import pandas as pd
import difflib
import shutil
import re

# Charger les fichiers
apprentissage_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/apprentissage_nettoye.csv'
ecole_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/ecole.csv'

apprentissage_df = pd.read_csv(apprentissage_path)
ecole_df = pd.read_csv(ecole_path)

# Normaliser les noms des colonnes pour éviter les erreurs d'espace et de casse
apprentissage_df.columns = apprentissage_df.columns.str.strip().str.lower()
ecole_df.columns = ecole_df.columns.str.strip().str.lower()

# Normaliser les noms des établissements en minuscules pour éviter les erreurs de correspondance
apprentissage_df['etablissement'] = apprentissage_df['etablissement'].str.lower().str.strip()
ecole_df['collège et lycée'] = ecole_df['collège et lycée'].str.lower().str.strip()

# Créer un dictionnaire de correspondance basé sur la similarité des noms
correspondance = {}
ecole_noms = ecole_df['collège et lycée'].tolist()

for etablissement in apprentissage_df['etablissement'].unique():
    match = difflib.get_close_matches(etablissement, ecole_noms, n=1, cutoff=0.6)
    if match:
        correspondance[etablissement] = match[0]
    else:
        correspondance[etablissement] = etablissement  # Conserver le nom d'origine s'il n'y a pas de correspondance

# Appliquer la correspondance à la colonne 'Etablissement'
apprentissage_df['etablissement'] = apprentissage_df['etablissement'].map(correspondance)

# Dictionnaire de remplacement pour 'Commune de domicile'
commune_remplacement = {
    'trevani': 'Koungou',
    'barakani': 'Ouangani',
    'chiconi': 'Tsingoni',
    'kaweni': 'Mamoudzou',
    '9 rue zena m\'dere': 'Koungou',
    'konkou': 'Koungou',
    'kanani': 'Ouangani',
    'handzo': 'Hapandzo'
}

# Trouver la bonne colonne pour 'Commune de domicile'
colonne_cible = [col for col in apprentissage_df.columns if "commune" in col.lower()]
if colonne_cible:
    colonne_commune = colonne_cible[0]  # Prendre le premier match trouvé
    # Remplacer les noms de communes dans la colonne correcte
    apprentissage_df[colonne_commune] = apprentissage_df[colonne_commune].replace(commune_remplacement)
else:
    print("Aucune colonne correspondante pour 'Commune de domicile' trouvée.")

# Fonction pour convertir les heures en minutes
def convertir_en_minutes(temps):
    match = re.search(r"(\d+)\s*h(?:eures?)?\s*(\d*)", str(temps).lower())
    if match:
        heures = int(match.group(1))
        minutes = int(match.group(2)) if match.group(2) else 0
        return heures * 60 + minutes
    match = re.search(r"(\d+)\s*min", str(temps).lower())
    if match:
        return int(match.group(1))
    return None

# Appliquer la conversion sur la colonne 'heures_maths'
apprentissage_df['heures_maths'] = apprentissage_df['heures_maths'].apply(convertir_en_minutes)

# Sauvegarder le fichier modifié
new_file_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/apprentissage_nettoye1.csv'
apprentissage_df.to_csv(new_file_path, index=False)

print(f'Fichier nettoyé et mis à jour enregistré sous : {new_file_path}')

# %%
