#!/usr/bin/python3

zahl = int(input('geben sie ein zahl :'))

zaehler = 0

if zahl > 1:
    for i in range(2,zahl):
       if(zahl % i) == 0:
          zaehler = zaehler + 1 
          break
          print(f'Zahl {zahl} ist keine primzahlen')
if zaehler == 0:
    print(f'Zahl {zahl} ist primzahlen')
else:
    print(f'Zahl {zahl} ist keine primzahlen')



