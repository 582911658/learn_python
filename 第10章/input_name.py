file_name = 'guest.txt'
with open(file_name, 'a') as file_project:
    print('输入q退出程序')
    first_name = ' '
    last_name = ' '
    while (first_name != 'q'):
        first_name = input('Please input your first_name.\n')
        last_name = input('Please input your last_name.\n')
        file_project.write(first_name.title()+'.'+last_name.title()+'\n')
