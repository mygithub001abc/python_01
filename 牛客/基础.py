"""
1.将字符串 'Hello World!' 存储到变量str中，再使用print语句将其打印出来
"""
str = "Hello World!"
print(str)
"""
2.将字符串 'Hello World!' 存储到变量str1中，
再将字符串 'Hello Nowcoder!' 存储到变量str2中，
再使用print语句将其打印出来（一行一个变量）
"""
str1 = "Hello World!"
str2 = "Hello Nowcoder!"
print(str1)
print(str2)
print('=' * 60)
"""
3.假设输入的name为Niuniu，则输出I am Niuniu and I am studying Python in Nowcoder!
"""
name = input("请输入名字：")
print("I am %s and I am syudying Python in Nowcoder!" % name)
"""
4.请分别按全小写、全大写和首字母大写的方式对name进行格式化输出（注：每种格式独占一行）
输入：
niuNiu
输出：
niuniu
NIUNIU
Niuniu
"""
print(name.lower())
print(name.upper())
print(name.title())
"""
5.请输出name去掉两边的空白符后的原本的内容。
输入：
 Niuniu 
输出：
Niuniu
"""
name = input("请输入一行字符串：")
print(name.strip())
print('=' * 60)
"""
6.
使用print()语句直接打印数字2和数字3是否相等的比较结果；
使用print()语句直接打印数字2和数字3是否不相等的比较结果；
使用print()语句直接打印数字2是否大于数字3的比较结果；
使用print()语句直接打印数字2是否小于数字3的比较结果；
使用print()语句直接打印数字2是否大于等于数字3的比较结果；
使用print()语句直接打印数字2是否小于等于数字3的比较结果；
使用print()语句直接打印 数字2是否小于数字3的比较结果 逻辑与（也即使用 and 运算符） 数字2是否小于数字1的比较结果 的运算结果 ；
使用print()语句直接打印 数字2是否小于数字3的比较结果 逻辑或（也即使用 or 运算符） 数字2是否小于数字1 的比较结果 的运算结果；
使用print()语句直接打印字符串'Python'和字符串"Python"是否相等的比较结果；
使用print()语句直接打印字符串'Python2'和字符串'Python3'是否不相等的比较结果；
使用print()语句直接打印字符串'PYTHON'.lower()和字符串'Python'.lower()是否相等的比较结果；
创建一个列表my_list，其中依次包含[1, 3]中的所有整数，
如果数字2在列表my_list里，请使用print()语句一行打印字符串'2 is in my_list!'；
如果数字8不在列表my_list里，请使用print()语句一行打印字符串'8 is not in my_list!'。
"""
print(2 == 3)
print(2 != 3)
print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)
print(2 < 3 and 2 < 1)
print(2 < 3 or 2 < 1)
print("Python" == "Python")
print("Python2" != "Python3")
print("PYTHON".lower() == "Python".lower())
my_list = [1, 2, 3]
if 2 in my_list:
    print("2 is in my_list!")
if 8 not in my_list:
    print("8 is not in my_list!")
print('=' * 60)
"""
7.读入第一个数字记入变量x中，读入第二个数字记入变量y中；
然后依次逐行用print函数打印x与y相加，x减去y，x与y相乘，x除以y（整除），x对y取余的计算结果。
输入：
4
2
输出：
6
2
8
2
0
"""
x = int(input("请输入一个整数："))
y = int(input("请输入一个非0整数："))
print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x % y)
print('=' * 60)
"""
8.某公司在面试结束后，创建了一个依次包含字符串 'Allen' 和 'Tom' 的列表offer_list，作为通过面试的名单。
请你依次对列表中的名字发送类似 'Allen, you have passed our interview and will soon become a member of our company.' 的句子。
但由于Tom有了其他的选择，没有确认这个offer，HR选择了正好能够确认这个offer的Andy，所以请把列表offer_list中 'Tom' 的名字换成 'Andy' ，
再依次发送类似 'Andy, welcome to join us!' 的句子。
输出描述：
按题目描述进行输出即可。
Allen, you have passed our interview and will soon become a member of our company.
Tom, you have passed our interview and will soon become a member of our company.
Allen, welcome to join us!
Andy, welcome to join us!
"""
off_list = ['Allen', 'Tom']
for i in off_list:
    print('%s, you have passed our interview and will soon become a member of our company.' % i)
off_list[1] = 'Andy'
for j in off_list:
    print("%s,welcome to join us!"% j)
print('=' * 60)
"""
9.为庆祝驼瑞驰在牛爱网找到合适的对象，所以驼瑞驰创建了一个依次包含字符串 'Niuniu' 和 'Niu Ke Le' 的列表guest_list，作为庆祝派对的邀请名单。
请你依次对列表中的名字发送类似'Niuniu, do you want to come to my celebration party?'的句子。
驼瑞驰的好朋友牛牛、GURR哥和LOLO姐也正好有空，所以请使用insert()方法把字符串'GURR'插入到列表guest_list的开头，
再使用insert()方法把字符串'Niumei'插入到字符串'Niu Ke Le'的前面，再使用append()方法把字符串'LOLO'插入到列表guest_list的最后，
再依次发送类似'Niuniu, thank you for coming to my celebration party!'的句子。
输入描述：
无
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Niuniu, do you want to come to my celebration party?
Niu Ke Le, do you want to come to my celebration party?

GURR, thank you for coming to my celebration party!
Niuniu, thank you for coming to my celebration party!
Niumei, thank you for coming to my celebration party!
Niu Ke Le, thank you for coming to my celebration party!
LOLO, thank you for coming to my celebration party!
"""
guest_list = ['Niuniu', 'Niu Ke Le']
for i in guest_list:
    print("%s,do you want to my celebration party?" % i)

