# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:44 2023

@author: matti
"""
import os
import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')

print("Requête 2 : Quelle région a le plus visité chaque type de page pendant une saison ?")
print("Descriptif")
print("Les périodes possibles sont : Hiver, Printemps, Eté et Automne.")
print("Elles correspondent à : \n1. Hiver : 20 décembre au 20 mars\n2. Printemps : 21 mars au 21 juin\n3. Eté : 22 juin au 22 septembre\n4. Automne : 23 septembre au 19 décembre")
saison = input("Quelle saison voulez-vous analyser : ")
lstValPoss = [1, 2, 3, 4]
while saison not in lstValPoss :
    print("Vous n'avez pas saisi une valeur correpondant à une question."
          "Veuillez adapter votre saisie en conséquence.\n\n")
    saison = input("Quelle saison voulez-vous analyser : ")

if saison == '1' :
    dateDeb = '20/12/%% %'
    dateFin = '20/03/%% %'
elif saison == '2' :
    dateDeb = '21/03/%% %'
    dateFin = '21/06/%% %'
elif saison == '3' :
    dateDeb = '22/06/%% %'
    dateFin = '22/09/%% %'
else :
    dateDeb = '23/09/%% %'
    dateFin = '19/12/%% %'

sql = """
      """
param = (f'{dateDeb}%', f'{dateFin}%')
cursor.execute(sql, param)
for row in cursor.fetchall() :
    print(row)


print("\n\n 1. Dessiner un graphique"
      "2. Obtenir une analyse"
      "3. Analyser une autre saison"
      "4. Retourner au menu principal")
choixReq2 = input("Saisissez le chiffre de votre choix : ")

lstChoixPossReq2 = [1, 2, 3, 4]
    
while choixReq2 not in lstChoixPossReq2 :
    print("Vous n'avez pas saisi une valeur correpondant à une question."
              "Veuillez adapter votre saisie en conséquence.\n\n")
    choixReq2 = input("Saisissez le chiffre de votre choix : ")
        
if choixReq2 == '1' :
    # Dessiner un graphique
elif choixReq2 == '2' :
    # Obtenir une analyse
elif choixReq2 == '3'
    # Appeler la fonction r2
else :
    # Retourner au menu principal
    import P2_Appli_MenuPrincipal as menuP
