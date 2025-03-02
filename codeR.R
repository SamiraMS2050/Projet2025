library(readr)
library(ggplot2)
install.packages("naniar")
library(naniar)
library(dplyr)
Data<-read.csv('Base_de_donnee.csv',header=TRUE,sep=',')
#Suppression de la colonne Auto_eval
Data$Auto_eval_Maths<- NULL
# remplacer les "" par des donnees manquantes
Data[Data == ""] <- NA
View(Data)
#Convertir en factor les variables nominales
Data[sapply(Data, is.character)] <- lapply(Data[sapply(Data, is.character)], as.factor)
str(Data)#Donne le nombre d individus et de variables ainsi que le type de variables 
colSums(is.na(Data))#Donne le nombre de valeurs manquantes par colonnes
gg_miss_var(Data)#Represente le nombre de donnees manquantes par colonnes
#Statistiques Descriptives 
#Valeurs numeriques
summary(Data)
# le nombre d élements par categorie
table(Data$Classe)
library(stringr)
# Nettoyer la colonne Projets_BAC
Data$Projets_BAC <- tolower(Data$Projets_BAC)  # Convertir en minuscules
Data$Projets_BAC <- str_trim(Data$Projets_BAC)  # Supprimer les espaces inutiles
Data$Projets_BAC <- str_replace_all(Data$Projets_BAC, "\\s+", "_")  # Remplacer les espaces internes par "_"
#Application des methodes de traitement des donnée manquante
#library(tidyr)
#Pour les colonnes numeriques
# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Temps_Francais.mn.  # Copier la colonne avant traitement
# Appliquer l'imputation par la median
Data$Temps_Francais.mn.[is.na(Data$Temps_Francais.mn.)] <- median(Data$Temps_Francais.mn., na.rm = TRUE)
# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Moyenne_Maths  # Copier la colonne avant traitement
# Appliquer l'imputation par la median
Data$Moyenne_Maths[is.na(Data$Moyenne_Maths)] <- median(Data$Moyenne_Maths, na.rm = TRUE)

#Pour les colonnes binaires
# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Acces_Internet # Remplace "Colonne_Binaire" par ta colonne

# Imputer les valeurs manquantes avec la médiane (ou le mode)
valeur_imputation <- median(Data$Acces_Internet, na.rm = TRUE)  # Utiliser mediane
Data$Acces_Internet[is.na(Data$Acces_Internet)] <- valeur_imputation

# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Changements_Parcours # Remplace "Colonne_Binaire" par ta colonne

# Imputer les valeurs manquantes avec la médiane (ou le mode)
valeur_imputation <- median(Data$Changements_Parcours, na.rm = TRUE)  # Utiliser mediane
Data$Changements_Parcours[is.na(Data$Changements_Parcours)] <- valeur_imputation


# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Difficultes_Langue # Remplace "Colonne_Binaire" par ta colonne

# Imputer les valeurs manquantes avec la médiane (ou le mode)
valeur_imputation <- median(Data$Difficultes_Langue, na.rm = TRUE)  # Utiliser mediane
Data$Difficultes_Langue[is.na(Data$Difficultes_Langue)] <- valeur_imputation


# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Ne_Mayotte # Remplace "Colonne_Binaire" par ta colonne

# Imputer les valeurs manquantes avec la médiane (ou le mode)
valeur_imputation <- median(Data$Ne_Mayotte, na.rm = TRUE)  # Utiliser mediane
Data$Ne_Mayotte[is.na(Data$Ne_Mayotte)] <- valeur_imputation

# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Travail_Parents # Remplace "Colonne_Binaire" par ta colonne

# Imputer les valeurs manquantes avec la médiane (ou le mode)
valeur_imputation <- median(Data$Travail_Parents, na.rm = TRUE)  # Utiliser mediane
Data$Travail_Parents[is.na(Data$Travail_Parents)] <- valeur_imputation

#pour les colonnes chaines de caracteres

# Stocker les valeurs avant imputation
Data$Var_avant <- Data$Langue_Maternelle # S'assurer qu'on copie la colonne correctement


# Trouver le mode (valeur la plus fréquente)
mode_value <- names(sort(table(Data$Langue_Maternelle), decreasing = TRUE))[1]

# Appliquer l'imputation par le mode
Data$Langue_Maternelle[is.na(Data$Langue_Maternelle)] <- mode_value
Data$Var_avant<-NULL

