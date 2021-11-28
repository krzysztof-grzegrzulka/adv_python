# import classes.Property as Property
from classes.Property import Property


class Flat(Property):
    def __init__(self, _area, _rooms: int, _price, _address, _floor):
        super().__init__(_area, _rooms, _price, _address)
        self._floor = _floor

    def __str__(self) -> str:
        return (f'Mieszkanie znajduje się w {self._area}, adres: ' +
                f'{self._address}. Znajduje się w nim {self._rooms} pokoi. ' +
                f'Wartość to {self._price}. Jest na piętrze {self._floor}.')