print()

guest_list.insert(0, 'GURR')
guest_list.insert(2, 'Niumei')
guest_list.append('LOLO')
for j in guest_list:
    print("%s,thank you for coming to my celebration party!" % j)
print('=' * 60)
"""
10.毕业季到了，牛牛为了找工作准备了自己简历，以及投递公司的列表company_list，
其中包括了字符串 'Alibaba', 'Baidu', 'Tencent', 'MeiTuan', 'JD' 作为他投递简历的目标公司。
请向列表中每个公司发送一条消息类似 'Hello Alibaba, here is my resume!'。
然而，遗憾的是Alibaba、Tencent、MeiTuan、JD都没有通过牛牛的简历审核，只有Baidu回复了他，邀请他去参加面试。因此你需要：
使用 del() 函数删除列表company_list中的字符串 'Alibaba'.
使用 pop() 函数依次删除列表company_list中的字符串'JD'，'MeiTuan'.
使用 remove() 函数删除列表company_list中的字符串'Tencent'.
最后向列表中的剩余的公司发送类似 'Baidu, thank you for passing my resume. I will attend the interview on time!' 的消息。

输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Hello Alibaba, here is my resume!
Hello Baidu, here is my resume!
Hello Tencent, here is my resume!
Hello MeiTuan, here is my resume!
Hello JD, here is my resume!

Baidu, thank you for passing my resume. I will attend the interview on time!
"""
company_list = ['Alibaba', 'Baidu', 'Tencent', 'MeiTuan', 'JD']
for company in company_list:
    print("Hello %s, here is my resume!" % company)
del company_list[0]
company_list.pop()
company_list.pop()
company_list.remove('Tencent')
for company in company_list:
    print("%s,thank you for passing my resume. I will attend the interview on time!" % company)

print("=" * 60)
"""
11.创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list后，
先使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，

输出一个换行，再使用print()语句一行打印字符串'The result of a temporary reverse order:'，
再使用print()语句把使用sorted()函数对列表my_list进行临时降序排序的结果整个打印出来；

输出一个换行，再使用print()语句一行打印字符串'Here is the original list again:'，
再使用print()语句把原来的列表my_list整个打印出来，确认没有改变原来的列表my_list；

对列表my_list调用sort()方法，使列表my_list中的字符串以降序排序，
输出一个换行，再使用print()语句一行打印字符串'The list was changed to:'，
再使用print()语句把修改后的列表my_list整个打印出来，确认列表my_list的字符串以降序排序；

对列表my_list调用reverse()方法，使列表my_list中的字符串的位置前后翻转，
输出一个换行，再使用print()语句一行打印字符串'The list was changed to:'，
再使用print()语句把修改后的列表my_list整个打印出来，确认列表my_list的字符串的位置前后翻转了。
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Here is the original list:
['P', 'y', 't', 'h', 'o', 'n']

The result of a temporary reverse order:
['y', 't', 'o', 'n', 'h', 'P']

Here is the original list again:
['P', 'y', 't', 'h', 'o', 'n']

The list was changed to:
['y', 't', 'o', 'n', 'h', 'P']

The list was changed to:
['P', 'h', 'n', 'o', 't', 'y']
"""
my_list = ['P', 'y', 't', 'h', 'o', 'n']
print('Here is the original list:')
print(my_list)

print()
print('The result of a temporary reverse order:')

# 降序排列，不改变原列表
print(sorted(my_list, reverse=True))
print()

print('Here is the original list again:')
print(my_list)

# 降序排列，改变原列表
my_list.sort(reverse=True)
print()
print('The list was changed to:')
print(my_list)

# 翻转，改变原列表
my_list.reverse()
print()
print('The list was changed to:')
print(my_list)

print('=' * 60)
"""
12.使用一个 for 循环 或 while 循环 打印[0, 15]中的所有整数（一行一个数字）
"""
for i in range(16):
    print(i)

print('=' * 60)
"""
13.牛牛有一个name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'] 记录了他最好的朋友们的名字，请创建一个二维列表friends，使用append函数将name添加到friends的第一行。
假如Niumei最喜欢吃pizza，最喜欢数字3，YOLO最喜欢吃fish， 最喜欢数字6，Niu Ke Le最喜欢吃potato，最喜欢数字0，Mona最喜欢吃beef，最喜欢数字3。
请再次创建一个列表food依次记录朋友们最喜欢吃的食物，并将创建好的列表使用append函数添加到friends的第二行；
然后再创建一个列表number依次记录朋友们最喜欢的颜色，并将创建好的列表使用append函数添加到friends的第三行。
这样friends就是一个二维list，使用print函数直接打印这个二维list。

输出描述：
[['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'], ['pizza', 'fish', 'potato', 'beef'], [3, 6, 0, 3]]
"""
friends = []
name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
friends.append(name)
food = ['pizza', 'fish', 'potato', 'beef']
friends.append(food)
number = [3, 6, 0, 3]
friends.append(number)
print(friends)

