#!/home/absolut/Documents/Prog/Python-3.5.2/
# -*-coding:Utf-8 -*

import modperso as mp

#etape 0, on recupère le chiffre à traité

nbr10 = int(input("nombre en base 10 : "))
while nbr10 < 1:
	nbr10=int(input("il faut qu'il soit >= 1, nbr =? "))

#etape 1, on initialise toutes les variables ou chaines

nbr2 = []
n = mp.pgp(nbr10,2)		#plus grande puissance de nbr10 pour la base 2
debut = n
for i in range(0,n+1):		#nbr2 est une liste de n+1 valeurs
	nbr2.append(0)
nbr2[0] = 1			#le premier bit trouvé par la pgp est d'indice 0
nbrtemp = nbr10-(2**n) 		#ce qu'il reste à traité de nbr10

while nbrtemp != 0 : 		#s'arrette losqu'on a une valeur de n conforme
	n = mp.pgp(nbrtemp,2)
	nbrtemp = nbrtemp -(2**n)
	nbr2[debut - n] = 1	#le nouveau bit trouvé est d'indice début-n

print nbr10,"equivaut : ",nbr2
