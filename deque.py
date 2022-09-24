from collections import deque


q = deque(maxlen=3) 

q.append(1)
q.append(2)
q.append(3)

print(q) #deque([1, 2, 3], maxlen=3)

q.append(4)
print(q) #deque([2, 3, 4], maxlen=3)

q.appendleft(3)
print(q) #deque([3, 2, 3], maxlen=3)


g = deque()

g.append(1)
g.append(2)

print(g.pop()) #2
print(g)#deque([1])

g.append(5)
g.appendleft(7)

print(g) #deque([7, 1, 5])

g.popleft() #7

print(g) #deque([1, 5])





