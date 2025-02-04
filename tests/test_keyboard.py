from src.keyboard import Keyboard
import pytest
"""Здесь написаны тесты с использованием pytest для модуля keyboard."""
# TasteCase№1
kb = Keyboard('Withe Project K9', 7600.0, 3)

def test_init():
    assert isinstance(kb.name, str)
    assert kb.name == 'Withe Project K9'
    assert isinstance(kb.price, float)
    assert kb.price == 7600.0
    assert isinstance(kb.quantity, int)
    assert kb.quantity == 3

def test_str():
    assert str(kb) == 'Withe Project K9'

def test_mix():
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
    try:
        kb.language = 'CH'
    except AttributeError:
        ...
    else:
        raise AssertionError("Expected AttributeError, but none was raised.")


