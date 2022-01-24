#!/usr/bin/python3

class Item():
    brutto = 1
    tax = 0.19

    def __init__(self, name='', price=0):
        if name == '':
            print('Eigenschaft "name" fehlt')
        if price == 0:
            print('Eigenschaft "price" fehlt')

        self.price = price * 2
        self.brutto = int(self.price) * (Item.tax + 1)
        self.name = self.set_name(name=name)

    def modify(self, name='', price=0):
        if name:
            self.name = self.set_name(name=name)
        if price != 0:
            self.price = price
            self.brutto = int(self.price) * (Item.tax + 1)

    def set_name(self, name=''):
        self.name = name.upper()

    def delete(self):
        pass

    def save(self):
        pass

    def show(self):
        print(f'Name: {self.name}')
        print(f'Brutto: {Item.brutto}')

