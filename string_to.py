#!/usr/bin/python3


eingabe = input('Machen Sie eine Eingabe:')

def string_to_int(my_string):
    try:
        return True, int(my_string)
    except:
        return False, my_string

def string_to_float(my_string):
     try:
         return True, float(my_string)
     except:
         return False, my_string


result1 , data= string_to_int(eingabe)
if result1 is True:
    print('Eingabe war ein INT')
    print(data)

result2, data= string_to_float(eingabe)
if result2 is True:
    print('Eingabe war ein FLOAT')
    print(data)
