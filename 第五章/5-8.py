from typing import NoReturn


users = [ ]
users.append(input('请输入用户名'))
for user in users :
    if user =='admin':
        print('Hello admin,would you like to see a status report? ')
    elif user !='admin':
        print(f'Hello {user} thank you for login again!')