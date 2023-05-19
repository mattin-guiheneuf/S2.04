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
          "intéressants et utiles, nous avons décidé de conserver uniquement les régions ayant réalisées au moins"
          "200 actions.\n")
    print("Les différentes régions sont :\n"
          "1. Allemagne              2. Andalucia                         3. Andorra\n"
          "4. Aragón                     5. Asturias                       6. Auvergne-Rhône-Alpes\n"
          "7. Balears, Illes                     8. Belgique                       9. Bourgogne-Franche-Comté\n"
          "10. Bretagne                    11. Canada                        12. Canarias\n"
          "13. Cantabria                     14. Castilla y León                        15. Castilla-La Mancha\n"
          "16. Cataluña                     17. Comunidad de Madrid                       18. Comunitat Valenciana\n"
          "19. Extremadura                     20. Galicia                        21. Grand Est\n"
          "22. Grande Bretagne                    23. Hauts de France                        24. Ile de France\n"
          "25. Italie                     26. La Rioja                        27. Navarra\n"
          "28. Normandie                     29. Nouvelle Aquitaine                        30. Occitanie\n"
          "31. País Vasco               32. Pays Bas 33. Pays de la Loire\n"
          "34. Portugal 35. Provence-Alpes-Côte d'Azur 36. Región de Murcia\n"
          "37. Suisse 38. USA\n" )

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