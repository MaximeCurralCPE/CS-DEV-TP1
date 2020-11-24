#TP1 CS-DEV
#24/11/20
#Maxime Curral

import impots_lib as lib

revenu=input("entrez votre revenu annuel")
print("vous devez payer " + lib.mes_impots(revenu) + "€ en impôts cette année")