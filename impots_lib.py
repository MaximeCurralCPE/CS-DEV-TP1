#TP1 CS-DEV
#24/11/20
#Maxime Curral

def mes_impots(revenu):
    revenu = int(revenu)
    impots = 0
    if revenu > 156244:
        impots += (revenu - 156244) * 0.45
        impots += (156244 - 73779) * 0.41
        impots += (73779 - 27519) * 0.3
        impots += (27519 - 9964) * 0.14 
    if revenu > 73779 and revenu <= 156244:
        impots += (revenu - 73779) * 0.41
        impots += (73779 - 27519) * 0.3
        impots += (27519 - 9964) * 0.14 
    if revenu > 27519 and revenu <= 73779:
        impots += (revenu - 27519) * 0.3
        impots += (27519 - 9964) * 0.14 
    if revenu > 9964 and revenu <= 27519:
        impots += (revenu - 9964) * 0.14
    return str(impots)
    
