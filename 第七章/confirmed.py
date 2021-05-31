'''首先，先创建一个待验证的用户列表
和一个用于存储已验证用户用户的空列表'''
unconfirmed_users = ['alice','brain','candace']
confirmed_users =[]
# 验证每一个用户直到没有用户为止
# 将每一个经过验证的用户都迁移到已验证的用户中
while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    print('Verifying user:'+ current_user.title())
    confirmed_users.append(current_user)
# 显示已验证的用户
print('\n The following users have been confirmed:')
for confirmed_user in confirmed_users :
    print(confirmed_user.title())