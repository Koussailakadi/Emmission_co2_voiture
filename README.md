# Emmission_co2_voiture
Génie logiciel et data

# Etapes :
1. Extraction automatique des données 
2. filtrage de la base de données
3. creation automatique de la base de données via un script : database_sql.sql dans le dossier DATA_BASE_CSV la fonction drop()
4. sauvegarde de données dans des tables avec une manière automatique avec un code python : create_database()

# service: 
1. on propose 20 services
2. requettes complexe: des jointure doubles et tripes , group by, destinct, avg, max, la moyenne avec une somme. 
3. pour voir les résultas, je vous prie de bien voir sur le fichier notebook : https://github.com/Koussailakadi/Emmission_co2_voiture/blob/master/CO2_Emmissions.ipynb

# Base de données brute:
1. fichier csv avec 55000 lignes environ et 26 colonnes. https://github.com/Koussailakadi/Emmission_co2_voiture/blob/master/mars-2014-complete.csv
2. aussin un fichier avec les descriptions de chaque colonne. https://github.com/Koussailakadi/Emmission_co2_voiture/blob/master/carlab-annuaire-variable.xlsx

# Dossier DATA_BASE_csv:
1. on a stocké toutes les valeurs correspondantes à chaque table dans un fichier csv séparé avec comme nom du fichier le nom de la table, pour faciliter la lecture des données et d'éviter de parcourire à chaque fois la base de données brute.

