#!/usr/bin/python3

# import
import os
import lib.item as item
import lib.einkaufsliste as mylist
#loesche Bildschirm
os.system('clear')
#import json


# erzeuge einen einkaufwagen
einkaufwagen = mylist.Einkaufsliste()

###########################################
# erzeuge ein Objekt
apfel = item.Item(name='Apfel', price=0.45)
apfel.modify(price=0.55)
birne = item.Item(name='Birne', price=1.25)
kiwi = item.Item(name='Kiwi', price=0.35)
einkaufwagen.append(apfel)
einkaufwagen.append(birne)
einkaufwagen.append(kiwi)
############################



#main loop, Haupschlife
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
        os.system('clear')
        file = input('Aus welcher Datei sollen die Daten geladen werden: ')
        einkaufwagen.import_data(file)

    # Daten anzeigen
    if action == 'a':
        einkaufwagen.show(True)

    # neue einkaufwagen anlegen
    if action == 'n':
        einkaufwagen = mylist.Einkaufsliste()

    # Daten erfassen
    if action == 'f':
        os.system('clear')
        myname = input('Was wollen Sie kaufen:')
        myprice =input('Was kostet das :')
        product = item.Item(name=myname, price=myprice)
        einkaufwagen.append(product)

    # Daten loeschen
    if action == 'l':
        einkaufwagen.show(True)
        number = int(input('Was wollen Sie loeschen:'))
        einkaufwagen.remove(number)
        os.system('clear')

    # Daten aendern
    if action == 'v':
        einkaufwagen.show(True)
        number = int(input('Was wollen Sie aendern:'))
        name = input('Wie soll der neu Name lauten [ENTER fuer alten Wert belassen]')
        price = input('Wie ist der neu Preis [ENTER fuer alten Wert belassen]')
        einkaufwagen.modify(number=number, name=name, price=price)

    # Daten speichern
    if action == 's':
       einkaufwwagen.save()



#with open('products.json') as fh

#with open(produktliste, 'w') as fh:
#    for produkt in produkte:
#        fh.write(f'{produkt["name"]};{produkt["menge"]}\n')

