"""
需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
"""
import time
from loguru import logger
# 方法 ：从文件中读取数据，返回的是列表形式的数据
def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name,'r')
        line = f.readline()
        user_data = eval(line)
        logger.info('返回的用户数据：'.format(user_data))
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


# 方法 ：向文件中写入内容，用户添加的信息是在原来的基础上添加的。
def save_data(file_name,file_content):
    f = None
    try:
        f = open(file_name,'a')
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

# 1.定义用户默认数据
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
             {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]

user_list1 = []
user_list1 = user_list if user_list1 else from_file_get_data(r'C:\Users\Admin\Desktop\z\5.python\project\python_01\work\user_data.txt')

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
# 创建一个类 ，包括新增用户，修改用户，删除用例，查询用户

class User(object):

    def __init__(self):
        pass

# 定义用户查询功能

    def get_user(self, username):

        # 1)用户未登录，返回权限不足
        if result.get('code') != 0 :
            result.pop('user_list')
            result.update({'message': '用户未登录，无法进行查询操作！'})   # 'code' : 1
            return result

        # 2)用户已登录成功，输入正确的用户名进行查询，返回结果（支持模糊查询）
        if result.get('code') == 0 :
            result.update({'user_list': []})
            lst = []  # 存放查询到的数据
            for x in user_list:
                get_username = x.get('account')  # 获取用户列表中的用户名
                if username in get_username:  # 实现模糊查询
                    x.pop('password')
                    lst.append(x)

            # 判断lst[]中是否为空，如果列表不为空，查询成功，返回对应的结果
            if lst:
                result.update({'message': '查询用户成功', 'user_list': lst})  # 'code': 0
                return result

            # 如果列表为空，说明输入的用户名不正确 ，返回无查询结果
            result.update({'code': 12, 'message': '未查询到用户,请重新输入'})  # 'code': 12  用户名未注册，查询无果
            return result

    # 定义用户添加功能

    def add_user(self, username , password = '123456', **kwargs):
        user_dict = {}
        user_dict['account'] = username
        user_dict['password'] = password
        user_dict.update(**kwargs)

        # 将组装的数据添加到用户列表中
        user_list.append(user_dict)

        save_data('user_data.txt', user_list)

        result.update({"message": "用户添加成功", "add_time": time.strftime("%Y-%m-%d %H:%M:%S")})

# 处理用户输入

if __name__ == '__main__':

    # 进行循环，以便用户进行各种操作
    flag = True

    while flag:

        # 1.提供用户的各种选择 ，比如输入1代表登录操作，输入2代表查询操作，输入q代表退出操作
        vls = input("1) 进行登录\t2) 进行查询用户\tq) 退出操作\t其它字符) 未知操作，请重新输入\n请输入对应操作编号：")

        # 2.当输入未知符号后，进行重新输入
        if vls not in ('1', '2', '3',  'q', 'quit'):
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
            u1 = User()
            get_result = u1.get_user(name)
            print(get_result)

            print('=' * 80)
            continue

        # 5.当输入3时，添加用户
        if vls == '3':
            start = 1
            while start:
                name = input("请输入添加的用户名:")
                user = User()
                get_result = user.get_user(name)

                if get_result.get('code') == 12 :
                    name = input("请再次输入添加的用户名:")
                    password = input("请输入用户密码:")
                    role = input("请输入用户角色:")
                    dept = input("请输入用户部门:")
                    user.add_user(name, password, role=role, dept=dept)
                    start = 0
                if get_result.get('code') == 0:
                    result.update({"code": 13, "message": "用户已存在，无法添加"})
                    print(result)
                    continue
                print(get_result)
                print('=' * 80)




        # 6.当输入q或quit时，退出操作
        if vls in ('q', 'quit'):
            flag = False
            print('退出成功！')

"""
bug
1.登录成功-->输入不存在的名字查询无结果-->输入存在的名字查询，返回未登录
1.登录成功-->输入存在的名字查询，返回结果-->输入不存在的用户名添加,添加成功-->再次查询时返回用户未登录
"""
