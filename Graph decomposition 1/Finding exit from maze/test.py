
import sys

def explore(adj, x, y,path,paths):
    path.append(x)
    if x==y:
        array=[]
        for i in range(len(path)):
            array.append(path[i])
        paths.append(array)
    for w in adj[x]:
        if w not in path:
            explore(adj, w, y,path,paths)
    path.pop()


def reach(adj, x, y):
    path = []
    paths=[]
    explore(adj, x, y,path,paths)
    return paths


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data=[4,4,1,2,3,2,4,3,1,4,1,4]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
