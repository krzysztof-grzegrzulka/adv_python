class Property:
    def __init__(self, area, rooms: int, price, address):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return(f'Nieruchomość znajduje się w {self._area}, adres: ' +
               f'{self._address}. Znajduje się w niej {self._rooms} pokoi. ' +
               f'Wartość to {self._price}')


class House(Property):
    def __init__(self, _area, _rooms: int, _price, _address, _plot):
        super().__init__(_area, _rooms, _price, _address)
        self._plot = _plot

    def __str__(self) -> str:
        return(f'Dom znajduje się na {self._area}, adres: ' +
               f'{self._address}. Znajduje się w nim {self._rooms} pokoi. ' +
               f'Wartość to {self._price}. Działka ma rozmiar {self._plot}m2.')


class Flat(Property):
    def __init__(self, _area, _rooms: int, _price, _address, _floor):
        super().__init__(_area, _rooms, _price, _address)
        self._floor = _floor

    def __str__(self) -> str:
        return(f'Mieszkanie znajduje się w {self._area}, adres: ' +
               f'{self._address}. Znajduje się w nim {self._rooms} pokoi. ' +
               f'Wartość to {self._price}. Jest na piętrze {self._floor}.')


house = House('osiedle mieszkaniowe', 2, '250000', 'Czerwona 3', '1000')
flat = Flat('apartamentowiec', 3, '500000', 'Niebieska 3a/12', '10')

print(house)
print(flat)