print('=' * 60)
"""
14.创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，
使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，
输出一个换行，再使用print()语句一行打印字符串'The number that my_list has is:'，
再使用len()函数获取列表my_list里面有多少个字符串，并使用print()函数一行打印该整数。
输入描述：
无
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Here is the original list:
['P', 'y', 't', 'h', 'o', 'n']

The number that my_list has is:
6
"""
my_list = ['P', 'y', 't', 'h', 'o', 'n']
print('Here is the original list:')
print(my_list)

print()
print('The number that my_list has is:')
print(len(my_list))

print('=' * 60)
"""
15.牛牛、牛妹和牛可乐都是Nowcoder的忠实用户，又到了一年一度的程序员节（10月24号），毫无疑问，他们都登录Nowcoder了，因为他们还没有刷完牛客题霸...
Nowcoder的管理员想对他们发送一些简单登录问候消息，并对他们表达了节日祝福。
请创建一个依次包含字符串 'Niuniu' 、'Niumei' 和 'Niu Ke Le' 的列表users_list，
请使用for循环遍历列表user_list，依次对列表users_list中的名字输出一行类似 'Hi, Niuniu! Welcome to Nowcoder!' 的字符串，
for循环结束后，最后输出一行字符串 "Happy Programmers' Day to everyone!"
输入描述：
无
输出描述：
按题目描述进行输出即可。
Hi, Niuniu! Welcome to Nowcoder!
Hi, Niumei! Welcome to Nowcoder!
Hi, Niu Ke Le! Welcome to Nowcoder!
Happy Programmers' Day to everyone!
"""
user_list = ['Niuniu', 'Niumei', 'Niu Ke Le']
for user in user_list:
    print("Hi,%s! Welcome to Nowcoder!" % user)
print("Happy Programmers' Day to everyone!")

print('=' * 60)
"""
16.创建一个列表my_list，其中包含[1, 1 000]中的所有整数，
再使用 min() 和 max() 核实该列表确实是从 1 开始，到 1 000 结束的。
此外，再对这个列表调用函数 sum()，看看 Python 将这一千个数字相加得到的结果是多少。
最后，对这个列表的所有整数求取平均值，直接保留一位小数。
输入描述：
无
输出描述：
输出三个整数，一个小数，每个数字独占一行。

备注：
1
1000
500500
500.5
"""
my_list = [num for num in range(1, 1001)]
print(min(my_list))
print(max(my_list))
print(sum(my_list))
avg = sum(my_list) / len(my_list)
print("%.1f" % avg)

print('=' * 60)
"""
17.通过给函数 range()指定第三个参数来创建一个列表my_list，其中包含 [0, 19]  中的所有偶数；
再使用一个 for 循环将这些数字都打印出来（每个数字独占一行）
"""
my_list = [num for num in range(0, 20, 2)]
for num in my_list:
    print(num)
print('=' * 60)
"""
18.创建一个列表my_list，其中包括 [1, 50] 内全部能被5整除的数字；再使用一个 for 循环将这个列表中的数字都打印出来（每个数字独占一行）
"""
my_list = [num for num in range(1, 51) if num % 5 == 0]
for num in my_list:
    print(num)
print('=' * 60)
"""
19.在Python中， * 代表乘法运算， ** 代表次方运算。
请创建一个空列表my_list，使用for循环、range()函数和append()函数令列表my_list包含底数2的 [1, 10] 次方，
再使用一个 for 循环将这些次方数都打印出来（每个数字独占一行
"""
my_list = []
for item in range(1, 11):
    my_list.append(2 ** item)
for num in my_list:
    print(num)

print('=' * 60)
"""
20.使用列表解析生成一个列表my_list，其中包含底数2的[1,10]次方。
再直接使用print()语句把刚刚创建的列表my_list整个打印出来（以列表形式，也即两边带方括号）
"""
my_list = []
for item in range(1, 11):
    my_list.append(2 ** item)
print(my_list)

print('=' * 60)
"""
21.创建一个列表group_list，其中依次包含字符串 'Tom', 'Allen', 'Jane', 'William', 'Tony' 表示这个小组成员的名字。
现有三项任务需要他们去完成，根据不同任务的繁琐度和实际情况需要分别派2人、3人、2人来完成，他们决定通过对列表分片来分配任务。
使用print()语句和切片来打印列表group_list的前两个元素表示去做第一个任务的人的名字，
再使用print()语句和切片来打印列表group_list的中间三个元素表示去做第二个任务的人的名字，
再使用print()语句和切片来打印列表group_list的后两个元素表示去做第三个任务的人的名字。
输入描述：
无
输出描述：
按照题意输出
['Tom', 'Allen']
['Allen', 'Jane', 'William']
['William', 'Tony']
"""
group_list = ['Tom', 'Allen', 'Jane', 'William', 'Tony']
print(group_list[:2])
print(group_list[2:])
print(group_list[-1:-3:-1])

