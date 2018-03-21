__author__ = 'JackRao'

import math;

class Circle:
    def __init__(self, radius=1):
        self.radius = radius;

    def getPerimeter(self):
        return 2*self.radius * math.pi;

    def getArea(self):
        return self.radius * self.radius * math.pi;



class Car(object):
    def __init__(self,model,color,mpg):
        self.model = model;
        self.color = color;
        self.mpg = mpg;


class Nothing1:
    pass


class Nothing2(object):
    pass

print "Nothing1 type: %s ; Nothing1: %s" % (type(Nothing1),type(Nothing2))