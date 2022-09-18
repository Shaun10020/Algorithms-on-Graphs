#Uses python3

import sys


def negative_cycle(adj, cost):
    dist=[float('inf')]*len(adj)
    index_list=[0]
    dist[0]=0
    change=True
    iteration=0
    while change and iteration<len(adj)+1:
        change=False
        for u in range(len(adj)):
            for i in range(len(adj[u])):
                if dist[adj[u][i]]>dist[u]+cost[u][i]:
                    dist[adj[u][i]]=dist[u]+cost[u][i]
                    change=True
        iteration+=1
        if float('inf') in dist:
            index=dist.index(float('inf'))
            index_list.append(index)
            iteration=0
            change=True
            dist=[float('inf')]*len(adj)
            for x in index_list:
                dist[x]=0
    if iteration<len(adj)+1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[4,4,1,2,-5,4,1,2,2,3,2,3,1,1]
    # data=[4,3,1,2,1,2,3,2,1,3,5,1,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
