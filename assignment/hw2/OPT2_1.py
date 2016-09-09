# author    :   Will Fu
# date      :   2016-09-09

def list_int(a_list):
    """ Return the elements of the list
        of type int.
    """
    new_list = []
    for value in a_list:
        if isinstance(value, int):
            new_list.append(value)

    return new_list

list1 = [0, 'A', 12.5, 8, "hello", 583]
print(list_int(list1))
