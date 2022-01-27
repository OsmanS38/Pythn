#!/usr/bin/python3

class Einkaufsliste():
    """
    Liste mit zu kaufenden Produkten
    """

    def __init__(self):
       self.mylist = list()

    def append(self,item=''):
        self.mylist.append(item)

    def show(self, action):
        counter = 0
        for item in self.mylist:
            if action is True:
                item.show(counter)
            else:
                item.show()
            counter += 1

    def remove(self, number):
        del(self.mylist[number])

    def modify(self, number=None, name='', price=0.0):
        if number is not None:
            self.mylist[number].modify(name=name, price=price)



