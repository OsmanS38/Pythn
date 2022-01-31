#!/usr/bin/python3

class Einkaufsliste():
    """
    Liste mit zu kaufenden Produkten
    """

    def __init__(self):
       """
       Initalisiert eıne Liste aus Objekten

       @retuen: void
       """
       self.mylist = list()
       self.file = ''

    def append(self,item=''):
        """
        Fuegt ein Objekt Item an die Liste an.

        @param: item (objekt) ein Produkt 
        @return: void 
        """
        self.mylist.append(item)

    def show(self, action):
        """
        Zeigt den Inhalt der mıt oder ohne Nummerierung Liste an.

        @param: action (bool) Soll nummeriert werden 
        @return: void
        """
        counter = 0
        for item in self.mylist:
            if action is True:
                item.show(counter)
            else:
                item.show()
            counter += 1

    def import_data(self):
        """
        Importiert Daten und ruft dafuer import_json oder import_csv auf.

        @param: file (str) Datei die eingelesen werden soll
        @return: void  
        """
        self.file = file 
        suffix = file.split('.').pop()
        if suffix == 'json':
            self.import_json()
        if suffix =='csv':
            self.import_csv()

    def import_json(self, file):
        """
        Importiert den Inhalt einer json Datei in mylist.

        @return: void 
        """
        pass

    def import_csv(self, file):
        """
        Importiert den Inhalt einer json Datei in mylist.

        @return: void
        """
        pass

    def remove(self, number):
        """
        Entfern ein Element aus der Liste.

        @param: number (int) Index des zu entfernenden Elementes 
        @return: void 
        """
        del(self.mylist[number])

    def modify(self, number=None, name='', price=0.0):
        """
        Entfern ein Element aus der Liste.

        @param: number (int) Index des zu entfernenden Elementes
        @return: void
        """
        if number is not None:
            self.mylist[number].modify(name=name, price=price)



