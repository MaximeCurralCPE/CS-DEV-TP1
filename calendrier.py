#TP1 CS-DEV
#24/11/20
#Maxime Curral

import calendrier_bibliothèque as lib

#question 1
print("question 1 :",lib.test_bissextile(2020))

#question 2
print("question 2 :",lib.nombre_jours(11,2020))

#question 3
print("question 3 :",lib.check_date('21/12/2012'))

#question 4
print("question 4 :")
print("Bonjour, veuillez suivre les instructions à l'écran pour vérifier si votre date existe :")
jour = input("  entrez le jour sous forme de nombre entier :")
mois = input("  entrez le mois sous forme de nombre entier :")
annee = input("  entrez l'année sous forme de nombre entier :")
if lib.check_date(jour + '/' + mois + '/' + annee) == True:
    print("date valide")
else :
    print("date non valide")
