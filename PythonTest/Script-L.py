# This Python file uses the following encoding: utf-8
# 代替循环的切片功能

l = list(range(100));
print l;

ll = l[10:20]   #取中间10个
print ll;

print l[-10:]    #取后10个

print l[:10:2]   #前10个数，每两个取一个

print l[::5]     #每5个取一个

