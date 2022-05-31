"""
my_str = "我的名字是 %s" %("李四")
print(my_str)

my_str1 = "李四今年 %d 岁" % (18)
print(my_str1)

my_str2 = "一斤西瓜 %f 元" %(3.5)
print(my_str2)

my_str3 = "一斤西瓜 %10.2f 元" %(3.5)
print(my_str3)

my_str4 = "一斤西瓜 %-10.2f 元" %(3.5)
print(my_str4)

my_str5 = "一斤西瓜 %+-10.2f 元" %(3.5)
print(my_str5)

my_str6 = "一斤西瓜 {} 元".format(3.5)
print(my_str6)

my_str7 = "今天星期 {}, 我买了{} 斤西瓜".format('一', 6)
print(my_str7)

astr = '_'
bstr = astr.join('1234')
print(bstr)

cstr = 'a b c d '
dstr = cstr.split(' ')
print(dstr)


s1 = "helloworld"
print(s1.find("hello"))
print(s1.find("H"))
print(s1.index("o"))
# print(s1.index("H"))  # 找不到报错

s2 = "测试报告.doc"
print(s2.endswith(".doc"))

s2 = "***测试报告.doc"
print(s2.startswith("***"))

s3 = "hello world"
print(s3)
s4 = s3.replace("world", "python")
print(s4)

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# str = input("请输入一行字符：")

# a1 = a2 = a3 = a4 = 0
# for char in str:
#     if char.encode('utf8').isalpha():
#         a1 += 1
#     elif char.isspace():
#         a2 += 1
#     elif char.isdigit():
#         a3 += 1
#     else:
#         a4 += 1
# print("字母个数：", a1)
# print("空格个数：", a2)
# print("数字个数：", a3)
# print("其他个数：", a4)

l1 = [1, 2, 3, 4, 5, 6]
print(l1[0:3:1])  # 取1-3
print(l1[2:6:1])  # 取3-6

s1 = 'python'
print(s1[1:3:1])  # 2-3

t1 = (1, 2, 3, 4, 5)
print(t1[0:4])  # 1-4
print(t1[:4:1])
print(t1[::1])
print(t1[::])
print("=" * 60)
print("分隔符".center(80, "="))

str1 = str(t1)
for x in str1:
    if x.isdigit():
        print(x, end = "")
print(type(str1))


print([x for x in range(1, 11) if x % 2])
tu2 = {x for x in range(1, 11) if x % 2}
print(tu2)
"""

str2 = "[1, 2, 3, 4, 5]"
for x in str2:
    if x.isdigit():
        print(x, end="")

print()


def add(x, y):
    z = x + y
    return z


print(add(3, 4))
print(add(5.0, 3.14))
print(add('hello', 'python'))
print(add('python', '3.6'))

# def qingke(name='小明', day ):
def qingke(day, name='小明'):
    print("今天星期{}，所以{}请客".format(day, name))


qingke(day='二', name='张三')
qingke(day='六')

def add(x, y, *args):
    print(args)
    z = x + y + sum(args)
    return z

print(add(3, 4))
print(add(3, 4, 5))
print(add(3, 4, 5, 6, 7, 8))
print(add(3, 4, *[5, 6, 7, 8]))


def show_info(**kwargs):
    print(kwargs)

d1 = {'x':1, 'y':2, 'z':3}
print(show_info(a = 'hello', b = 'world'))
print(show_info(**d1))


class Students():
    name = ""
    grade= ""

    def study(self):
        print("{}年纪学生{}正在教师上课！".format(self.grade, self.name))


s1 = Students()
s1.name = '张三'
s1.grade = '5'
s1.study()

s2 = Students()
s2.grade = '4'
s2.name = '李四'
s2.study()