print('=' * 60)
"""
22.创建一个依次包含字符串'Niuniu'、'Niumei'、'HR'、'Niu Ke Le'、'GURR' 和 'LOLO' 的列表users_list，
使用for循环遍历users_list，如果遍历到的用户名是 'HR' ，则使用print()语句一行打印字符串 'Hi, HR! Would you like to hire someone?'，
否则使用print()语句一行打印类似字符串 'Hi, Niuniu! Welcome to Nowcoder!' 的语句。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Hi, Niuniu! Welcome to Nowcoder!
Hi, Niumei! Welcome to Nowcoder!
Hi, HR! Would you like to hire someone?
Hi, Niu Ke Le! Welcome to Nowcoder!
Hi, GURR! Welcome to Nowcoder!
Hi, LOLO! Welcome to Nowcoder!
"""
user_list = ['Niuniu', 'Niumei', 'HR', 'Niu Ke Le', 'GURR', 'LOLO']
for user in user_list:
    if user == 'HR':
        print('Hi, HR! Would you like to hire someone?')
    else:
        print('Hi,{}! Welcome to Nowcoder!'.format(user))

print('=' * 60)
"""
23.创建一个空列表my_list，如果列表为空，请使用print()语句一行输出字符串'my_list is empty!'，
否则使用print()语句一行输出字符串'my_list is not empty!'。
"""
my_list = []
if len(my_list) == 0:
    print('my_list is empty!')
else:
    print('my_list is not empty!')

print('=' * 60)
"""
24.创建一个依次包含字符串'Niuniu'、'Niumei'、'GURR'和'LOLO'的列表current_users，
再创建一个依次包含字符串'GurR'、'Niu Ke Le'、'LoLo'和'Tuo Rui Chi'的列表new_users，
使用for循环遍历new_users，如果遍历到的新用户名在current_users中，
则使用print()语句一行输出类似字符串'The user name GurR has already been registered! Please change it and try again!'的语句，
否则使用print()语句一行输出类似字符串'Congratulations, the user name Niu Ke Le is available!'的语句。（注：用户名的比较不区分大小写）
输入描述：
无
输出描述：
按题目描述进行输出即可。
The user name GurR has already been registered! Please change it and try again!
Congratulations, the user name Niu Ke Le is available!
The user name LoLo has already been registered! Please change it and try again!
Congratulations, the user name Tuo Rui Chi is available!
"""
current_users = ['Niuniu', 'Niumei', 'GURR', 'LOLO']
new_users = ['GurR', 'Niu Ke Le', 'LoLo', 'Tuo Rui Chi']
for name in new_users:
    i = name.upper()
    if i in current_users:
        print('The user name %s has already been registered! Please change it and try again!' % name)
    else:
        print('Congratulations, the user name %s is available!' % name)

print('=' * 60)
"""
25.某食堂今天中午售卖 'pizza'：10块钱一份，'rice' ：2块钱一份，'yogurt'：5块钱一份，剩下的其他菜品都是8块钱一份。
请创建如下一个order_list记录点单情况：
['rice', 'beef', 'chips', 'pizza', 'pizza', 'yogurt', 'tomato', 'rice', 'beef']
然后使用for循环遍历列表order_list，使用if-elif-else结构依次打印每份菜品及其价格，且每个菜品都独占一行，按照'beef is 8 dollars'的形式。
并且在遍历过程中将价格相加，求对于这些点单记录，食堂总共营业收入多少？（单独输出一个整数）
输入描述：
无
输出描述：
按题目描述进行输出即可。
rice is 2 dollars
beef is 8 dollars
chips is 8 dollars
pizza is 10 dollars
pizza is 10 dollars
yogurt is 5 dollars
tomato is 8 dollars
rice is 2 dollars
beef is 8 dollars
61
"""
order_list = ['rice', 'beef', 'chips', 'pizza', 'pizza', 'yogurt', 'tomato', 'rice', 'beef']
sum = 0
for item in order_list:
    if item == 'rice':
        print('%s is 2 dollars' % item)
        sum += 2
    elif item == 'pizza':
        print('%s is 10 dollars' % item)
        sum += 10
    elif item == 'yogurt':
        print('%s is 5 dollars' % item)
        sum += 5
    else:
        print('%s is 8 dollars' % item)
        sum += 8
print(sum)

