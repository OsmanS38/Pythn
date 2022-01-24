#!/usr/bin/python3

class produkte():

    produktliste=[{'produkt': 'apfel', 'menge': '2', 'preis': '2'},{'produkt': 'birne', 'menge': '3', 'preis': '3'}]

    def list():
        for item in produkte.produktliste:
            print(item)

    def listAdd():
        with open('produkte.txt','a') as fh:
            for produkt in produkte.produktliste:
                for item in produkt:
                    fh.write(item)

    def listWrite():
        with open('produkte.txt','w') as fh:
            for produkt in produkte.produktliste:
                #for a in produkt.items():
                fh.write(f'{str(produkt)} \n')
    def listRead():
        with open('produkte.txt','r') as fh:
            for produkt in fh.readlines():
                print('Read: ',produkt)

    def create (produkt,menge,preis):
        item={'produkt':produkt, 'menge': menge, 'preis':preis}
        produkte.produktliste.append(item)

    def delete():
        produkt = input('DeleteProdukt:')
        for item in produkte.produktliste:
            if item ['produkt'] == produkt:
                produkte.produktliste.remove(item)

    def modify ():
        modiProdukt=input('modifyProdukt:')
        for item in produkte.produktliste:
            if item ['produkt'] == modiProdukt:
                produkte.produktliste.remove(item)
        a=input('neues produkt:')
        b=input('neue menge:')
        c=input('neue preis:')
        produkte.create(a,b,c)



while True:
    print('creat:c')
    print('delete:d')
    print('modify:m')
    print('quit and print:q')
    action= input('action:')
    if action == 'c':
        print('*create*'*10)
        a=input('produkt:')
        b=input('menge:')
        c=input('preis:')
        produkte.create(a,b,c)
    elif action== 'd':
        print('*delete* '*10)
        produkte.delete()
    elif action == 'm':
        print('*modify*'*10)
        produkte.modify()
    elif action == 'q':
        print('*listWrite*'*10)
        produkte.listWrite()
        print('*txt.Read*'*10)
        produkte.listRead()
        print('**'*10)
        break



