import sys
from collections import deque
sys.stdin = open('input.txt','r')

def dfs(start) :
    visited[start] = 1
    print(start, end = " ")
    for node in graph[start]:
        if visited[node] == 0:
            dfs(node)   

def bfs(start):
    queue = deque([start])
    visited[start]=1
    while queue :
        vv = queue.popleft()
        print(vv, end = " ")
        for nnode in graph[vv]:
            if visited[nnode] == 0:
                queue.append(nnode)
                visited[nnode] = 1



n, m, v = map(int, input().split())
graph = [[]  for _ in range(n+1)]

for _ in range(m):
    start_node, finish_node = map(int, input().split())
    graph[start_node].append(finish_node)
    graph[finish_node].append(start_node)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)

dfs(v)

print()
visited = [0] * (n+1)

bfs(v)