#%%
import pandas as pd
import re

# Charger le fichier CSV
file_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/nettoye.csv'  # Remplace avec le bon chemin
output_file_path = 'C:/Users/abkat/OneDrive/Documents/master ssd/projet/nettoye_minutes.csv'
df = pd.read_csv(file_path)

def convert_to_minutes(time_str):
    """
    Convertit une chaîne de temps en minutes.
    - "2h" -> 120
    - "1h30" -> 90
    - "45min" -> 45
    - "2 h" -> 120
    - "1min" -> 1
    - "3" (sans unité) -> 180 (traité comme heures)
    """
    if pd.isna(time_str):
        return None
    
    time_str = time_str.strip().lower().replace(" ", "")  # Supprimer espaces et uniformiser

    # Vérifier si c'est juste un nombre (sans 'h' ou 'min')
    if time_str.isdigit():
        return int(time_str) * 60

    hours = 0
    minutes = 0

    # Extraire les heures et minutes
    hour_match = re.search(r"(\d+)h", time_str)
    minute_match = re.search(r"(\d+)min", time_str)

    if hour_match:
        hours = int(hour_match.group(1))
    if minute_match:
        minutes = int(minute_match.group(1))
    
    return hours * 60 + minutes

# Colonnes contenant les heures
hour_columns = ["Heures_Maths", "Heures_Sciences", "Heures_Francais"]

# Appliquer la conversion
for col in hour_columns:
    if col in df.columns:
        df[col + "_Minutes"] = df[col].apply(convert_to_minutes)

# Sauvegarder le fichier modifié
df.to_csv(output_file_path, index=False)

print(f"Fichier mis à jour enregistré sous : {output_file_path}")


# %%