print('=' * 60)
"""
26.又到了一年一度的牛客运动会，Tom和Andy报名参加了项目，
但由于比赛前一天，Andy喝了太多碳酸饮料，导致身体不适，所以临时让Allen上场了，
换人参赛需要修改参赛名单，请完成以下内容模拟整个过程。

请创建一个依次包含字符串'Tom'和'Andy'的元组my_tuple，
先使用print()语句一行打印字符串'Here is the original tuple:'，再使用for循环将元组my_tuple的内容打印出来；

请使用try-except代码块执行语句my_tuple[1] = 'Allen'，
若引发TypeError错误，先输出一个换行，再使用print()语句一行打印字符串"my_tuple[1] = 
'Allen' cause cause a TypeError: 'tuple' object does not support item assignment"；

再重新对my_tuple赋值一个新元组，新元组依次由字符串'Tom'和'Allen'构成。
输出一个换行，先使用print()语句一行打印字符串'The tuple was changed to:'，再使用for循环将元组my_tuple的内容打印出来，确定修改无误。
输入描述：
无
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Here is the original tuple:
Tom
Andy

my_tuple[1] = 'Allen' cause a TypeError: 'tuple' object does not support item assignment

my_tuple was changed to:
Tom
Allen
"""
my_tuple = ('Tom', 'Andy')
print('Here is the original tuple:')
for item in my_tuple:
    print(item)

try:
    my_tuple[1] = 'Allen'
except TypeError:
    print()
    print("my_tuple[1] = 'Allen' cause cause a TypeError: 'tuple' object does not support item assignment")
    my_tuple = ('Tom', 'Allen')
    print()
    print('The tuple was changed to:')
    for item in my_tuple:
        print(item)

print('=' * 60)
"""
27.创建一个依次包含键-值对'<': 'less than'和'==': 'equal'的字典operators_dict，
先使用print()语句一行打印字符串'Here is the original dict:'，
再使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，使用print()语句一行输出类似字符串'Operator < means less than.'的语句；

对字典operators_dict增加键-值对'>': 'greater than'后，
输出一个换行，再使用print()语句一行打印字符串'The dict was changed to:'，
再次使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，使用print()语句一行输出类似字符串'Operator < means less than.'的语句，确认字典operators_dict确实新增了一对键-值对。
输入描述：
无
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）
"""
operators_dict = {'<': 'less than', '==': 'equal'}
print('Here is the original dict:')
for i in sorted(operators_dict.keys()):
    print('Operator {} means {}'.format(i, operators_dict[i]))
operators_dict['>'] = 'greater than'
print()
print('The dict was changed to:')
for j in sorted(operators_dict.keys()):
    print('Operator {} means {}'.format(j, operators_dict[j]))

print('=' * 60)
"""
28.又到了毕业季，牛牛作为牛客大学的学生会主席，决定对本校的应届毕业生进行就业调查。
他创建了一个依次包含字符串'Niumei'、'Niu Ke Le'、'GURR'和'LOLO'的列表survey_list，作为调查名单；
又创建了一个依次包含键-值对'Niumei': 'Nowcoder'和'GURR': 'HUAWEI'的字典result_dict，作为已记录的调查结果。
请遍历列表survey_list，如果遍历到的名字已出现在 包含字典result_dict的全部键的列表 里，
则使用print()语句一行输出类似字符串'Hi, Niumei! Thank you for participating in our graduation survey!'的语句以表达感谢，
否则使用print()语句一行输出类似字符串'Hi, Niu Ke Le! Could you take part in our graduation survey?'的语句以发出调查邀请。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Hi, Niumei! Thank you for participating in our graduation survey!
Hi, Niu Ke Le! Could you take part in our graduation survey?
Hi, GURR! Thank you for participating in our graduation survey!
Hi, LOLO! Could you take part in our graduation survey?
"""
survey_list = ['Niumei', 'Niu Ke Le', 'GURR', 'LOLO']
result_dict = {'Niumei': 'Nowcoder', 'GURR': 'HUAWEI'}
for i in survey_list:
    if i in result_dict.keys():
        print('Hi, %s! Thank you for participating in our graduation survey!' % i)
    else:
        print('Hi, %s! Could you take part in our graduation survey?' % i)

print('=' * 60)
"""
29.创建一个依次包含键-值对{'name': 'Niuniu'和'Student ID': 1}的字典my_dict_1，
创建一个依次包含键-值对{'name': 'Niumei'和'Student ID': 2}的字典my_dict_2，
创建一个依次包含键-值对{'name': 'Niu Ke Le'和'Student ID': 3}的字典my_dict_3，
创建一个空列表dict_list，使用append()方法依次将字典my_dict_1、my_dict_2和my_dict_3添加到dict_list里，
使用for循环遍历dict_list，对于遍历到的字典，使用print()语句一行输出类似字符串"Niuniu's student id is 1."的语句以打印对应字典中的内容。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Niuniu's student id is 1.
Niumei's student id is 2.
Niu Ke Le's student id is 3.
"""
my_dict_1 = {'name': 'Niuniu', 'Student ID': 1}
my_dict_2 = {'name': 'Niumei', 'Student ID': 2}
my_dict_3 = {'name': 'Niu Ke Le', 'Student ID': 3}

dict_list = []
dict_list.append(my_dict_1)
dict_list.append(my_dict_2)
dict_list.append(my_dict_3)
for i in dict_list:
    print("{}'s student id is {}".format(i['name'], i['Student ID']))

