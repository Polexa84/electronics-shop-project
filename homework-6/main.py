from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("../src/it.csv")
    # FileNotFoundError: Отсутствует файл it.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv("../src/items.csv")
    # InstantiateCSVError: Файл item.csv поврежден
