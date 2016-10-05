#!/home/absolut/Documents/Prog/Python-3.5.2/
# -*-coding:Utf-8 -*

from math import *

nbr_b = str(input("nbr à traiter : "))
b = int(input("base du nombre : "))

nbr_carac = len(nbr_b) #nombre de symbole
nbr_10= 0 #solution recherché

for i in range(nbr_carac,0,-1):
	nbr_10 = nbr_10 + pow(b,i-1)*int(nbr_b[nbr_carac -i])
			  #poid * valeur
print "------------------------------------------------------------"
print "resultat en base 10: ", int(nbr_10)
