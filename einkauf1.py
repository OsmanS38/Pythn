#!/usr/bin/python3


#produkte = [ 'apfel', 'birne', 'kiwi' ]
#menge = [ 4, 3, 6]
#
#counter = 0
#for produkt in produkte:
#    print(f'Produkt: {produkt}')
#    print(f'Menge: {menge[counter]}')
#    counter += 1

# produkte = [ {'name': 'apfel', 'menge': 4, 'farbe': 'gruen'}, {'name': 'birne', 'menge': 3, 'preis': 3.4}, {'name': 'kiwi', 'menge': 6} ]



############# Aktionen
#1 [e]inlesen der Produktliste
#2 Produkte er[f]assen
#3 Produkte [l]oeschen
#4 Produkte [a]nzeigen
#5 Produkte veraendern
#6 Program verlassen
#7 Produkte speichern
import os
os.system('clear')

produkte = list()
produktliste = 'produkte.txt'
action = ''
while action != 'q':
    print('#' * 30 )
    print('[q]uit')
    print('[e]inlesen der Produktliste')
    print('[n]eu anlegen der Produktliste')
    print('Produkte er[f]assen')
    print('Produkte [l]oeschen')
    print('Produkte [a]nzeigen')
    print('Produkte [v]eraendern')
    print('Produkte [s]peichern')
    action = input('Waehlen Sie ein Aktion aus: ' )

    # Daten einlesen
    if action == 'e':
        with open(produktliste, 'r') as fh:
            for line in fh.readlines():
                produkt, menge = line.split(';')
                print(f'{produkt} - {menge}')
                produkte.append({'name': produkt, 'menge': menge[0:-1]})
        os.system('clear')
        print('Daten geladen')

    # Daten anzeigen
    if action == 'a':
        for produkt in produkte:
            print(f'{produkt["name"]} ({produkt["menge"]})')

    # neue Produktliste anlegen
    if action == 'n':
        with open(produktliste, 'w') as fh:
            print('neue Produktliste angelegt')
#            pass

    # Daten erfassen
    if action == 'f':
        produkt = input('Welches Produkt soll erfasst werden: ')
        menge = input('Geben Sie die Menge an: ')
        produkte.append({'name': produkt, 'menge': menge})
        os.system('clear')
        print('Daten geladen')

    # Daten loeschen
    if action == 'l':
        counter = 0
        os.system('clear')
        for produkt in produkte:
            print(f'[{counter}] {produkt["name"]} ({produkt["menge"]})')
            counter += 1
        subaction = input('Welches Produkt moechten Sie loeschen: ')
        del(produkte[int(subaction)])

    # Daten aendern
    if action == 'v':
        counter = 0
        os.system('clear')
        for produkt in produkte:
            print(f'[{counter}] {produkt["name"]} ({produkt["menge"]})')
            counter += 1
        subaction = input('Welches Produkt moechten Sie aendern: ')
        produkte[int(subaction)]['menge'] = input('Geben Sie die neue Menge an: ')


with open(produktliste, 'w') as fh:
    for produkt in produkte:
        fh.write(f'{produkt["name"]};{produkt["menge"]}\n')


#weiter = True
#while weiter is True:
#    produkt = input('Geben Sie ein Produkt an: ')
#    menge = input('Geben Sie die Menge an: ')
#    produkte.append({'name': produkt, 'menge': menge})
#    action = input('fuer fertig "j" druecken: ')
#with open('produkte.txt', 'a') as fh:
#    fh.write(f'{produkt};{menge}\n')
#    if action == 'j':
#        weiter = False
#    
#for produkt in produkte:
#    print(f'Name: {produkt["name"]} - Menge: {produkt["menge"]}')
#
#with open('produkte.txt', 'r') as fh:
#    for line in fh.readlines():
#        print(line)

