from src.item import Item


def test_init_object_item():
    object_1 = Item("Смартфон", 10000, 20)
    assert object_1.name == "Смартфон"
    assert object_1.price == 10000
    assert object_1.quantity == 20

def test_sum_total_price():
    object_1 = Item("Смартфон", 10000, 20)
    object_2 = Item("No Смартфон", 100, 666)

    assert object_1.calculate_total_price() == 10000 * 20
    assert object_2.calculate_total_price() == 100 * 666