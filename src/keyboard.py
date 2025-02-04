from src.item import Item

#Реализуем подмешивания в дочерний класс
class MixinLog:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def __str__(self):
        return f'{self._language}'

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"


#Создаем новый класс для товара "Клавиатура" с наследованием от Item
class Keyboard(Item, MixinLog):

    #Инициализируем и берем данные из родительского класса
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def __str__(self):
        return f'{self.name}'

