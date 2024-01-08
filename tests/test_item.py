from src.item import Item


def test_init_object_item():
    object_1 = Item("Смартфон", 10000, 20)
    assert object_1.name == "Смартфон"