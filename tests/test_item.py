from src.item import Item
from src.phone import Phone

import pytest
"""Здесь написаны тесты с использованием pytest для модуля item."""
# TasteCase№1
def test_item():
    emp1 = Item("Телевизор",10000.0,10)
    assert isinstance(emp1.name, str)
    assert emp1.name == "Телевизор"
    assert isinstance(emp1.price, float)
    assert emp1.price == 10000.0
    assert isinstance(emp1.quantity, int)
    assert emp1.quantity == 10
    assert emp1 in Item.all

def test_calculate_total():
    Item.all.clear()  # Очищаем список, чтобы тесты были независимыми
    emp1 = Item("Фотоаппарат", 60000.0, 5)
    emp2 = Item("Модем", 1000.0, 13)
    assert emp1.calculate_total_price() == 300000
    assert emp2.calculate_total_price() == 13000
    assert len(Item.all) == 2

def test_apply_discount():
    # устанавливаем новый уровень цен
    Item.pay_rate = 0.6
    emp1 = Item("Дискета", 60.0, 100)
    emp2 = Item("Модем", 1000.0, 13)
    emp1.apply_discount()
    assert emp1.price == 36
    assert emp2.price == 1000.0

def test_setter_getter():
    emp1 = Item("ГиперМагнитофон", 60.0, 100)
    assert emp1.name == "ГиперМагнитофон"
    emp1.name = "ГиперМагнитофон"
    assert emp1.name == "ГиперМагни"
    assert len(emp1.name) == 10

def test_staticmethod():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('123.5') == 123
    assert Item.string_to_number('усу') == 0

def test_class_method():
    Item.all.clear()
    Item.instantiate_from_csv("../src/items.csv")
    assert len(Item.all) == 5
    item1 = Item.all[-1]
    assert item1.name == 'Мышка'

def test_repr_and_str():
    emp5 = Item("Телевизор",10000.0,10)
    assert repr(emp5) == "Item('Телевизор', 10000.0, 10)"
    assert str(emp5) == 'Телевизор'

def test_add():
    emp6 = Item("Телевизор",10000.0,10)
    phn1 = Phone("iPhone 16 Pro Max", 160_000, 3, 2)
    assert emp6 + phn1 == 13
    assert phn1 + phn1 == 6
    try:
        phn1 + 10
        assert False, "Ожидалось исключение ValueError, но оно не возникло."
    except ValueError as e:
        assert str(e) == 'Складывать можно только объекты Item и дочерние от них.'



















