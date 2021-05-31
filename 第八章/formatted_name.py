def get_formatted_name(first_name, last_name, middle_name=''):
    """
    返回整洁的函数名
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()


musician = get_formatted_name('Jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