# Utilisation de la méthode des K-NN pour la colonne Projets_BAC
install.packages("VIM")  # Si non installé
library(VIM)
Data <- kNN(Data, variable = "Projets_BAC", k = 5)
table(Data$Projets_BAC)
Data$Projets_BAC_imp<-NULL
#Fin traitement de données manquantes
#Nettoyage de la colonne langue maternelle
Data$Langue_Maternelle[c(60,64,83,84,86,107,141,159,161)] <- NA
Data$Langue_Maternelle <- str_trim(tolower(Data$Langue_Maternelle))
# Liste des valeurs valides
valeurs_valides <- c("shimaoré", "kibushi", "malgache", "français", "shindzouani",NA)

# Remplacement des valeurs non valides par "autres"
Data$Langue_Maternelle <- ifelse(Data$Langue_Maternelle %in% valeurs_valides, 
                                 Data$Langue_Maternelle, "autres")
View(Data)
library(fastDummies)
# Transformer en variables binaires
colonnes_a_encoder <- c("Langue_Maternelle", "Projets_BAC","Etablissement","Classe","Domicile")
Dat <- dummy_cols(data, select_columns =colonnes_a_encoder, remove_first_dummy = FALSE, remove_selected_columns = TRUE)
View(Dat)
write.csv(Dat, "Data_cleaned.csv", row.names = FALSE)
data<-read.csv("Data_cleaned.csv")
View(data)
colSums(is.na(data))
data$Langue_Maternelle_NA<-NULL
write.csv(data, "Data_cleaned.csv", row.names = FALSE)
#Le fichier Data_cleaned.csv contient les donnees complete en binaires 
#Etude des corrélations
library(corrplot)
library(ggcorrplot)
library(corrr)
library(reshape2)
install.packages("ggcorrplot")
install.packages("corrr")
# 1️⃣ Sélectionner uniquement les colonnes numériques
numeric_vars <- data[, sapply(data, is.numeric)] 
# Calculer la matrice de corrélation
# 2️⃣ Exclure les variables binaires (qui n'ont que 2 valeurs uniques : 0 et 1)
numeric_vars_filtered <- numeric_vars[, sapply(numeric_vars, function(x) length(unique(x)) > 2)]
corr_matrix <- cor(numeric_vars_filtered, use = "complete.obs")

# Remplacer les NA par 0 pour éviter des trous dans le graphique
corr_matrix[is.na(corr_matrix)] <- 0  

# Convertir la matrice en format long pour ggplot2
cor_matrix<- melt(corr_matrix)

# Tracer la matrice avec ggplot2
ggplot(cor_matrix, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") + 
  geom_text(aes(label = round(value, 2)), size = 4) +  # Affichage des valeurs
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", midpoint = 0) +
  labs(title = "Matrice de Corrélation des variables quantitatives",
       x = "", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10))

# 1️⃣ Sélectionner uniquement les colonnes binaires (qui ne contiennent que 0 et 1)
binary_vars <- Data[, sapply(Data, function(x) is.numeric(x) && all(x %in% c(0, 1, NA)))]

# 2️⃣ Calculer la matrice de corrélation en utilisant le coefficient de Pearson (adapté aux variables binaires)
cor_matrix_bin <- cor(binary_vars, use = "pairwise.complete.obs", method = "pearson")
 
# Remplacer les NA par 0 pour éviter des trous dans le graphique
cor_matrix_bin[is.na(cor_matrix_bin)] <- 0  

# Convertir la matrice en format long pour ggplot2
cor_matrix_bins <- melt(cor_matrix_bin)

# Tracer la matrice avec ggplot2
ggplot(cor_matrix_bins, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") + 
  geom_text(aes(label = round(value, 2)), size = 4) +  # Affichage des valeurs
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", midpoint = 0) +
  labs(title = "Matrice de Corrélation des variables binaires",
       x = "", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10))

# Charger les librairies nécessaires
library(vcd) 
install.packages("vcd")
# Pour le V de Cramér

# 1️⃣ Sélectionner uniquement les colonnes qualitatives (facteurs ou chaînes de caractères)
qualitative_vars <- Data[, sapply(Data, is.factor) | sapply(Data, is.character)]

# 2️⃣ Convertir les colonnes en facteurs (si elles sont en chaînes de caractères)
qualitative_vars <- data.frame(lapply(qualitative_vars, as.factor))

