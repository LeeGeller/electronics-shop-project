import pathlib

from src.item import Item

if __name__ == '__main__':
    ROOT = pathlib.Path(__file__).parent.parent
    DATA1 = pathlib.Path.joinpath(ROOT / 'src/items2.csv')
    DATA2 = pathlib.Path.joinpath(ROOT / 'src/items3.csv')
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(DATA1)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(DATA2)
    # InstantiateCSVError: Файл item.csv поврежден
