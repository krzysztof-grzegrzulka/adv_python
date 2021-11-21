def check_number_in_list(number_list: list, test_num: int):
    return test_num in number_list


list_for_tests = [1, 2, 3]
print(check_number_in_list(list_for_tests, 4))  # False
print(check_number_in_list(list_for_tests, 3))  # True
