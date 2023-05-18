# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:56 2023

@author: matti
"""
import os
import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')

print("Requête 3 : Quels types de pages a le plus fréquenté une région ?")
print("Descriptif")
print("Les différentes régions sont :\n"
      "1.                      2.                         3.\n"
      "4.                      5.                         6.\n"
      "7.                      8.                         9.\n"
      "10.                     11.                        12.\n"
      "13.                     14.                        15.\n"
      "16.                     17.                        18.\n"
      "19.                     20.                        21.\n"
      "22.                     23.                        24.\n"
      "25.                     26.                        27.\n"
      "28.                     29.                        30.\n")
input("Saisissez le chiffre de la région que vous souhaitez analyser : ")
input("Il y a 20 types de pages. Saisissez le nombre de types de pages les plus fréquentés que vous souhaitez analyser : ")

print("\n\n 1. Dessiner un graphique"
      "2. Recommencer une analyser"
      "3. Retour au menu principal")
choixReq3 = input("Saisissez le chiffre de votre choix : ")

while choixReq3 not in lstChoixPossReq3 :
    print("Vous n'avez pas saisi une valeur correpondant à une question."
              "Veuillez adapter votre saisie en conséquence.\n\n")
    choixReq3 = input("Saisissez le chiffre de votre choix : ")
    
if choixReq3 == '1' :
    # Dessiner un graphique
elif choixReq3 == '2' :
    # Appeler la fonction
else :
    # Retour au menu principal
    import P2_Appli_MenuPrincipal as menuP 