print('=' * 60)
"""
30.驼瑞驰调查了班上部分同学喜欢哪些颜色，并创建了一个依次包含键-值对'Allen': ['red', 'blue', 'yellow']、'Tom': ['green', 'white', 'blue']和'Andy': ['black', 'pink']的字典result_dict，作为已记录的调查结果。
现在驼瑞驰想查看字典result_dict的内容，你能帮帮他吗？
使用for循环遍历"使用sorted()函数按升序进行临时排序的包含字典result_dict的所有键的列表"，对于每一个遍历到的名字，先使用print()语句一行输出类似字符串"Allen's favorite colors are:"的语句，然后再使用for循环遍历该名字在字典result_dict中对应的列表，依次输出该列表中的颜色。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Allen's favorite colors are:
red
blue
yellow
Andy's favorite colors are:
black
pink
Tom's favorite colors are:
green
white
blue
"""
result_dict = {'Allen': ['red', 'blue', 'yellow'], 'Tom': ['green', 'white', 'blue'], 'Andy': ['black', 'pink']}
key_list = sorted(result_dict.keys())
for i in key_list:
    print("{}'s favorite colors are:".format(i))
    for j in result_dict[i]:
        print(j)

print('=' * 60)
"""
31.创建一个依次包含键-值对'Beijing': {Capital: 'China'}、'Moscow': {Capital: 'Russia'}和'Paris': {Capital: 'France'}的字典cities_dict，
请使用for循环遍历"已使用sorted()函数按升序进行临时排序的包含字典cities_dict的所有键的列表"，
对于每一个遍历到的城市名，使用print()语句一行输出类似字符串'Beijing is the capital of China!'的语句。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Beijing is the capital of China!
Moscow is the capital of Russia!
Paris is the capital of France!
"""
cities_dict = {'Beijing': {'Capital': 'China'}, 'Moscow': {'Capital': 'Russia'}, 'Paris': {'Capital': 'France'}}

for i in sorted(cities_dict.keys()):
    print('{} is the capital of {}!'.format(i, cities_dict[i].get('Capital')))

#
# print('=' * 60)
"""
32.请定义一个函数cal()，该函数返回两个参数相减的差。
输入第一个数字记录在变量x中，输入第二个数字记录在变量y中，将其转换成数字后调用函数计算cal(x, y)，再交换位置计算cal(y, x)。
输入描述：
输入两个整数。
输出描述：
根据题目描述输出两个差，每个数字单独一行。
示例1
输入：
3
5
复制
输出：
-2
2
"""
def cal(x, y):
    return x - y

num1 = int(input("请输入一个整数："))
num2 = int(input("请输入一个整数："))

print(cal(num1, num2))
print(cal(num2, num1))

print('=' * 60)
"""
33.假如牛牛一个列表 friends_list 记录了他最好的几个朋友：['Niu Ke Le', 'Niumei', 'Niuneng', 'GOLO']，现在他想将列表里的名字替换成从0开始的数字，依次表示这几个朋友的重要性。
请写一个replace函数，第一个参数是列表friends_list，第二个参数是要替换的数字index，即在函数中将列表元素修改成成列表下标值。
请使用print函数直接打印修改前的列表。
使用for循环遍历列表 friends_list，每次调用replace函数替换列表中相应下标的元素。
结束循环后，再次使用print函数直接打印修改后的列表，查看是否替换成功。
输入描述：
无
输出描述：
['Niu Ke Le', 'Niumei', 'Niuneng', 'GOLO']
[0, 1, 2, 3]
"""
friends_list = ['Niu Ke Le', 'Niumei', 'Niuneng', 'GOLO']
print(friends_list)

def replace(friends_list, index):
    for index in range(len(friends_list)):  #[0, 1, 2, 3]
        friends_list[index] = index  # 把值的下标赋给值

for i in friends_list:
    replace(friends_list, i)

print(friends_list)


print('=' * 60)
"""
34.假如这是一台自动售卖饮料机的一段程序：
使用print()语句一行输出字符串 'What kind of drink would you like?' ，
然后使用input()函数读取字符串，并将读取到的字符串存储到变量kind_of_drink中，
假设读取到饮料是可乐（cola），也即变量kind_of_drink的内容为'cola'，
请使用print()语句一行输出字符串 'Below is your cola. Please check it!' 。
其他饮料已经售空了，因此如果是其他字符串，则输出一句类似 'The milk has been sold out!' 的信息。

输入描述：
无
输出描述：
按题目描述进行输出即可。
示例1
输入：
cola
复制
输出：
What kind of drink would you like?
Below is your cola. Please check it!
"""
print('What kind of drink would you like?')
kind_of_drink = input('请输入您想要的饮料：')
if kind_of_drink == 'cola':
    print( 'Below is your cola. Please check it!')
else:
    print('The milk has been sold out!')

