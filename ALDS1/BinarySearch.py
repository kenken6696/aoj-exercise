# not found suitable BinarySearch module

def binary_search(a, x, lo=0, hi=None):
    """Return True if list a in item x, assuming a is sorted.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        elif a[mid] > x:
            hi = mid
        else:
            return True
    return False

same_num_count = 0
firstlist_num = int(input())
sorted_firstlist = sorted(set(input().split()))
secondlist_num = int(input())
secondlist = set(input().split())

for n in secondlist:
    if binary_search(sorted_firstlist, n):
        same_num_count += 1
print(same_num_count)