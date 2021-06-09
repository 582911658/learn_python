responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查的名字和回答
    name = input('\n what is your name?')
    response = input('which montain would you like to climb today?')

    # 将答卷存储在字典中
    responses[name] = response

    # 看是否还有人要参与调查
    repeat = input('Would you like to let another person respond?(yes or no)')
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print('\n --- Poll Results ---\n')
for name, response in responses.items():
    print(name.title() + ' would like to climb' + response.title() + '.')
