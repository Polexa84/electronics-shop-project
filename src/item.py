import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity

        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) >= 10:
            self.__name = name[:10]
        else:
             self.__name = name

    @staticmethod
    def string_to_number(value: str):
        """
        Преобразует строку в число.
        """
        try:
            return int(float(value))
        except ValueError:
            return 0


    @classmethod
    def instantiate_from_csv(cls, file):
        """
        Инициализирующий экземпляры класса `Item` данными из файла items.csv
        """
        try:
            with open(file, encoding="utf-8") as list:
                goods = csv.DictReader(list)

                for good in goods:
                    try:
                        name = good["name"]
                        price = float(good['price'])
                        quantity = int(good['quantity'])
                        cls(name, price, quantity)
                    except KeyError:
                        print(f"InstantiateCSVError: Файл {file} поврежден")
                    except ValueError:
                        print(f"InstantiateCSVError: Файл {file} поврежден")

        except FileNotFoundError:
            print(f"FileNotFoundError: Отсутствует файл {file}")


class InstantiateCSVError(Exception): # Все равно нужно определение, хотя оно и не используется
    pass