print('=' * 60)
"""
35.编写一个 while 循环模拟餐厅服务员询问客人一共有多少人用餐，要求在 while 循环中使用条件测试来结束循环。
每次循环开始先使用print()语句一行输出字符串 "Welcome! How many people, please?\nEnter 'quit' to end the program."，
如果读取到字符串等于'quit'，则退出 while 循环，
否则将字符串转成整数，如果整数不超过4，则使用print()语句一行输出字符串 'Your small table is reserved!'；
如果整数大于4不超过6，则使用print() 语句一行输出字符串 'Your middle table is reserved!'；
如果整数大于6不超过10，则使用print() 语句一行输出字符串 'Your large table is reserved!'；
如果整数超过10，则使用print()语句一行输出字符串 'Sorry, there is no free table that seats over ten persons.'；
然后本次循环结束，再次进入 while 循环中的条件测试。
输入描述：
保证每一行的输入只有数字或字符串'quit'，且保证数字合法，范围在[1, 20]。
输出描述：
按题目描述进行输出即可。
示例1
输入：
2
18
quit
复制
输出：
Welcome! How many people, please?
Enter 'quit' to end the program.
Your small table is reserved!
Welcome! How many people, please?
Enter 'quit' to end the program.
Sorry, there is no free table that seats over ten persons.
Welcome! How many people, please?
Enter 'quit' to end the program.
"""
while True:
    print("Welcome! How many people, please?\nEnter 'quit' to end the program.")
    user_input = input("请输入就餐人数：")
    if user_input == 'quit':
        break
    elif int(user_input) <= 4:
        print( 'Your small table is reserved!')

    elif 4 < int(user_input) <= 6:
        print('Your middle table is reserved!')

    elif 6 < int(user_input) <= 10:
        print('Your large table is reserved!')

    else:
        print('Sorry, there is no free table that seats over ten persons.')

print('=' * 60)
"""
36.编写一个 while 循环判断输入的字符串对应的十进制数值是否是被8整除的数字，要求使用布尔变量 active 来控制循环结束的时机。
每次循环开始先使用print()语句一行输出字符串 "Please enter a positive integer!\nEnter 'quit' to end the program." ，
如果读取到字符串等于'quit'，则把布尔变量 active 的值更改为False，
否则将字符串转成整数，如果能被8整除即是8的倍数，则使用print()语句一行输出类似字符串'80 is a multiple of 8.'的语句，
否则使用print()语句一行输出类似字符串'4 is not a multiple of 8.'的语句，
然后本次循环结束，再次进入 while 循环中的条件测试。
输入描述：
保证每一行的输入只有数字或字符串'quit'，且保证数字合法，范围在[1, 100]。
输出描述：
按题目描述进行输出即可。
示例1
输入：
1
16
quit
复制
输出：
Please enter a positive integer!
Enter 'quit' to end the program.
1 is not a multiple of 8.
Please enter a positive integer!
Enter 'quit' to end the program.
16 is a multiple of 8.
Please enter a positive integer!
Enter 'quit' to end the program.
"""
active = True
while active:
    print("Please enter a positive integer!\nEnter 'quit' to end the program.")
    user_input = input('请输入要验证的数字：')
    if user_input == 'quit':
        active = False
    elif int(user_input) % 8 == 0:
        print('{} is a multiple of 8'.format(user_input))
    else:
        print('{} is not a multiple of 8'.format(user_input))

print('=' * 60)
"""
37.某游乐园院按照游客身高段收取票价：不到 1.0米 的游客免费； 1.0~1.2 米的游客为 80 元；超过 1.2 米的游客为 150 元。
请编写一个死循环，每次循环开始先使用print()语句一行输出字符串"Please tell me your height!\nEnter 'quit' to end the program."。
如果读取到的字符串等于'quit'，则使用 break 语句退出循环；
否则将字符串转成浮点数，如果小于1.0米，则使用print()语句一行输出字符串'Your admission cost is 0 yuan.'，
如果大于等于1.0米且小于等于1.2米，则使用print()语句一行输出字符串'Your admission cost is 80 yuan.'，
如果大于1.2米，则使用print()语句一行输出字符串'Your admission cost is 150 yuan.'，
然后本次循环结束，再次进入 while 循环中的条件测试。

输入描述：
保证每一行的输入只有浮点数或字符串'quit'，且保证数字合法，范围在[0, 3]。
输出描述：
按题目描述进行输出即可。
示例1
输入：
0.5
1.2
quit

输出：
Please tell me your height!
Enter 'quit' to end the program.
Your admission cost is 0 yuan.
Please tell me your height!
Enter 'quit' to end the program.
Your admission cost is 80 yuan.
Please tell me your height!
Enter 'quit' to end the program.
"""
while True:
    print("Please tell me your height!\nEnter 'quit' to end the program.")
    user_input = input('请输入您的身高：')
    if user_input == 'quit':
        break
    elif float(user_input) < 1.0:
        print('Your admission cost is 0 yuan.')
    elif 1.0 <= float(user_input) <= 1.2:
        print('Your admission cost is 80 yuan.')
    elif float(user_input) > 1.2:
        print('Your admission cost is 150 yuan.')

