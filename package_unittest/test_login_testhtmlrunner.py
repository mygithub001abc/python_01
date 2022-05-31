# 1.使用TestSuite()，将不同的测试用例添加到套件中
"""
TestSuite():
    1.addTest(testCase),testCase代表测试用例，可以添加不同的测试用例到套件中（单条）
    2.addTests(tests)可以添加不同的测试用例到套件中（一组）
"""
# 2.使用TextTestRunner(),运行测试套件

from work.work_4 import login
import unittest, sys
from package_unittest.HTMLTestRunner import HTMLTestRunner
class TestLogin(unittest.TestCase):


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
    suite_a = unittest.TestSuite()

    # 往套件中添加用例
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_login_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)
    # 创建一个测试报告
    test_report = './test_report.html'

    # 打开测试报告
    with open(test_report, 'wb') as f:
        runner = HTMLTestRunner(f, title='测试报告', description='测试报告描述')
        runner.run(suite_a)
    # 运行套件中的用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite_a)
