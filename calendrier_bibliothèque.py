#TP1 CS-DEV
#24/11/20
#Maxime Curral

def test_bissextile(annee):
    #une année est bissextile si elle est divisible par 4 et ne termine pas par 00
    #cette fonction teste ces deux conditions et renvoie True si l'année est bissextile.
    if str(annee)[-2:] != 0 and int(annee) % 4 == 0:
        return True
    else:
        return False
def check_date(date):
    jour,mois,annee = map(int, date.split('/'))
    if jour > 0:
        if annee >= 0:
            if mois >= 1 and mois <= 12:
                if mois == 2 and test_bissextile(annee) == True and jour <= 29:
                    return True
                elif mois == 2 and test_bissextile(annee) == False and jour <= 28:
                    return True
                elif mois in [1,3,5,7,8,10,12] and jour <= 31:
                    return True
                elif mois in [4,6,9,11] and jour <= 30:
                    return True
    else:
        return False

def nombre_jours(mois,annee):
    #vérifie si le mois donné en entrée existe
    #s'il existe, retourne le nombre de jours de ce mois
    if mois in [1,3,5,7,8,10,12]:
        return 31
    elif mois in [4,6,9,11]:
        return 30
    elif mois == 2:
        if test_bissextile(annee) == True:
            return 29
        else:
            return 28
    else:
        return False
