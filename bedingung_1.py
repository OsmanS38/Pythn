#!/usr/bin/python3

zahl = input('Bitte geben Sie eine Zahl ein: ')

# 2, 12, 10, -2, -12
if int(zahl) > 10:
    print('Die Zahl ist groesser als 10')
elif int(zahl) == 10:
    print('Die Zahl ist gleich 10')
elif int(zahl) < 10:
    print('Die Zahl ist kleiner als 10')
else:
    print('Die Eingabe ist nicht vom Typ Integer')


