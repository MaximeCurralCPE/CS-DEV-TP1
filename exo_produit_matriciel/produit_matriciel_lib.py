#TP1 CS-DEV
#24/11/20
#Maxime Curral

def multiplication(matrice_1,matrice_2):
    if len(matrice_1[0]) == len(matrice_2):
        matrice_resultat = []
        for i in range(len(matrice_1)):
            ligne = []
            for j in range(len(matrice_2[0])):
                valeur = 0
                for k in range(len(matrice_1[0])):
                    valeur += matrice_1[i][k] * matrice_2[k][j]
                ligne.append(valeur)
            matrice_resultat.append(ligne)
        return matrice_resultat
    else:
        return 'matrices incompatibles !'

def affichage(matrice):
    resultat = ''
    for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                resultat += '  ' + str(matrice[i][j]) + '  '
            resultat += '\n'
    return resultat