# This Python file uses the following encoding: utf-8
# 第一个例子是用类的方式实现斐波那契数列，很有意思的是那个那个next 和 __iter__
# 这两个是迭代器iterator的两个必备实现函数 ， 这个函数的优点是内存占用很小，基本不随着max值的变化而变化
# StopIteration()也很重要，没有这个函数，迭代就停不下来！！！

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

f = Fab(51)
print f.next();
for n in f:
    print n

#第二个例子就是用来说明yield的神奇作用，我记得在哪里看见过这种用法，也是yield，忘了哪种语言。。。。。。。。。
#起到的作用就是“输出不中断”或者“返回不中断继续”，哈哈哈哈哈哈，所以yield又被称为generator

def fab(max):
    n,a,b = 0,0,1
    while n <max:
        yield b;
        a, b = b, a+b
        n = n+1

for i in fab(5):
    print i
