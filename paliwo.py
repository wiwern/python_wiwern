#!/bin/python3
print('''To jest program do
obliczania kosztu przejazdu autem''')
input()
print('Ile kosztuje paliwo za litr?')
c=input()
c=float(c)
print('Ile km przejechaliśmy?')
d=input()
d=float(d)
print('ile pali auto na 100km?')
l=input()
l=int(l)
dist=d/100
sp=dist*l
koszt=sp*c
print('''Przejechaliśmy %s km, spaliliśmy %s litrów,
kosztowało nas to %s złotych'''%(d,sp,koszt))

