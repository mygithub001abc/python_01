
# 问题：测试用例过多导致用例冗余，维护性不高，产生原因，代码重复，数据不同


# 解决方案：使用parameterized实现数据参数化

# 使用方法：expend(list)  list: 数据列表

# 使用@parameterized.expand装饰器可以为测试函数的参数进行参数化
from work.work_4 import login
from parameterized import parameterized
import unittest


lst_data = [
    (0, 'admin', '123456'),
    (0, 'dev', '123456'),
    (1, 'aaa', '123456'),
    (1, 'admin', '12345'),
    (1, '', '123456'),
    (1, 'admin', '')
]

class TestLogin(unittest.TestCase):
    @parameterized.expand(lst_data)
    def test_login_success(self, except_value, username, password):

        actual_value = login(username, password).get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    unittest.main()

