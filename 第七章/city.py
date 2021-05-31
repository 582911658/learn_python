prompt = '\nPlease enter the name of a city you have vist :'
prompt += '\n(Enter \'quit\' when you are finished.)'
prompt += '\n>'
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('I\'d love to go ' + city.title()+'!')
