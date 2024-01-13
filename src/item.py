import csv
import pathlib


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(Item)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        return self.price with discount
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Get name
        """
        return f"{self.__name}"

    @name.setter
    def name(self, name: str) -> None:
        """
        Inout new name
        """
        self.__name = str(name).strip()[:10].capitalize()

    @classmethod
    def instantiate_from_csv(cls, path_file: str) -> None:
        """
        Get csv file and create 5 classes
        """
        cls.all.clear()
        with open(path_file, 'r', encoding='windows-1251') as csv_file:
            file = csv.DictReader(csv_file)
            for row in file:
                name = row['name']
                price = float(row['price'])
                quantity = float(row['quantity'])
                cls(name, price, quantity)
