# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:48:39 2023

@author: mguiheneuf
"""

import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')


import sys
import os



print("Menu Principal\n"
      "1. Quel est le nombre d'actions réalisés par type de pages ?\n"
      "2. Quelle région a le plus visité chaque type de page pendant une saison ?\n"
      "3. Quels types de pages a le plus fréquenté une région ?\n")

choix = input("Saisissez le chiffre de votre choix : ")

lstChoixPoss = ['1', '2', '3']

while choix not in lstChoixPoss :
    print("Vous n'avez pas saisi une valeur correpondant à une question. "
          "Veuillez adapter votre saisie en conséquence.\n\n")
    choix = input("Saisissez le chiffre de votre choix : ")
    
if choix == '1' :
    # Importer le fichier de la Requête 1
    # import P2_Appli_Requete1 as r1
    print('Test1')
elif choix == '2' :
    # Importer le fichier de la Requête 2
    # import P2_Appli_Requete2 as r2
    print('Test2')
else :
    # Importer le fichier de la Requête 3
    # import P2_Appli_Requete3 as r3
    print('Test3')
