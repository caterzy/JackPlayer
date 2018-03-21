# This Python file uses the following encoding: utf-8

class BaseCircle1:
    __jackName ="Rao"  #私有变量，不可继承
    baseVer1 = "baseVer1";
    def __init__(self, name):
        self.__jackName = name

class BaseCircle2:
    baseVer2 = "baseVer2";

class Circle(BaseCircle1,BaseCircle2):
    __XinName ="Rao"  #私有变量，不可以继承，不能被实例调用
    ver = "123";

c = Circle("JackRao");
print c.ver
print c.baseVer1
print c.baseVer2


class Employee:
    name = "";

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print john.name


class Emply(Employee):
    pass

ee = Emply();
ee.name


