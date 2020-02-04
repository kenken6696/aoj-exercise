
def mystraggle():
    if __name__ == '__main__':
        p = 0
        input_list = input().split()
        while len(input_list) > p
            if input_list[p + 1].isdecimal():
                ans = calc(input_list[p], input_list[p+1], input_list[p+2])
            else:
                ans = calc(ans, input_list[p], input_list[p+1])
            p = p + 3
        print(ans)

def calc(num1, num2, ope):
    int ans = 0
    if ope == '+':
        ans = num1 + num2
    elif ope == '-':
        ans = num1 - num2
    elif ope == '*':
        ans = num1 * num2
    return ans

def main():
    mystraggle()