from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Jen'] = 'python'
favorite_languages['sarah'] ='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name,language in favorite_languages.items():
    print(name.title() +"'s favorite_language is "+language.title()+'.')
