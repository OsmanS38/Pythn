#!/usr/bin/python3

# Eingabe
satz = input('Bitte geben Sie einen Satz ein: ')

# Verarbeitung
woerter = satz.split(' ')
anzahl_woerter = len(woerter)
anzahl_zeichen = len(satz)

# Aushabe
print(anzahl_woerter)
print(anzahl_zeichen)
print('Der Satz "' + satz + '" hat ' + str(anzahl_woerter) + ' Woerter und ' + str(anzahl_zeichen) + ' Zeichen')
print(f'Der Satz "{satz}" hat {anzahl_woerter} Woerter und {anzahl_zeichen} Zeichen')


