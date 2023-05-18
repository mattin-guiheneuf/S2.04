# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:56 2023

@author: matti
"""
import os
import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')

def requete3() :
    os.system('cls')
    print("Requête 3 : Quels types de pages a le plus fréquenté une région ?")
    print("Cette requête affiche, pour une région que vous devez saisir, les x types de pages les plus fréquentés"
          "et le nombre d’actions effectuées.\n")
    print("On compte dans notre base de données ... régions différentes. Pour garder les échantillons les plus"
          "intéressants et utiles, nous avons décidé de conserver uniquement les régions ayant effectuées au moins"
          "... actions.\n")
    print("Les différentes régions sont :\n"
          "1. Galicia              2.'Danemark                         3.\n"
          "4.                      5.                         6.\n"
          "7.                      8.                         9.\n"
          "10.                     11.                        12.\n"
          "13.                     14.                        15.\n"
          "16.                     17.                        18.\n"
          "19.                     20.                        21.\n"
          "22.                     23.                        24.\n"
          "25.                     26.                        27.\n"
          "28.                     29.                        30.\n")
      """   'Galicia', 'Danemark', 'País Vasco', 'Región de Murcia',
           "Côte d'Ivoire", 'Nouvelle Aquitaine', 'Cataluña', 'Ile de France',
           'Aragón', 'Irlande', 'Occitanie', 'Canarias', 'Andalucía',
           'Suisse', 'Corse', 'Maroc', 'Castilla y León', 'Mexique',
           'Castilla-La Mancha', 'Allemagne', 'Comunitat Valenciana',
           'Hauts de France', "Provence-Alpes-Côte d'Azur", 'Balears, Illes',
           'Auvergne-Rhône-Alpes', 'Portugal', 'Comunidad de Madrid',
           'La Rioja', 'Grande Bretagne', 'Bretagne', 'Pays de la Loire',
           'Kazakhstan ', 'Extremadura', 'Pays Bas', 'Suède', 'Belgique',
           'Asturias', 'USA', 'Andorra', 'Pologne', 'Brésil', 'Madagascar',
           'Lithuanie', 'Bourgogne-Franche-Comté', 'Grand Est', 'Italie',
           'Navarra', 'Nouvelle Zélande', 'Normandie', 'Equateur',
           'Guadeloupe', 'Inde', 'Brunei', 'Cantabria', 'Russie', 'Chine',
           'Algérie', 'Roumanie', 'Canada', 'Luxembourg', 'Norvège', 'Malte',
           'Colombie', 'Croatie', 'Slovaquie', 'Australie',
           'République Tchèque', 'Hongrie', 'Argentine', 'Corée du Sud',
           'Panama', 'Afrique du Sud', 'Pérou', 'Turquie', 'Ceuta y Melilla',
           'Grèce', 'Nicaragua', 'Cuba', 'Venezuela', 'Bolivie', 'Sri Lanka',
           'Sénégal', 'Syrie', 'Tanzanie', 'Qatar', 'Chypre', 'Honduras',
           'Polynésie Française', 'Israël', 'Autriche', 'Guatemala', 'Chili',
           'Viet Nam', 'Finlande', 'Indonésie', 'Egypte', 'Lettonie',
           'Ukraine', 'Uruguay', 'Gabon', 'Singapour', 'Guinée équatoriale',
           'Biélorussie', 'Somalie', 'Kenya', 'Monaco', 'Oman', 'Hong-Kong',
           'Guyanne', 'Islande', 'Arabie Saoudite', 'La Réunion',
           'Costa Rica', 'Porto Rico', 'Salvador', 'République Dominicaine',
           'Macédoine', 'Bulgarie', 'Grenade', 'Malaysie', 'Iran', 'Estonie',
           'Géorgie', 'Albanie', 'Mali', 'Taïwan'
           """
    input("Saisissez le chiffre de la région que vous souhaitez analyser : ")
    input("Il y a 20 types de pages. Saisissez le nombre de types de pages les plus fréquentés que vous souhaitez analyser : ")

    print("Résultat Requête")    

    print("\n\n 1. Dessiner un graphique"
          "2. Recommencer une analyser"
          "3. Retour au menu principal")
    choixReq3 = input("Saisissez le chiffre de votre choix : ")

    lstChoixPossReq3 = ['1', '2', '3']

    while choixReq3 not in lstChoixPossReq3 :
        print("Vous n'avez pas saisi une valeur correpondant à une question."
              "Veuillez adapter votre saisie en conséquence.\n\n")
        choixReq3 = input("Saisissez le chiffre de votre choix : ")
    
    if choixReq3 == '1' :
        # Dessiner un graphique
        print('Test1')
    elif choixReq3 == '2' :
        # Effectuer une autre analyse
        requete3()
    else :
        # Retour au menu principal
        import P2_Appli_MenuPrincipal as menuP 
        menuP.menuPrincip()