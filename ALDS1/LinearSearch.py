def use_contains():
    same_num_count = 0
    firstlist_num = int(input())
    firstlist = set(input().split())
    secondlist_num = int(input())
    secondlist = set(input().split())

    for n in secondlist:
        if firstlist.__contains__(n):
            same_num_count += 1

    print(same_num_count)

def use_intersection():
    input()
    firstlist = set(input().split())
    input()
    secondlist = set(input().split())
    same_num_count = len(firstlist.intersection(secondlist))
    print(same_num_count)

use_intersection()