#!/usr/bin/python3

obst =[]
gemueze =[] 
list =[]

a ={'name':[], 'menge':[], 'preis':[]}

#b =list(a.werke())

while True:
    neu_dinge = input('Geben Sie ein Obst ,Gemueze:') 
     #(wenn hat in list:q)')
    if neu_dinge not in list:
        list += [neu_dinge]
        print(list)
    else:
        print('Diese sache haben Sie doch!')

