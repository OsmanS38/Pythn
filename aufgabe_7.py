#!/usr/bin/python3

satz = input('Bitte geben Sie einen Satz ein: ')

woerter = satz.split()

for wort in woerter:
    wort =wort.upper()
#    print(wort.upper())
 
    print(wort.capitalize())

#result



