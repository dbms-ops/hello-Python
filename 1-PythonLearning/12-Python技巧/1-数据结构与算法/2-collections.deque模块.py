#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-26 23:29 
# user: lixun
# filename: 
# description: 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码 在多行上面做简单的文本匹配，
#              并返回匹配所在行的最后 N 行，
# 

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def main():
    with open('../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print pline
                print line


if __name__ == "__main__":
    main()