print('='*60)
"""
38.创建一个依次包含字符串'chicken'、' bacon'和'durian'的列表 pizza_orders，再创建一个名为 finished_pizza 的空列表，
使用 while 循环判断列表 pizza_orders 里面是否还有元素，如果有则使用pop()方法删掉将列表 pizza_orders 的最后一个元素，
并把刚刚删掉的元素存到一个名为pizza的变量，假设pizza的值为'bacon'，请使用print()语句一行打印类似字符串'I made your bacon pizza!'的语句，
并使用append()语句将pizza添加到列表 finished_pizza 的末尾，然后本次循环结束，再次进入 while 循环中的条件测试。
在 while 循环结束后，再使用print()语句把列表 finished_pizza 整个打印出来。

输入描述：
无
输出描述：
按题目描述进行输出即可。
I made your durian pizza!
I made your bacon pizza!
I made your chichen pizza!
['durian', 'bacon', 'chichen']
"""
pizza_orders = ['chicken', 'bacon', 'durian']
finished_pizza = []
while True:
    if len(pizza_orders) != 0:
        pizza = pizza_orders.pop()
        print('I made your {} pizza!'.format(pizza))
        finished_pizza.append(pizza)
    elif len(pizza_orders) == 0:
        break
print(finished_pizza)

print('='*60)
"""
39.创建一个依次包含字符串'bacon'、'durian'、'bacon'、'bacon'、'chicken'和'durian'的列表pizza_inventory，
使用 while循环 判断字符串'bacon'是否存在于列表pizza_inventory中，
如果存在，则使用remove()方法删掉列表pizza_inventory中的一个字符串'bacon'，并使用print()语句一行输出字符串'A bacon pizza was deleted from list.'，
然后本次循环结束，再次进入 while 循环中的条件测试。
在 while 循环结束后，如果if语句判断字符串'bacon'确实不在列表pizza_inventory中，
请使用print()语句一行输出字符串'There is really no bacon in pizza_inventory!'。
"""
pizza_inventory = ['bacon', 'durian', 'bacon', 'bacon', 'chicken', 'durian']
while True:
    if 'bacon' in pizza_inventory:
        pizza_inventory.remove('bacon')
        print('A bacon pizza was deleted from list.')
        break
    else:
        print('There is really no bacon in pizza_inventory!')

print('='*60)

"""
40.创建一个名为survey_dict的空字典，
请编写一个死循环，
每次循环开始先使用print()语句一行输出字符串'If you have the chance, which university do you want to go to most?'，
再使用print()语句一行输出字符串'What is your name?'，再将读取到的字符串存储在变量name中，
再使用print()语句一行输出字符串'Which university do you want to go to most?'，再将读取到的字符串存储在变量university中，
再把键-值对name: university存储在字典survey_dict中，
再使用print()语句一行输出字符串"Is there anyone who hasn't been investigated yet?"，
如果输入的字符串为'No'，则使用 break 语句退出循环，否则本次循环结束，再次进入 while 循环中的条件测试。
在 while 循环结束后，使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典survey_dict的所有键的列表，
对于每一个遍历到的被调查者的名字，使用print()语句一行输出类似字符串"I'am Tom. I'd like to go to Fudan University if I have the chance!"的语句。
输入描述：
无
输出描述：
按题目描述进行输出即可。
示例1
输入：
Tom
Fudan University
Yes
Ben
Peking University
Yes
Andy
Tsinghua University
No
复制
输出：
If you have the chance, which university do you want to go to most?
What is your name?
Which university do you want to go to most?
Is there anyone who hasn't been investigated yet?
If you have the chance, which university do you want to go to most?
What is your name?
Which university do you want to go to most?
Is there anyone who hasn't been investigated yet?
If you have the chance, which university do you want to go to most?
What is your name?
Which university do you want to go to most?
Is there anyone who hasn't been investigated yet?
I'am Andy. I'd like to go to Tsinghua University if I have the chance!
I'am Ben. I'd like to go to Peking University if I have the chance!
I'am Tom. I'd like to go to Fudan University if I have the chance!
"""
survey_dict = {}

while True:
    print('If you have the chance, which university do you want to go to most?')
    print('What is your name?')
    name = input('请输入姓名：')
    print('Which university do you want to go to most?')
    university = input('请输入您想上的大学：')
    print("Is there anyone who hasn't been investigated yet?")
    if input("请确认：") == 'No':
        break
    survey_dict[name] = university
for i in sorted(survey_dict.keys()):
    print("I'am {}. I'd like to go to {} if I have the chance!".format(i, survey_dict.get(i)))
print('='*60)
"""
41.牛牛有一份字符串my_str = 'I am$ N$iuniu$, an$d I $am stu$dying in $Now$coder!' 被污染了，其中出现了很多奇怪的$符号。
现请你使用split函数将这份字符串从符号$处分割成众多字符列表，记录在my_list中，并使用print函数直接打印my_list中的结果。
然后再使用join函数将my_list中的分段字符串重新连接成一个新的字符串，并使用print函数输出。
输入描述：
无
输出描述：
['I am', ' N', 'iuniu', ', an', 'd I ', 'am stu', 'dying in ', 'Now', 'coder!']
I am Niuniu, and I am studying in Nowcoder!
"""

my_str = 'I am$ N$iuniu$, an$d I $am stu$dying in $Now$coder!'
my_str =my_str.split('$')
print(my_str)
print(''.join(my_str))
