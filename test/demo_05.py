class Students(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        print(self.__score)


    def test(self):
        ret =self.__score = 89
        return ret


s1 = Students("小明", 88)
print(s1.name)
# print(s1.__score)  私有属性无法访问
s1.get_score()
print(s1.test())




