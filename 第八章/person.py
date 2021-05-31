def build_person(first_name, last_name,age = ''):
    """
    返回一个字典，其中包含一个人名信息
    """
    person = {'first': first_name, 'last': last_name, 'age': age}
    if age :
        person['age'] = age
    return person
    
    
musician = build_person('jimi', 'hendrix',age = 27)
print(musician)

