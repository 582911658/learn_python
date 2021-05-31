# name = input('Please enter your name:')
# print('Hello '+name.title()+'!')

prompt = '''If you tell us who you are,
so we can personalize the messages you see.'''
prompt += '\nWhat is your first name?\n'

name = input(prompt)
print('\n Hello ' + name.title() + '!')
