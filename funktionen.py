#!/usr/bin/python3

#def zeige(variable):
#   print(variable)

#kurs = 'Dr.Heuer IT-Akademie'
#zeige(kurs)


def person(first ='Joe', last ='Doe'):
    print(f'{last},{first}')

person(last='Fred')

def is_int(value):
    try:
        return True, int(value)
#	 return True
    except:
        return False, value



while True:
    menge = input('Menge: ')
    exit_code, result = is_int(menge)
    print(exit_code)
    print(result)
#   if is_int(menge) is True:
#      print(is_int(menge))
#      break
