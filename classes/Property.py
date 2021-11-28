class Property:
    def __init__(self, area, rooms: int, price, address):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return (f'Nieruchomość znajduje się w {self._area}, adres: ' +
                f'{self._address}. Znajduje się w niej {self._rooms} pokoi. ' +
                f'Wartość to {self._price}')
