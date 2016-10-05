#!/home/absolut/Documents/Prog/Python-3.5.2/
# -*-coding:Utf-8 -*

from math import *

nbr_10 = int(input("nombre à convertir : "))
nbr_2=[]
reste = nbr_10
while reste != 1 :
	nbr_2.append(reste%2)
	reste = reste // 2
nbr_2.append(1)
nbr_2.reverse()
print nbr_2
