letters = ['a', 'b', 'c']


def my_enumerate(my_list):
    return list(zip(range(len(my_list)), my_list))


print(my_enumerate(letters))
