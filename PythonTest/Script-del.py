# This Python file uses the following encoding: utf-8

x = ["123","321"]
print(x);
y=x;
print(y);

#del y
del x
#print x;
print(y);
#应用及别名，x和y都是 ["123","321"]的引用，只要存在一个引用["123","321"]就不会丢失地址（不知道这么算不算胡掰），
# 所以x和y删除其中之一，另外一个还是有值的