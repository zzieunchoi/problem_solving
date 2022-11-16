# 중복 없는 조합
arr1 = [1, 2, 3]
arr1 = sorted(arr1)
n1= len(arr1)

visited1=[False]* n1
selected1 = [0]*n1
visited11 = []
def nojo(depth):
    if depth==n1 and visited1 not in visited11:
        visited11.append(visited1)
        print(selected1)
    else:
        for i in range(n1):
            if visited1[i]==0:
                visited1[i]=True
                selected1[depth]=arr1[i]
                nojo(depth+1)
                visited1[i]=False
nojo(0)

##############################################
# 중복 없는 순열
arr2 = [1, 2, 3]
n2 = len(arr2)

visited2=[False]*n2
selected2=[0]*n2

def nosun(depth):
    if depth==n2:
        print(selected2)
    else:
        for i in range(n2):
            if visited2[i]==0:
                visited2[i]=True
                selected2[depth]=arr2[i]
                nosun(depth+1)
                visited2[i]=False
nosun(0)

##############################################
# 중복 있는 조합
arr3 = [1, 2, 3]
arr3 = sorted(arr3)
n3= len(arr3)

selected3 = [0]*n3

def nojo(depth):
    if depth==n3:
        print(selected1)
    else:
        for i in range(n1):
            if visited1[i]==0:
                visited1[i]=True
                selected1[depth]=arr1[i]
                nojo(depth+1)
                visited1[i]=False
nojo(0)

##############################################
# 중복 있는 순열
arr4 = [1, 2, 3]
arr4 = sorted(arr4)
n4 = len(arr4)

selected4=[0]*n4

def sun(depth):
    if depth==n4:
        print(selected4)
    else:
        for i in range(n4):
            selected4[depth]=arr4[i]
            sun(depth+1)
sun(0)