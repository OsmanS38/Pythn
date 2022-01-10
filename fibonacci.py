#!/usr/bin/python3

Zahl =int( input('Wieviele Stellen sollen berechnet werden :'))

a = 0
b = 1

i = 0

while i<= Zahl:
    result = a + b
    i = i + 1
#   i += 1
    print(f'Durchlauf : {i}: result :{result}')
    a = b
    b = result
