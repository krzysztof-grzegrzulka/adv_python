def take_3_ints(x: int, y: int, z: int) -> bool:
    if x + y >= z:
        return True
    else:
        return False


print(take_3_ints(1, 1, 1))  # wieksze
print(take_3_ints(1, 1, 2))  # rowne
print(take_3_ints(1, 1, 11))  # mniejsze
print(type(take_3_ints(1, 1, 11)))
