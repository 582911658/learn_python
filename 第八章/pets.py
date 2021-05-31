def describe_pet(animal_type='dog',pet_name = ''):
    """显示宠物信息"""
    print('I have a ' + animal_type.title() + '.')
    print('It\'s name is '+pet_name.title()+'.')


describe_pet(pet_name='Tom', animal_type='cat')
describe_pet('dog', 'Jimmy')
