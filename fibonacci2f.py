#!/usr/bin/python3

Zahl =int( input('Wieviele Stellen sollen berechnet werden :'))

a = 0
b = 1
i = 0

list = []
list.append(0)
list.append(1)
output = ''
for teil in range(2,Zahl):
    result = a + b
    list.append(result)
    i += 1
    if output == '':
        output = f'0, 1, {result}'
    else:
        outout = f'{output}, {result}'
    a = b
    b = result
print(output)
print(list)




