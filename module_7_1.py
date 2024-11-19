from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):                          # возвращает строку в формате '<название>, <вес>, <категория>'
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'           # Инкапсулированный атрибут

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')          # чтение всей информации из файла
        products = file.read()                      # чтение файла
        file.close()                                # закрытие файла
        return products

    def add(self, *products):                       # Добавляет в файл __file_name каждый продукт из products
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in self.get_products():
                file.write(str(i) + '\n')      # Добавление значения с переносом строки
            else:
                print(f'Продукт {str(i)} уже есть в магазине')
        file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
