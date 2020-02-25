dic = {} # list's insert and linkedlist's search are O(n),so timeover..

for _ in range(int(input())):
    
    cmd, word = input().split()
    
    if cmd == 'insert':
        dic[word] = 1

    elif cmd == 'find':
        if dic.__contains__(word):
            print('yes')
        else:
            print('no')

class MyHashset():
    def __init__(self):
        self.hashset = [None] * 100
    
    def hash(self, key):
        pass # return unique index using key

    def add(self, key):
        pass # set key on hashed index in hashset

    def cotains(self, key):
        pass # check value on hashed index in hashset 