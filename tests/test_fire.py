import unittest
from . import core, ui

def test_core():
    assert True == core.fire.calculate_fire()


def test_ui():
    assert True == ui.show_fire()