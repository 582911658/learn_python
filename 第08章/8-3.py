def make_shirt(size, word):
    """
    打印衣服的尺码
    """
    print(size.title()+'\n'+word.title())


make_shirt('63', 'I love python')
make_shirt(size='63', word='I love python')
