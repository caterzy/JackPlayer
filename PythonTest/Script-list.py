# This Python file uses the following encoding: utf-8


myList = [i**2 for i in range(1,11)];   ##生成一个1~10平方的数组

print myList


f = open("output.txt", "w")

for item in myList:
    f.write(str(item) + "\n")

f.close()