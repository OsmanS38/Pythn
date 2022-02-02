#!/usr/bin/python3

class Item():

    # Klasseneigenschaft
    tax = 0.19

    def __init__(self, name='', price=0.0):
        """
        Initialisiert ein Object und belegt dabei die Objekteigenschaften mit Werten

        @param: name (str) Name des Produktes
        @param: price (float) Preis eines Produktes
        @return: void
        """
        try:
           price = float(price)
        except:
            print('Eingabe kann nicht in ein float umgewandelt werden.')
        if name == '':
            print('Eigenschaft "name" fehlt')
        if price <= 0:
            print('Eigenschaft "price" fehlt')
        self.set_name(name=name)
        self.set_price(price=price)

    def modify(self, name='', price=0.0):
        """
        Modifiziert die Objekteigenschaften

        @param: name (str) Name des Produktes
        @param: price (float) Preis eines Produktes
        @return: void
        """
        if name != '':
            self.set_name(name=name)
        if price != 0.0:
            self.set_price(price=price)

    def set_name(self, name=''):
        """
        Modifiziert die Objekteigenschaft name

        @param: name (str) Name des Produktes
        @return: void
        """
        self.name = name

    def set_price(self, price=0.0):
        """
        Modifiziert die Objekteigenschaft price

        @param: price (float) Preis eines Produktes
        @return: void
        """
        self.price = float(price)
        self.brutto = int(self.price) * (Item.tax + 1)


    def show(self,counter=None):
        """
        Zeigt alle Objekteigenschaften an

        @param: counter (int) zahler zur Objektauswahl
        @return: void
        """
        if counter is None:
            print(f'Name: {self.name}')
            print(f'Preis: {self.price}')
        else:
            print(f'[{counter}] {self.name}')

    def get_data(self):
        """
        Liefert alle Objekteigenschaften zurueck

        @return: (dict)
        """
        return { 'name': self.name, 'price': self.price }
