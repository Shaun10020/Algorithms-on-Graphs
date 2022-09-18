#Uses python3

import sys


def dfs(adj, used, order, x):
    for i in adj[x]:
        if used[i]==0:
            used,order=dfs(adj,used,order,i)
    if used[x]==0:
        used[x]=1
        order.append(x)
    return used,order


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for x in range(len(adj)):
        if used[x]==0:
            dfs(adj,used,order,x)
    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

