import sys
from collections import deque


def search(lines, word, history=5):
    prev_lines = deque(maxlen=history)

    for line in lines:
        if word in line:
            yield line, prev_lines
        prev_lines.append(line)


for line, prevline in search(open('text_example.txt'), 'ipsum'):
    for pline in prevline:
        print(pline, end=' ')
    print(line, end=' ')
    print('-' * 15)
