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


def test_pay_rate():
    object_1 = Item("Смартфон", 10000, 20)
    object_2 = Item("No Смартфон", 100, 666)

    object_1.pay_rate = 0.5
    object_1.apply_discount()

    assert object_1.price == 10000 * 0.5
    assert object_2.price == 100
    assert object_1.calculate_total_price() == (10000 * 0.5) * 20
    assert object_1.pay_rate == 0.5


def test_item_all():
    assert len(Item.all) == 0

    object_1 = Item("Смартфон", 10000, 20)
    assert len(Item.all) == 1

    object_2 = Item("No Смартфон", 100, 666)
    assert len(Item.all) == 2
    assert isinstance(Item.all, list)

    for value in Item.all:
        assert isinstance(value, object)
