def is_contained(num, sorted_list):
    middle_index = len(sorted_list)//2
    if num > sorted_list[middle_index]:
        is_contained(num, sorted_list[middle_index:])
    elif num < sorted_list[middle_index]:
        is_contained(num, sorted_list[:middle_index])
    elif num == sorted_list[middle_index]:
        return True
    else:
        return False

same_num_count = 0
firstlist_num = int(input())
firstlist = set(input().split())
sorted_firstlist = sorted(firstlist)
secondlist_num = int(input())
secondlist = set(input().split())

for n in secondlist:
    if is_contained(n, sorted_firstlist):
        same_num_count += 1
print(same_num_count)