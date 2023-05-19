# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:50:44 2023

@author: matti
"""
import os
import pyodbc
conn = pyodbc.connect('DSN=BD_Guiheneuf_Lakartxela')

def requete2():
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
        print("Vous n'avez pas saisi une valeur correpondant à une question."
              "Veuillez adapter votre saisie en conséquence.\n\n")
        saison = input("Quelle saison voulez-vous analyser : ")


    """
    sql = 
          
    param = (f'{dateDeb}%', f'{dateFin}%')
    cursor.execute(sql, param)
    for row in cursor.fetchall() :
        print(row)
    """
    
    print("Résultat Requête")

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
        print('Test1')
    elif choixReq2 == '2' :
        # Obtenir une analyse
        print('Test2')
    elif choixReq2 == '3' :
        # Appeler la fonction r2
        requete2()
    else :
        # Retourner au menu principal
        import P2_Appli_MenuPrincipal as menuP
        menuP.menuPrincip()
