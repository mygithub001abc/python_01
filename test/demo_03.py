list1 = []
for item in [100, 200, 300]:
    # for item in [100, 200, 300][::-1]:
    list1.insert(0, item)

print(list1)

# 集合的方法
s1 = {1, 2, 3, 4, 5, 6, 7}

print(len(s1))

# 成员运算
print(1 in s1)
print(8 not in s1)

# 浅拷贝方法
s2 = s1.copy()
print(s2)

# 添加元素
s1.add(8)
print(s1)

# 删除
s1.remove(4)
print(s1)

# s1.remove(4) # remove方法如果元素不存在则会报错

s1.discard(7)
print(s1)

s1.discard(7)  # discard方法如果元素不存在也不会报错

print(s1.pop())
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)  # set()

# print(s2[0])    集合不能通过下标操作

for item in s2:
    print(item)

print(list(zip(['one', 'two', 'three'], [100, 200, 300])))
d6 = dict(zip(['one', 'two', 'three'], [100, 200, 300]))
print(d6)

d7 = dict.fromkeys("ab")  # {'a': None, 'b': None}
print(d7)
d8 = dict.fromkeys("ab", 100)
print(d8)

d1 = dict(one=1, two=2, three=3)
print(d1)
d1['one'] = 100
print(d1)
d1['other'] = 4
print(d1)

d1.update({'one': 1000, 'test': 5})
print(d1)

d1.update(one=999, test2=6)
print(d1)

d1.update((('one', 888),))
print(d1)

print(d1.setdefault('one'))

print(d1.setdefault('one1'))
print(d1)

print(d1.setdefault('one2', 9999))
print(d1)


print("============================")
# 格式化字符串字面量
# str.format()方法

# print风格
# 1. formatstring % value   只需要替换一个值的时候
# 2. formatstring % (value1, value2...) 可以用元组来表示要替换的多个值
# 3. formatstring % {key1: value1, key2: value2...}

name = 'xxx'
age = 18
height = 198.60
hometown = '广东'

s1 = "姓名: %s" % name
print(s1)

s1 = "姓名: %s\n年龄: %d" % (name, age)
print(s1)

s1 = "姓名: %(name)s\n年龄: %(age)d" % {"height": 188.90, "name": "yyyy", "age": 30}
print(s1)


# 格式化字符串字面量
# 在字符串的前面加上f或者F,能将字符串中{}里面内容进行替换
name = 'xxx'
age = 18
height = 198.60
hometown = '广东'


print("name: {name}")
print(f"name: {name}")
print(F"name: {name}")

# :加上一个整数，可以指定该字段的最小字符宽度
for item in range(1, 11):
    print(f"{item:2} {item**2:3} {item**3:4}")


# str.format()方法
name = 'xxx'
age = 18
height = 198.60
hometown = '广东'

s1 = "姓名: {}\n年龄: {}\n身高: {}".format(name, age, height)
print(s1)

s1 = "姓名: {2}\n年龄: {0}\n身高: {1}".format(age, height, name)
print(s1)

s1 = "姓名: {1}\n年龄: {0}\n身高: {0}".format(age, name)
print(s1)