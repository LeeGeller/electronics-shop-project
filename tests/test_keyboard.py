from src.item import Item
from src.keyboard import Keyboard, Mixin


def test_class():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)

    assert isinstance(Keyboard, object)
    assert issubclass(Keyboard, Item)
    assert issubclass(Keyboard, Mixin)
    assert str(keyboard) == "Dark Proje"
