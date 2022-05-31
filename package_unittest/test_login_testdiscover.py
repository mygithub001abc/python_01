# 1.使用TestLoader()，可以批量添加测试用例
"""
d. TestLoader
    1.可以批量运行测试用例:discover(test_dir, pattern= 'test*.py')
        test_dir:指定要搜索的路径
        pattern= 'test*.py'：指定匹配模式，在test_dir目录下搜索所有的patten文件
"""

from work.work_4 import login
import unittest, sys

class TestLogin(unittest.TestCase):

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    # 清除类方法
    @classmethod
    def tearDownClass(cls) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)
    # 初始化方法
    def setUp(self) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    # 清除方法

    def tearDown(self) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    # 1.测试登录的测试用例

    # case1: 输入正确的用户名和正确的密码登录

    def test_login_success(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case2：输入错误的用户名和密码登录

    def test_login_wrong(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('aaa', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case3：输入空的用户名或空的密码登录

    def test_password_is_null(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    # 创建一个套件
    suite_a = unittest.TestLoader().discover('.', pattern='test_login_testdiscover.py')


    print(suite_a)

    # 运行套件中的用例
    runner = unittest.TextTestRunner()
    runner.run(suite_a)
