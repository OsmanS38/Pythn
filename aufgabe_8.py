#!/usr/bin/python3

satz = input('Bitte geben Sie einen Satz ein: ')

woerter = satz.split(' ')

for wort in woerter:
    wort = wort.upper()
#    print(wort)
    line = ''
    for zeichen in wort:
        if line == '':
            line = zeichen
        else:
            line = line + ' ' + zeichen
    print(line)





