#Uses python3

import sys
import queue

def distance(adj, s, t):
    dist=[float('inf')]*len(adj)
    prev=[float('inf')]*len(adj)
    queue=[]
    dist[s]=0
    queue.append(s)
    while queue:
        u=queue.pop(0)
        for x in adj[u]:
            if dist[x]==float('inf'):
                queue.append(x)
                dist[x]=dist[u]+1
                prev[x]=u
    if dist[t]==float('inf'):
        return -1
    else:
        return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[4,4,1,2,4,1,2,3,3,1,2,4]
    # data=[5,4,5,2,1,3,3,4,1,4,3,5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
