# version i
def calculations_i(numbers_param):
    numbers2 = []
    for number in numbers_param:
        numbers2.append(number*2)
    return numbers2

# version ii
def calculations_ii(numbers_param):
    numbers2 = [number*2 for number in numbers_param]
    return numbers2
    
print(calculations_i([1, 2, 3, 4, 5]))

print(calculations_ii([6, 7, 8, 9, 10]))