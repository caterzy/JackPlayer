# This Python file uses the following encoding: utf-8
# This Python file uses the following encoding: utf-8
__author__ = 'Administrator'


board = []

for x in range(5):
    item = ['O','O','O','O','O']
    board.append(item)

def print_board(board):
    for item in board:
        print " ".join(item);#join用于将序列中的元素以指定的字符链接生成一个新的字符串     http://www.runoob.com/python/att-string-join.html

print_board(board);