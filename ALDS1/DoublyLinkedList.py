# collections.deque is implemented using doubly linked list at C level..
from collections import deque

linkedlist = deque()

for _ in range(int(input())):
    input_command = input()
    if input_command == 'deleteFirst':
        linkedlist.popleft()

    elif input_command == 'deleteLast':
        linkedlist.pop()
    
    else:
        com, num = input_command.split() # use str, not list to be faster
        if com == 'insert':
            linkedlist.appendleft(num)

        elif com == 'delete':
            try:
                linkedlist.remove(num)
            except ValueError: # specify a Error to be faster
                pass
            

print(' '.join(linkedlist))