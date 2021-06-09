# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的新列表
unconfirmed_users = ['Alice', 'Brain', 'candace']
confirmed_users = []

# 验证每一个用户，直到没有用户为止
# 将每一个已验证用户都移动到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying user:' + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证用户
print('\nThe following user have been confirmed:')
for confirned_user in confirmed_users:
    print(confirned_user.title())
