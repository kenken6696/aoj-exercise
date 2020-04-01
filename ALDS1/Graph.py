# convert from adjacency list to adjacency matrices
adj_list = []

adj_size = int(input())
for _ in range(adj_size):
    adj_list.append(list(map(int, input().split())))
    
adj_mtx = []
for i in adj_list:
    line = i[0] + [0 * (adj_size-1)]
    
    if i[i] == 0:
        continue
    for _ in range(i[]:
        adj_mtx[i[0]] = line