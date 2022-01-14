#!/usr/bin/python3

#ip = '192.162.16.23'

# loop, jede ip adress
# loop, jedes oktett

###########################
#frage solange nach einer ip bis diese gueltig ist
state = None
while state is not True:
    state = None
    ip = input('Geben Sie eine IPv4 Adresse ein: ')
    oktetts = ip.split('.')
    if len(oktetts) == 4:

##########################
# hole ip Adresse
# nehme jedes Teil der Ip Adresse 
	for oktett in oktetts:
	    oktett in int(oktett)
            if oktett < 256 and oktett >= 0 and state is not False:
		state = True
	    else: 
