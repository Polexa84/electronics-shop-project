from src.item import Item
import pytest
"""Здесь надо написаны тесты с использованием pytest для модуля item."""
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








