# 逆ポーランド記法はstack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def calc(self, ope):
        ans = 0
        num1 = self.pop()
        num2 = self.pop()
        if ope == '+':
            ans = num2 + num1
        elif ope == '-':
            ans = num2 - num1
        elif ope == '*':
            ans = num2 * num1
        self.push(ans)


stack = Stack()
input_list = input().split()
for i in input_list:
    if i.isdecimal():
        stack.push(int(i))
    else:
        stack.calc(i)
print(stack.pop())