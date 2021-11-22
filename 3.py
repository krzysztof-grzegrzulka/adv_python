class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return(f'Nieruchomość znajduje się w {self.area}, adres: ' +
               f'{self.address}. Znajduje się w niej {self.rooms} pokoi. ' +
               f'Wartość to {self.price}')


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return(f'Dom znajduje się na {self.area}, adres: ' +
               f'{self.address}. Znajduje się w nim {self.rooms} pokoi. ' +
               f'Wartość to {self.price}. Działka ma rozmiar {self.plot} m2.')


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return(f'Mieszkanie znajduje się w {self.area}, adres: ' +
               f'{self.address}. Znajduje się w nim {self.rooms} pokoi. ' +
               f'Wartość to {self.price}. Jest na piętrze {self.floor}.')

house = House('osiedle mieszkaniowe', 2, '250000', 'Czerwona 3', '1000')
flat = Flat('apartamentowiec', 3, '500000', 'Niebieska 3a/12', '10')

print(house)
print(flat)