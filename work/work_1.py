"""
1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
2. 打印1~100内被3整除的所有数的和 。
3. 使用range()输出1~10内的所有奇数 。
4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
5. 求1+2+3+...+100的和
6. 判断一个数n能同时被3和5整除
7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。备注：需要使用input()方法
10. 将一个列表的数据复制到另一个列表中。
11. 输出 9*9 乘法口诀表。
12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
数相加)，几个数相加由键盘控制。
14. 题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *

"""

# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a, b, c, d = 1, 2, 3, 4
num01 = a + b - c * d
print(num01)

# 2. 打印1~100内被3整除的所有数的和

sum = 0
for x in range(1, 101):
    if x % 3 == 0:
        sum += x
print(sum)

# 3. 使用range()输出1~10内的所有奇数
for x in range(1, 11):
    if x % 2:
        print(x)

# 4. 打印1~100所有偶数的和减去所有奇数的和的值

sum01 = 0  # 偶数累加和,初始值0
sum02 = 0  # 奇数累加和，初始值0

for x in range(1, 101):
    if x % 2 == 0:
        sum01 += x
    else:
        sum02 += x
print(sum01 - sum02)

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1, 101):
    sum += x
print(sum)

# 6. 判断一个数n能同时被3和5整除
# n = int(input("请输入一个数："))
# if n % 3 == 0 and n % 5 == 0:
#     print("这个数能同时被3和5整除")
# else:
#     print("这个数不能同时被3和5整除")

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
num = 25
if num in range(1, 101):
    print(num)

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()

# x = int(input("请输入第一个整数:"))
# y = int(input("请输入第二个整数:"))
# z = int(input("请输入第三个整数:"))
# list1 = [x, y, z]
# list1.sort()
# for num in list1:
#     print(num)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法

# score = int(input("请输入您的成绩："))
# if score >= 90:
#     print("A")
# elif 60 <= score <= 89:
#     print("B")
# else:
#     print("C")

# 10. 将一个列表的数据复制到另一个列表中
list1 = [4, 5, 6]
list2 = [1, 2, 3]
list2.extend(list1)
print(list2)

# 11. 输出 9*9 乘法口诀表

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%dx%d=%-2d" % (j, i, i * j), end="\t")
    print()

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# input_str = input("请输入一行字符串：")
# a1 = a2 = a3 = a4 = 0
# for char in input_str:
#     if char.encode("utf8").isalpha():
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

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
# 从键盘获取a
# a = int(input("请输入一个数字："))
# # 从键盘控制几个数相加
# b = int(input("请输入要加的次数："))
# s = 0
# sum = 0
# i = 0
# while i < b:
#     s += a * (10 ** i)
#     sum += s
#     i += 1
# print(sum)

# 14. 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 方法一：
for i in range(1, 8, 2):
    str = '*' * i
    print(str.center(7))
for i in range(5, 0, -2):
    str = '*' * i
    print(str.center(7))

print('=' * 10)

# 方法二：
for n in range(1, 5):
    print(' ' * (4 - n) + '*' * (2*n-1))
for n in range(1, 4):
    print(' ' * n + '*' * (7- 2 * n))