# This Python file uses the following encoding: utf-8

def myFunction():
    pass

f = myFunction;

print(f)

####################################################################

def iabs(x):return abs(x);

def isum(x,y,f):return f(x)+f(y);

_abs = iabs;
result = isum(-991,-1,_abs);
print (result)


####################################################################
# 匿名函数：lambda
####################################################################
def add(x,y):return x+y;
print (add(1,2))

_add = lambda x,y: x+y
print (_add(1,2))


def sum(x,y=10):return x+y
sum2 = lambda x,y=10:x+y
print (sum2(1))       #11
print (sum2(1,100))   #101