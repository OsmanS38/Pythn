#!/usr/bin/python3

# produkte = [ {'name': 'apfel', 'menge': 4, 'farbe': 'gruen'}, {'name': 'birne', 'menge': 3, 'preis': 3.4}, {'name': 'kiwi', 'menge': 6} ]

import os
import lib.item as item
os.system('clear')


#ding1 = item.Item()
#ding1.create(name='Fred', price=2)
ding1 = item.Item(name='Fred', price=2)


#ding2 = item.Item()
#ding2.create(name='Apfel', price=3)
ding2 = item.Item(name='Apfel', price=3)

ding1.show()
ding1.modify(name='Joe')
ding1.show()
ding1.name = 'Eva'
print(ding1.name)
ding1.show()
print(ding1.brutto)
print(ding2.brutto)
print(item.Item.brutto)


#
#action = ''
#while action != 'q':
#    print('#' * 30 )
#    print('[q]uit')
#    print('[e]inlesen der Produktliste')
#    print('[n]eu anlegen der Produktliste')
#    print('Produkte er[f]assen')
#    print('Produkte [l]oeschen')
#    print('Produkte [a]nzeigen')
#    print('Produkte [v]eraendern')
#    print('Produkte [s]peichern')
#    action = input('Waehlen Sie ein Aktion aus: ' )
#
#    # Daten einlesen
#    if action == 'e':
#        pass
#
#    # Daten anzeigen
#    if action == 'a':
#        pass
#
#    # neue Produktliste anlegen
#    if action == 'n':
#        pass
#
#    # Daten erfassen
#    if action == 'f':
#        pass
#
#    # Daten loeschen
#    if action == 'l':
#        pass
#
#    # Daten aendern
#    if action == 'v':
#        pass
#
#
#with open(produktliste, 'w') as fh:
#    for produkt in produkte:
#        fh.write(f'{produkt["name"]};{produkt["menge"]}\n')
#
