#Uses python3

import sys


def acyclic(adj):
    visited=[]
    marked=[0]*len(adj)
    label=False
    for i in range(len(adj)):
        if i not in visited:
            marked[i]=1
            label=explore(adj,i,visited,marked)
            if label:
                break
            marked[i]=0
    if label:
        return 1
    return 0

def explore(adj,x,visited,marked):
    if x not in visited:
        visited.append(x)
    for i in range(len(adj[x])):
        if marked[adj[x][i]]==1:
            return True
        if adj[x][i] in visited:
            continue
        label=explore(adj,adj[x][i],visited,marked)
        if label:
            return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[5,7,1,2,2,3,1,3,3,4,1,4,2,5,3,5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
