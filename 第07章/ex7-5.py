message1 = '不到三岁观众免费\n'
message2 = '3~12岁观众10美元\n'
message3 = '超过12岁观众15美元\n'
message4 = '输入q退出程序\n'
message5 = '请输入你的年龄>'
print(message1 + message2+message3 + message4)
while True:
    游客年龄 = input(message5)
    if 游客年龄 != 'q':
        游客年龄 = int(游客年龄)
        if 游客年龄 < 3:
            print('免费。\n')
        elif 游客年龄 <= 12:
            print('你的票价为10美元。\n')
        else:
            print('你的票价是15美元。')
    elif 游客年龄 == 'q':
        break
print('程序已退出')
