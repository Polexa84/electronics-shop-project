from src.phone import Phone
import pytest
"""Здесь написаны тесты с использованием pytest для модуля phone."""
# TasteCase№1
phn1 = Phone("iPhone 15 Pro Max", 120000.0, 3, 2)

def test_init():
    assert isinstance(phn1.name, str)
    assert phn1.name == "iPhone 15 Pro Max"
    assert isinstance(phn1.price, float)
    assert phn1.price == 120000.0
    assert isinstance(phn1.quantity, int)
    assert phn1.quantity == 3
    assert isinstance(phn1.number_of_sim, int)
    assert phn1.number_of_sim == 2
    try:
        phn1.number_of_sim = -1
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."

def test_repr_and_str():
    phn1.number_of_sim = 1
    assert str(phn1) == "iPhone 15 Pro Max"
    assert repr(phn1) == "Phone('iPhone 15 Pro Max', 120000.0, 3, 1)"
