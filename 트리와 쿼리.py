import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
connect = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
child = [[] for _ in range(n+1)]
parents = [-1] * (n+1)
sizes = [0] * (n+1)

def make_tree(curr, parent):
    global child, parents
    visited = set()
    for node in connect[curr]:
        if node != parent:
            if node in visited:
                continue
            visited.add(node)
            child[curr].append(node)
            parents[node] = curr
            make_tree(node, curr)


make_tree(r, -1)
def countSubtrees(curr):
    global sizes
    sizes[curr] = 1
    for node in child[curr]:
        countSubtrees(node)
        sizes[curr] += sizes[node]

countSubtrees(r)
for _ in range(q):
    s = int(input())
    print(sizes[s])