import classes.Property as Property


class House(Property):
    def __init__(self, _area, _rooms: int, _price, _address, _plot):
        super().__init__(_area, _rooms, _price, _address)
        self._plot = _plot

    def __str__(self) -> str:
        return (f'Dom znajduje się na {self._area}, adres: ' +
                f'{self._address}. Znajduje się w nim {self._rooms} pokoi. ' +
                f'Wartość: {self._price}. Działka ma rozmiar {self._plot}m2.')
