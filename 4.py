def take_3_ints(x: int, y: int, z: int) -> bool:
    if x + y >= z:
        return True
    else:
        return False


print(take_3_ints(1, 1, 1))  # wieksze
print(take_3_ints(1, 1, 2))  # rowne
print(take_3_ints(1, 1, 11))  # mniejsze
type_test = take_3_ints(1, 1, 11)
print(type(type_test))
