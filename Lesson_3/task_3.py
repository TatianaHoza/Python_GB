tuple_obj = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')


my_dict = dict()

for item in tuple_obj:
    obj_type = type(item)
    lst = []
    for el in tuple_obj:
        if type(el) == obj_type:
            lst.append(el)
    
    my_dict[type(item)] = lst


print(my_dict)
