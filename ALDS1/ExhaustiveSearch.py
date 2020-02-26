# 本当は動的計画法をやるべきだが

a_size = int(input())
a_list = sorted(map(int, input().split()))
input()
m_list = map(int, input().split())

def solve(a_i, m):
    
    if m == 0:
        return True
    if a_i >= a_size:
        return False
    return solve(a_i+1, m) or solve(a_i+1, m - a_list[a_i])

for m in m_list:
    if solve(0, m):
        print('yes')
    else:
        print('no')