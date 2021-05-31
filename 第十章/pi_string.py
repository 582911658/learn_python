file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('请输入你的生日，格式为mmddyy，例如900910\n')
if birthday in pi_string:
    print('pi前100万位中包含你的生日')
else:
    print('pi前100万位中不包含你的生日')
