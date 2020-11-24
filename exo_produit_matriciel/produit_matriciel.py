#TP1 CS-DEV
#24/11/20
#Maxime Curral

import produit_matriciel_lib as lib

A = [ [1,0,0,0] , [0,1,0,0] , [0,0,1,0] , [0,0,0,1] ]
B = [ [1,2,0] , [2,1,1] , [1,1,3] , [1,2,3] ]
C = lib.multiplication(A,B)

print(lib.affichage(C))