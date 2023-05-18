# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:21 2023

@author: matti
"""
import os
import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')
cursor = conn.cursor()

def requete1() :
    os.system('cls')
    print("Requête 1 : Quel est le nombre d'actions réalisés par type de pages ?\n")
    print("Descriptif\n")
    
    sql = """SELECT P.type_page, COUNT(ADV.Id_action) AS nbrActions
             FROM Pages P
             JOIN Actions A ON P.Id_page = A.idpage
             JOIN ActionsVisites ADV ON A.idaction = ADV.Id_action
             GROUP BY P.Type_page;"""        
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)



    print("\n1. Dessiner un graphique\n"
          "2. Obtenir une analyse\n"
          "3. Retourner au menu principal\n")
    choixReq1 = input("Saisissez le chiffre de votre choix : ")
    
    lstChoixPossReq1 = ['1', '2', '3']
    
    while choixReq1 not in lstChoixPossReq1 :
        print("Vous n'avez pas saisi une valeur correpondant à une question. "
              "Veuillez adapter votre saisie en conséquence.\n")
        choixReq1 = input("Saisissez le chiffre de votre choix : ")
        
    if choixReq1 == '1' :
        # Dessiner un graphique
        print('Test1')
    elif choixReq1 == '2' :
        # Obtenir une analyse
        print('Test2')
    else :
        # Retourner au menu principal
        import P2_Appli_MenuPrincipal as menuP
        menuP.menuPrincip()