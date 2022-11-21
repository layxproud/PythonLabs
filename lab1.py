array = ['aboba', 'a', 'adadadaada', 'aaa',
         'bbbb', 'ccccc', 'ddddddd']


def lensort(list):
    newlist = sorted(list, key=len)
    return newlist


print(lensort(array))
