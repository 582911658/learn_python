print('10以内被2整除的数')
current_number1 = 0
while current_number1 < 10:
    if current_number1 % 2 == 0:
        print(current_number1)
    current_number1 += 1
    continue
print('10以内不能被2整除的数')
current_number2 = 0
while current_number2 < 10:
    if current_number2 % 2 != 0:
        print(current_number2)
    current_number2 += 1
    continue
