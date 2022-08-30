from collections import deque

num = int(input())
my_deque = deque()
passed_list = []
for _ in range(num):
    line = input().split(" ")
    if line[0] == 'READY':
        my_deque.append(line[1])
    if line[0] == 'PASSED':
        passed_list.append(my_deque.popleft())
    if line[0] == 'EXTRA':
        my_deque.append(my_deque.popleft())

print("\n".join(passed_list))