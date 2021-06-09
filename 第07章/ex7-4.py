加披萨辅料 = []
active = True
while active:
    披萨辅料 = input('请输入一系列的披萨配料,输入quit 退出\n')
    if 披萨辅料 != 'quit':
        print('您输入的辅料已添加')
        加披萨辅料.append(披萨辅料)
        print(加披萨辅料)
        continue
    if 披萨辅料 == 'quit':
        active = False

print(加披萨辅料)
