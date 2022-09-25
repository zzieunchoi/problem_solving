import sys
sys.stdin = open('input.txt','r')

E, S, M = map(int, input().split())
EE = 1
SS = 1
MM = 1
year =1


while(True):
    if EE ==E and SS ==S and MM == M:
        break
    EE +=1
    SS +=1
    MM +=1
    year +=1
    if EE >= 16:
        EE = EE-15
    if SS >= 29:
        SS = SS -28
    if MM >= 20:
        MM = MM -19

print(year)
