"""
存在的问题
1.无法查看运行的用例数，比如成功了几条，失败了几条
2.如果失败了，是什么原因导致？最好给出失败的错误日志
3.无法组织用例，不能控制哪些执行，哪些不执行
"""

# 解决方案：使用unittest

# unittest框架说明

"""
a. TestCase():
    1.可进行断言 assertEqual(值1, 值2)
    2.测试可查看结果，可查看失败的原因
    3.可进行初始化和清除功能

测试过程中，最小的单元就是测试用例(TestCase) . 在unittest做测试时，需要遵循如下规则：
1）所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
2）每个测试方法，都是以test开头
3）编写测试类，建议以Test开头
4）编写的模块，建议小写test开头


b. TestSuite():
    1.可以添加不同的测试用例到套件中（单条）
    2.可以添加不同的测试用例到套件中（一组）
    
c. TextTestRunner():
    1.可以运行测试用例
    
d. TestLoader
    1.可以批量运行测试用例
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
    unittest.main()

