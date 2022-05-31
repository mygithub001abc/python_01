s1 = "hello world"
num = 25
f1 = 3.14
b1 = False
print(s1, type(s1))
print(num, type(num))
print(f1, type(f1))
print(b1, type(b1))

# 单条件判断
weather = "rain"
if weather == "rain":
    print("打车")
else:
    print("坐地铁")

# 多条件判断
score = 89
if score > 90:
    print("优秀")
elif score > 80:
    print("良好")
elif score > 60:
    print("及格")
else:
    print("不及格")

#  打印 1- 5
a = 1
while a <= 5:
    print(a)
    a += 1

# 计算1-100的和

sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
print(sum)

for x in range (10, 1, -2):
    print(x)


l1 = []
l2 = [12, '123', 'abc', 3.14, [1, 2, 3]]
print(l1)
print(l2)

for x in l2:
    print("列表中的值：", x)


list1 = ["red", "green", "yello"]
print(list1)

list1.append("black")
print(list1)

print(list1.count("green"))

list1.extend("abc")
print(list1)

print(list1.index('a'))

list1.insert(5, 666)
print(list1)

list1.pop(1)
print(list1)

list1.remove("black")
print(list1)

list1.reverse()
print(list1)
print("================")
l1 = [20, -3, 5, 300]
l1.sort()
print(l1)

# 练习：返回1~10之间的偶数
for x in range(2, 11, 2):
    print(x)