# 3️⃣ Calculer la matrice de V de Cramér pour mesurer l'association entre variables catégorielles
cramer_matrix <- matrix(NA, ncol = ncol(qualitative_vars), nrow = ncol(qualitative_vars))
colnames(cramer_matrix) <- colnames(qualitative_vars)
rownames(cramer_matrix) <- colnames(qualitative_vars)

for (i in 1:ncol(qualitative_vars)) {
  for (j in 1:ncol(qualitative_vars)) {
    if (i != j) {
      tbl <- table(qualitative_vars[, i], qualitative_vars[, j]) # Créer une table de contingence
      cramer_matrix[i, j] <- assocstats(tbl)$cramer  # Calculer V de Cramér
    } else {
      cramer_matrix[i, j] <- 1  # Corrélation parfaite avec soi-même
    }
  }
}
# Remplacer les NA par 0 pour éviter des trous dans le graphique
cramer_matrix[is.na(cramer_matrix)] <- 0  

# Convertir la matrice en format long pour ggplot2
cramer <- melt(cramer_matrix)

# Tracer la matrice avec ggplot2
ggplot(cramer, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") + 
  geom_text(aes(label = round(value, 2)), size = 4) +  # Affichage des valeurs
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", midpoint = 0) +
  labs(title = "Matrice de Corrélation des variables qualitatives",
       x = "", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10))


library(psych)
install.packages("psych")# Pour le coefficient point bisérial
library(ggplot2)

# 1️⃣ Sélectionner les variables quantitatives et binaires
num_vars <- Data[, sapply(Data, is.numeric)]  # Variables numériques
binary_vars <- Data[, sapply(Data, function(x) length(unique(x)) == 2 & is.numeric(x))]  # Variables binaires (0/1)

# 2️⃣ Calculer les corrélations point bisériales
cor_matrix <- matrix(NA, ncol = ncol(binary_vars), nrow = ncol(num_vars))
colnames(cor_matrix) <- colnames(binary_vars)
rownames(cor_matrix) <- colnames(num_vars)

for (i in 1:ncol(num_vars)) {
  for (j in 1:ncol(binary_vars)) {
    cor_matrix[i, j] <- cor.test(num_vars[, i], binary_vars[, j])$estimate # Point bisérial
  }
}
# Remplacer les NA par 0 pour éviter des trous dans le graphique
cor_matrix[is.na(cor_matrix)] <- 0  

# Convertir la matrice en format long pour ggplot2
cor <- melt(cor_matrix)

# Tracer la matrice avec ggplot2
ggplot(cor, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") + 
  geom_text(aes(label = round(value, 2)), size = 4) +  # Affichage des valeurs
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", midpoint = 0) +
  labs(title = "Matrice de Corrélation binaire vs quantitative",
       x = "", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10))


           # Sélectionner les variables qualitatives et binaires
qual_vars <- Data[, sapply(Data, is.character)]  # Variables qualitatives (facteurs)
binary_vars <- Data[, sapply(Data, function(x) length(unique(x)) == 2 & is.numeric(x))]  # Variables binaires (0/1)
           
# Initialisation du tableau pour stocker les p-values du Chi²
chi2_results <- matrix(NA, ncol = ncol(binary_vars), nrow = ncol(qual_vars))
colnames(chi2_results) <- colnames(binary_vars)
rownames(chi2_results) <- colnames(qual_vars)
           
 # Boucle pour tester chaque combinaison Qualitative ↔ Binaire
for (i in 1:ncol(qual_vars)) {
  for (j in 1:ncol(binary_vars)) {
    tab <- table(qual_vars[, i], binary_vars[, j])  # Tableau de contingence
    chi2_results[i, j] <- chisq.test(tab)$p.value  # Test du Chi² et extraction de la p-value
  }
}         
# Remplacer les NA par 0 pour éviter des trous dans le graphique
chi2_results[is.na(chi2_results)] <- 0  

# Convertir la matrice en format long pour ggplot2
df_chi2 <- melt(chi2_results)

# Tracer la matrice avec ggplot2
ggplot(df_chi2, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") + 
  geom_text(aes(label = round(value, 2)), size = 4) +  # Affichage des valeurs
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", midpoint = 0) +
  labs(title = "Matrice de Corrélation Chi² (Binaires vs Qualitatives)",
       x = "", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10))
#Correlation quantitatives vs qualitatives


