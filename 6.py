def list_operations(list1: list, list2: list) -> list:
    concat_list = [*list1, *list2]
    concat_list = list(set(concat_list))
    for i in range(len(concat_list)):
        concat_list[i] = concat_list[i]**3
    return concat_list


list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(list_operations(list1, list2))
