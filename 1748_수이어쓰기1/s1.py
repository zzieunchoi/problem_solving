import sys
sys.stdin = open('input.txt','r')

n= int(input())
a = len(str(n))
i = 0
ssub = 0
res = 0
while i < a-1:
    ssub += (((10 ** (i+1)) -1) - (10**(i) - 1)) * (i+1)
    i+=1
    
res= ssub + (n - (10 ** (i) -1)) * (i+1)
print(res)