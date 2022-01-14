#!/usr/bin/python3

zahl = int(input('geben sie ein zahl :'))

zahl1 = 1
zahl2 = 999


for zahl in range(zahl1, zahl2 + 1):
    if zahl > 1:
        for i in range(2,zahl):
            if(zahl % i) == 0:
                break
        else:
            print(zahl)

