def make_great(magicians):
    """
    打印列表中每一个魔术师的名字,
    并且添加“The Great”
    """
    while magicians:
        magician = 'The Great ' + magicians.pop()
        print(magician)


magicians = ['tom', 'tim', 'look']
make_great(magicians[:])
print(magicians)
