prompt = '\nTell me someth,and I will repeatg it back to you:'
prompt += '\nEntel \'quit\' to end the program.\n'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
