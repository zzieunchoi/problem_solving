n,m=4, 2
arr=list(range(1,n+1))
visited=[False]*n
selected=[0]*m
#중복 x
def permutation(depth):
    if depth==m:
        print(selected)
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            selected[depth]=arr[i]
            permutation(depth+1)
            visited[i]=False

# permutation(0)

#중복 o
def permute(depth):
    if depth==m:
        print(selected)
        return
    for i in range(n):
        selected[depth]=arr[i]
        permutation(depth+1)

permute(0)