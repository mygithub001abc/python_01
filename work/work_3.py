"""
需求-迭代2：用户查询功能:
1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
3. 若输入的用户名不正确 ，给出无查询结果的提示
4. 查询支持模糊查询。
"""

# 1.定义用户默认数据
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
             {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
# 2.定义默认返回结果
result = {'code': 0, 'message': ''}


# 3.定义登录功能
def login(username, password):
    # 1)用户名为空
    if username is None or username == '':
        result.update({'code': 1, 'message': '用户名不能为空'})
        return result

    # 2)密码为空
    if password is None or password == '':
        result.update({'code': 1, 'message': '密码不能为空'})
        return result

    # 3)用户名和密码都匹配，登录成功
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({'code': 0, 'message': '登录成功', 'user_list': user_list})
            return result

    # 4)用户名或密码不正确的情况
    result.update({'code': 1, 'message': '请检查您的用户名或密码是否填写正确'})
    return result

# 4.定义用户查询功能

def get_user(username):

    # 1)用户未登录，返回权限不足
    if result.get('code') != 0:
        result.update({'code': 1, 'message': '用户未登录，无法进行查询操作！'})
        return result

    # 2)用户已登录成功，输入正确的用户名进行查询，返回结果（支持模糊查询）
    if result.get('code') == 0:
        result.update({'user_list': []})
        lst = []  # 存放查询到的数据
        for x in user_list:
            get_username = x.get('account')  # 获取用户列表中的用户名
            if username in get_username:  # 实现模糊查询
                x.pop('password')
                lst.append(x)

        # 判断lst[]中是否为空，如果列表不为空，查询成功，返回对应的结果
        if lst:
            result.update({'message': '查询用户成功', 'user_list': lst})
            return result

        # 如果列表为空，说明输入的用户名不正确 ，返回无查询结果
        result.update({'message': '未查询到用户,请重新输入'})
        return result


# 处理用户输入

if __name__ == '__main__':

    # 进行循环，以便用户进行各种操作
    flag = True

    while flag:

        # 1.提供用户的各种选择 ，比如输入1代表登录操作，输入2代表查询操作，输入q代表退出操作
        vls = input("1) 进行登录\t2) 进行查询用户\tq) 退出操作\t其它字符) 未知操作，请重新输入\n请输入对应操作编号：")

        # 2.当输入未知符号后，进行重新输入
        if vls not in ('1', '2', 'q', 'quit'):
            print('无效输入，请重输')
            print('=' * 80)
            continue

        # 3.当输入1时，进行登录
        if vls == '1':

            username = input('请输入用户名：')
            password = input('请输入密码：')
            login_result = (login(username, password))  # 调用登录功能
            print(login_result)

            print('=' * 80)
            continue

        # 4.当输入2时，进行查询
        if vls == '2':
            name = input('请输入要查询的用户名：')
            get_result = get_user(name)
            print(get_result)

            print('=' * 80)
            continue

        # 5.当输入q或quit时，退出操作
        if vls in ('q', 'quit'):
            flag = False
            print('退出成功！')





