def check_even(test_num) -> bool:
    if test_num % 2 == 0:
        return True
    else:
        return False


check_even_execution = check_even(12)

if check_even_execution is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print(type(check_even_execution))
