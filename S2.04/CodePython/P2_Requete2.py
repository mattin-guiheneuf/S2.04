# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:44 2023

@author: matti
"""
def requete2():
    import matplotlib.pyplot as plt
    import os
    import pyodbc
    conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')
    cursor = conn.cursor()
    
    os.system('cls')
    print("Requête 2 : Quelle région a le plus visité chaque type de page pendant une saison ?")
    print("Cette requête nous montre les régions qui ont le plus visité chaque type de pages avec le "
          "nombre d’actions correspondant, sur une période x que vous devez saisir (exprimée en saison).\n")
    print("Les périodes possibles sont donc : Hiver, Printemps, Eté et Automne.\n")
    print("Elles correspondent à : \n1. Hiver : Décembre, Janvier et Février\n2. Printemps : Mars, Avril et Mai\n"
          "3. Eté : Juin, Juillet et Août\n4. Automne : Septembre, Octobre et Novembre\n")
    saison = input("Quelle saison voulez-vous analyser : ")

    lstValPoss = ['1', '2', '3', '4']

    while saison not in lstValPoss :
        print("Vous n'avez pas saisi une valeur correpondant à une saison."
              "Veuillez adapter votre saisie en conséquence.\n\n")
        saison = input("Quelle saison voulez-vous analyser : ")

    typePage = []
    region = []
    nbrActions = []
    
    if saison == '1' :
        sql = """SELECT ActRegionHiver.Type_page AS TypePage, ActRegionHiver.Region1 AS Region, MaxActPageHiver.nbrActMax AS NombreActions
                 FROM ActRegionHiver
                 JOIN MaxActPageHiver ON ActRegionHiver.Type_page = MaxActPageHiver.Type_page
                 WHERE MaxActPageHiver.nbrActMax = ActRegionHiver.nbrActions
                 GROUP BY TypePage, Region;"""
    elif saison == '2' :
        sql = """SELECT ActRegionPrintemps.Type_page AS TypePage, ActRegionPrintemps.Region1 AS Region, MaxActPagePrintemps.nbrActMax AS NombreActions
                 FROM ActRegionPrintemps
                 JOIN MaxActPagePrintemps ON ActRegionPrintemps.Type_page = MaxActPagePrintemps.Type_page
                 WHERE MaxActPagePrintemps.nbrActMax = ActRegionPrintemps.nbrActions
                 GROUP BY TypePage, Region;"""
    elif saison == '3' :
        sql = """SELECT ActRegionEte.Type_page AS TypePage, ActRegionEte.Region1 AS Region, MaxActPageEte.nbrActMax AS NombreActions
                 FROM ActRegionEte
                 JOIN MaxActPageEte ON ActRegionEte.Type_page = MaxActPageEte.Type_page
                 WHERE MaxActPageEte.nbrActMax = ActRegionEte.nbrActions
                 GROUP BY TypePage, Region;"""
    else :
        sql = """SELECT ActRegionAutomne.Type_page AS TypePage, ActRegionAutomne.Region1 AS Region, MaxActPageAutomne.nbrActMax AS NombreActions
                 FROM ActRegionAutomne
                 JOIN MaxActPageAutomne ON ActRegionAutomne.Type_page = MaxActPageAutomne.Type_page
                 WHERE MaxActPageAutomne.nbrActMax = ActRegionAutomne.nbrActions
                 GROUP BY TypePage, Region;"""

    cursor.execute(sql)
    for row in cursor.fetchall() :
        typePage.append(row[0])
        region.append(row[1])
        nbrActions.append(row[2])
        
    print(typePage, region, nbrActions)

    print("\n\n1. Obtenir une analyse"
          "2. Analyser une autre saison"
          "3. Retourner au menu principal")
    choixReq2 = input("Saisissez le chiffre de votre choix : ")

    lstChoixPossReq2 = ['1', '2', '3']
    
    while choixReq2 not in lstChoixPossReq2 :
        print("Vous n'avez pas saisi une valeur correpondant à une action."
              "Veuillez adapter votre saisie en conséquence.\n\n")
        choixReq2 = input("Saisissez le chiffre de votre choix : ")
        
    if choixReq2 == '1' :
        # Obtenir une analyse
        if saison == '1' :
            print("")
        elif saison == '2' :
            print("")
        elif saison == '3' :
            print("")
        else :
            print("")
            
    elif choixReq2 == '2' :
        # Appeler la fonction r2
        requete2()
    else :
        # Retourner au menu principal
        import P2_MenuPrincipal as menuP
        menuP.menuPrincip()
