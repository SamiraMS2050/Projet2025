#%%
import pandas as pd
def conversion(nom):
    if nom=='non' or nom=="nn" or nom=="non.":
        return 0
    elif nom=='oui' or nom=="oui u" or nom=="oui.":
        return 1
    else:
        return nom
# Convertir toutes les valeurs de la colonne  en minuscules et supprimer les espaces superflus
# 'str.lower()' convertit toutes les lettres en minuscules pour uniformiser les valeurs
# 'str.strip()' enlève les espaces avant et après chaque valeur, ce qui permet de corriger des cas comme ' oui ' ou 'non '.
df = pd.read_csv('nettoye.csv')
df['Cours_Particuliers'] = df['Cours_Particuliers'].str.lower().str.strip()
df['Cours_Particuliers'] = df['Cours_Particuliers'].apply(conversion)
df['Travail_Parents'] = df['Travail_Parents'].str.lower().str.strip()
df['Travail_Parents'] = df['Travail_Parents'].apply(conversion)
df['Difficultes_6e'] = df['Difficultes_6e'].str.lower().str.strip()
df['Difficultes_6e'] = df['Difficultes_6e'].apply(conversion)
df['Changements_Parcours'] = df['Changements_Parcours'].str.lower().str.strip()
df['Changements_Parcours'] = df['Changements_Parcours'].apply(conversion)
df['Difficultes_Langue'] = df['Difficultes_Langue'].str.lower().str.strip()
df['Difficultes_Langue'] = df['Difficultes_Langue'].apply(conversion)
df['Ne_Mayotte'] = df['Ne_Mayotte'].str.lower().str.strip()
df['Ne_Mayotte'] = df['Ne_Mayotte'].apply(conversion)
df['Acces_Internet'] = df['Acces_Internet'].str.lower().str.strip()
df['Acces_Internet'] = df['Acces_Internet'].apply(conversion)
df.to_csv("nettoye.csv", index=False)  
#%%
d = df['Acces_Internet'].unique()
print(d)
# %%
####par contre pour que les tests marchent faudra avoir une copie de nettoye.csv avant de lui appliqueer les conversion 
#et de ce fait la premiere fonction test prendra la copie 
#et la deuxieme fonction test prendra le fichier nettoye.csv apres conversion 
###Apres l execution des 2 codes on doit avoir les 2 valeurs de i et j egaux ce qui justifiera que le code fait bien ce qu on lui demande


######## Première fonction test 
i=0
j=0
df = pd.read_csv('nettoye_copie.csv')
df['Acces_Internet'] = df['Acces_Internet'].str.lower().str.strip()
for n in df['Acces_Internet']:
    if n=='oui':
        i=i+1
    elif n=='non':
        j=j+1
print(i)
print(j)

# %%
# Deuxième fonction test 
i=0
j=0
df = pd.read_csv('nettoye.csv')
for n in df['Acces_Internet']:
    if n=='1':
        i=i+1
    elif n=='0':
        j=j+1
print(i)
print(j)

# %%
