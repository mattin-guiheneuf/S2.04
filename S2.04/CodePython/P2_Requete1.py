# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:21 2023

@author: matti
"""

def requete1() :
    import matplotlib.pyplot as plt
    import os
    import pyodbc
    conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')
    cursor = conn.cursor()
    
    os.system('cls')
    print("Requête 1 : Quel est le nombre d'actions réalisés par type de pages ?\n")
    print("Cette requête compte le nombre d’actions par types de pages.\n")
    
    typePage = []
    nbrActions = []
    
    sql = """SELECT P.type_page, COUNT(ADV.Id_action) AS nbrActions
             FROM Pages P
             JOIN Actions A ON P.Id_page = A.idpage
             JOIN ActionsVisites ADV ON A.idaction = ADV.Id_action
             GROUP BY P.Type_page;"""  
             
    cursor.execute(sql)
    for row in cursor.fetchall():
        typePage.append(row[0])
        nbrActions.append(row[1])
        
    print(typePage, nbrActions)

    print("\n1. Dessiner un graphique\n"
          "2. Obtenir une analyse\n"
          "3. Retourner au menu principal\n")
    choixReq1 = input("Saisissez le chiffre de votre choix : ")
    
    lstChoixPossReq1 = ['1', '2', '3']
    
    while choixReq1 not in lstChoixPossReq1 :
        print("Vous n'avez pas saisi une valeur correpondant à une action. "
              "Veuillez adapter votre saisie en conséquence.\n")
        choixReq1 = input("Saisissez le chiffre de votre choix : ")
        
    if choixReq1 == '1' :
        # Dessiner un graphique
        plt.bar(typePage, nbrActions)
        plt.xlabel("Types de pages")
        plt.ylabel("Nombre d'actions")
        plt.title("Répartition des actions selon les types de pages")
        plt.show()
        
    elif choixReq1 == '2' :
        # Obtenir une analyse
        print("On peut remarquer que les types '..', '...' et '...' sont les plus fréquentés")
    else :
        # Retourner au menu principal
        import P2_MenuPrincipal as menuP
        menuP.menuPrincip()