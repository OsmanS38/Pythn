#!/usr/bin/python3

ip = input('Geben Sie Ihre Ipv4 Adresse :')

oklet =ip.split('.')

#print(oklet)

list = {1,2,3,4,5,6,7,8,9}

if  len(ip) > 7  and len(ip) < 15:
    print('Ipv4 adress  gültig:')

elif len(oklet) !=4 :
    print('Ipv4 adress keine gültig:')

elif oklet < 0 and oklet > 255:
    print('Ipv4 adress keine gültig:')

else:
    print(f'Ipv4 adress keine gültig:')
