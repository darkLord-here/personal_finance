import unittest
from personal_finance import core, ui

def test_core():
    assert (720000, 3413182, 68263640, 85329550, 170659100, 20427216) == core.calculate_fire(60000, 27, 50, 0.07)


def test_ui():
    assert True == ui.show_fire()