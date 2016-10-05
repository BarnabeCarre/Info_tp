#!/home/absolut/Documents/Prog/Python-3.5.2/
# -*-coding:Utf-8 -*
import math as mt

#------plus grande puissance pour obtenir un nombre x------#
def pgp (x,p):
	pgp = int(mt.log(x)/mt.log(p))
	return pgp

#-----factoriel d'un nombre x-----#
def fac(valeur):
    i = 0
    result = 1
    while i <valeur:
        result =(i+1)*result
        i += 1
    return result

#-----Donne les tables de multiplication de nb-----#
def tabmult(nb, mx = 10):
    i = 0
    while i < mx: # Tant que i est strictement inférieure à la variable max,
        print i + 1, "*", nb, "=", (i + 1) * nb
        i += 1
