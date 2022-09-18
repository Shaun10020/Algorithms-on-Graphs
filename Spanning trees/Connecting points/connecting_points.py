#Uses python3
import sys
import math

def euclidean_distance(node_1,node_2):
    (x1,y1)=node_1
    (x2,y2)=node_2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def ExtractMin(adj,cost):
    min=float('inf')
    _i=0
    _j=0
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if cost[i][j]<min:
                min=cost[i][j]
                _i,_j=i,j
    weight=cost[_i].pop(_j)
    _j=adj[_i].pop(_j)
    return _i,_j,weight

def Union(set,u,v):
    if Findset(set,u)<Findset(set,v):
        set[Findset(set,v)]=u
    else:
        set[Findset(set,u)]=v

def Findset(set,u):
    if set[u]==u:
        return u
    else:
        return Findset(set,set[u])

def minimum_distance(x, y):
    result = 0.
    node=[]
    visited=[]
    for i in range(len(x)):
        node.append((x[i],y[i]))
    cost=[]
    adj=[]
    set=[]
    for i in range(len(x)):
        cost.append([])
        adj.append([])
        set.append(i)
    for i in range(len(x)):
        visited.append(i)
        for j in range(len(x)):
            if i==j or j in visited:
                continue
            cost[i].append(euclidean_distance(node[i],node[j]))
            adj[i].append(j)
    edges=[]
    while len(edges)<len(x)-1:
        u,v,w=ExtractMin(adj,cost)
        if Findset(set,u)!=Findset(set,v):
            edges.append((u,v))
            result+=w
            Union(set,u,v)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[4,0,0,0,1,1,0,1,1]
    # data=[5,0,0,0,2,1,1,3,0,3,2]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
